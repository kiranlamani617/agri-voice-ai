# -*- coding: utf-8 -*-
import io
import json
import os
import random
import requests

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

try:
    import openai
except ImportError:
    openai = None

try:
    import gtts
except ImportError:
    gtts = None

try:
    import joblib
    import numpy as np
    model_path = os.path.join(settings.BASE_DIR, 'ml_model', 'crop_model.pkl')
    if os.path.exists(model_path):
        ml_model = joblib.load(model_path)
    else:
        ml_model = None
except Exception as e:
    print(f"ML Model Load Notice: {e}")
    ml_model = None

from .models import QueryHistory, CropPrediction, Conversation
from .serializers import QueryHistorySerializer, CropPredictionSerializer, ConversationSerializer
from .knowledge import (
    CROPS_DATA,
    DISEASES_DATA,
    SCHEMES_DATA,
    DISTRICT_COORDINATES,
    get_weather_advisory,
    smart_agricultural_answer,
)


def home(request):
    # If client specifically asks for JSON, return JSON metadata
    if 'application/json' in request.headers.get('Accept', '') or request.GET.get('format') == 'json':
        return JsonResponse({
            "message": "AgriVoice AI API is running 🌾🚀",
            "endpoints": [
                "/api/ask/",
                "/api/tts/",
                "/api/weather/",
                "/api/crops/",
                "/api/diseases/",
                "/api/schemes/",
                "/api/predict/",
                "/api/soil/",
                "/api/forecast/",
            ]
        })

    # Otherwise serve the full frontend web app
    ui_index = os.path.join(os.path.dirname(settings.BASE_DIR), 'agrivoice-ui', 'index.html')
    if os.path.exists(ui_index):
        with open(ui_index, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='text/html; charset=utf-8')

    return JsonResponse({"message": "AgriVoice AI API is running 🌾🚀"})


def _openai_response(question, language='kn'):
    if openai is None:
        return None

    api_key = os.environ.get("OPENAI_API_KEY") or getattr(settings, "OPENAI_API_KEY", None)
    if not api_key or api_key == "your-api-key-here":
        return None

    try:
        client = openai.OpenAI(api_key=api_key)
        lang_str = "Kannada (ಕನ್ನಡ)" if language == 'kn' else ("Hindi (हिंदी)" if language == 'hi' else "English")
        system_prompt = (
            f"You are AgriVoice AI, an expert agricultural scientist and friendly farming assistant. "
            f"Respond clearly and concisely {lang_str}. "
            f"Provide actionable farming advice on crops, fertilizers, pest control, weather, or government schemes. "
            f"Keep the answer under 100 words so it can be easily spoken aloud to farmers."
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI error: {e}")
        return None


def _sarvam_response(question, language='kn'):
    api_key = os.environ.get("SARVAM_API_KEY") or getattr(settings, "SARVAM_API_KEY", None)
    if not api_key or api_key == "your-api-key-here":
        return None

    try:
        lang_instruction = "in Kannada" if language == 'kn' else "in English"
        url = "https://api.sarvam.ai/text-to-text"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        payload = {
            "model": "sarvam-2b-v0.5",
            "messages": [
                {"role": "system", "content": f"You are AgriVoice AI, a smart assistant for farmers providing practical farming guidance {lang_instruction}."},
                {"role": "user", "content": question}
            ],
            "max_tokens": 180,
            "temperature": 0.7
        }
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        print(f"Sarvam error: {e}")
        return None


# In-memory TTS byte cache to keep audio generation instant
_TTS_CACHE = {}

@api_view(['GET'])
@permission_classes([AllowAny])
def tts_view(request):
    """
    Native Text-to-Speech stream using gTTS for Kannada, English, or Hindi.
    Returns audio/mpeg.
    """
    text = request.GET.get('text', '').strip()
    lang = request.GET.get('lang', 'kn')

    if not text:
        return HttpResponse("Missing text parameter", status=400)

    # Sanitize and truncate for quick audio delivery
    clean_text = text.replace('*', '').replace('#', '').strip()[:250]
    cache_key = f"{lang}:{clean_text}"

    if cache_key in _TTS_CACHE:
        return HttpResponse(_TTS_CACHE[cache_key], content_type='audio/mpeg')

    if gtts is None:
        return HttpResponse("TTS engine not installed", status=503)

    try:
        fp = io.BytesIO()
        tts_obj = gtts.gTTS(text=clean_text, lang=lang if lang in ['kn', 'en', 'hi'] else 'kn')
        tts_obj.write_to_fp(fp)
        audio_bytes = fp.getvalue()

        # Cache if under 100 entries
        if len(_TTS_CACHE) < 100:
            _TTS_CACHE[cache_key] = audio_bytes

        response = HttpResponse(audio_bytes, content_type='audio/mpeg')
        response['Cache-Control'] = 'public, max-age=86400'
        return response
    except Exception as e:
        # Fallback to English TTS if Kannada voice encounters network glitch
        try:
            fp = io.BytesIO()
            tts_obj = gtts.gTTS(text=clean_text, lang='en')
            tts_obj.write_to_fp(fp)
            return HttpResponse(fp.getvalue(), content_type='audio/mpeg')
        except Exception:
            return HttpResponse(f"TTS Error: {str(e)}", status=500)


@api_view(['POST'])
@permission_classes([AllowAny])
def ask(request):
    """
    Main AI Farming Assistant endpoint:
    Accepts question, language (kn/en/hi), optional model override.
    Farmer can speak or type -> gets instant structured answer + audio text.
    """
    question = request.data.get("question", "").strip()
    model = request.data.get("model", "auto")
    language = request.data.get("language", "kn")

    if not question:
        return Response({"error": "Missing question field"}, status=status.HTTP_400_BAD_REQUEST)

    answer_text = None

    # Try external LLM if requested or if credentials exist
    if model == "sarvam":
        answer_text = _sarvam_response(question, language)
    elif model == "openai":
        answer_text = _openai_response(question, language)
    elif model == "auto":
        # Check if user has active external keys
        answer_text = _openai_response(question, language) or _sarvam_response(question, language)

    # High-accuracy agricultural domain reasoning fallback
    knowledge_result = smart_agricultural_answer(question, language)

    if answer_text:
        final_answer = answer_text
        audio_text = answer_text[:180]
        category = knowledge_result.get("category", "general")
        category_label = knowledge_result.get("category_label", "AI ಸಲಹೆ 🤖")
        title = knowledge_result.get("title", "ಕೃಷಿ AI ಉತ್ತರ")
    else:
        final_answer = knowledge_result["answer"]
        audio_text = knowledge_result["audio_text"]
        category = knowledge_result["category"]
        category_label = knowledge_result["category_label"]
        title = knowledge_result["title"]

    # Save to history if user is authenticated
    if request.user.is_authenticated:
        try:
            QueryHistory.objects.create(user=request.user, question=question, answer=final_answer)
            Conversation.objects.create(user=request.user, message=question, response=final_answer)
        except Exception:
            pass

    return Response({
        "answer": final_answer,
        "audio_text": audio_text,
        "audio_url": f"/api/tts/?lang={language}&text={requests.utils.quote(audio_text)}",
        "category": category,
        "category_label": category_label,
        "title": title,
        "language": language
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def weather_view(request):
    """
    Real-time Live Weather & Agricultural Advisory API for Karnataka districts.
    Fetches live data from Open-Meteo.
    """
    city_key = request.GET.get('city', 'mandya').lower().strip()
    lang = request.GET.get('lang', 'kn')

    district = DISTRICT_COORDINATES.get(city_key, DISTRICT_COORDINATES['mandya'])
    lat = district['lat']
    lon = district['lon']

    weather_data = {
        "city_key": city_key,
        "city_name_kn": district['name_kn'],
        "city_name_en": district['name_en'],
        "temperature": 27.5,
        "humidity": 65,
        "wind_speed": 9.2,
        "rain_probability": 15,
        "condition_kn": "ಭಾಗಶಃ ಮೋಡ ಕವಿದಿದೆ",
        "condition_en": "Partly Cloudy",
        "icon": "partly-cloudy",
        "forecast": []
    }

    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
            f"&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max"
            f"&timezone=Asia%2FKolkata"
        )
        r = requests.get(url, timeout=4)
        if r.status_code == 200:
            data = r.json()
            current = data.get("current", {})
            daily = data.get("daily", {})

            temp = current.get("temperature_2m", 27.5)
            hum = current.get("relative_humidity_2m", 65)
            wind = current.get("wind_speed_10m", 9.0)
            wcode = current.get("weather_code", 0)

            # Map weather code to text
            if wcode in [0, 1]:
                cond_kn, cond_en = "ಸ್ವಚ್ಛ ಆಕಾಶ (ಬಿಸಿಲು)", "Clear Sky / Sunny"
                icon = "sunny"
            elif wcode in [2, 3]:
                cond_kn, cond_en = "ಭಾಗಶಃ ಮೋಡ", "Partly Cloudy"
                icon = "partly-cloudy"
            elif wcode in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
                cond_kn, cond_en = "ಮಳೆ ಬೀಳುತ್ತಿದೆ", "Rain / Showers"
                icon = "rainy"
            elif wcode in [95, 96, 99]:
                cond_kn, cond_en = "ಗುಡುಗು ಸಹಿತ ಮಳೆ", "Thunderstorm"
                icon = "thunderstorm"
            else:
                cond_kn, cond_en = "ಮೋಡ ಕವಿದ ವಾತಾವರಣ", "Cloudy"
                icon = "cloudy"

            daily_rain_prob = 0
            if daily.get("precipitation_probability_max"):
                daily_rain_prob = daily["precipitation_probability_max"][0] or 10

            weather_data.update({
                "temperature": round(temp, 1),
                "humidity": hum,
                "wind_speed": round(wind, 1),
                "rain_probability": daily_rain_prob,
                "condition_kn": cond_kn,
                "condition_en": cond_en,
                "icon": icon,
            })

            # Process 7-day forecast
            dates = daily.get("time", [])
            max_temps = daily.get("temperature_2m_max", [])
            min_temps = daily.get("temperature_2m_min", [])
            rain_probs = daily.get("precipitation_probability_max", [])
            codes = daily.get("weather_code", [])

            forecast_list = []
            days_kn = ["ಸೋಮ", "ಮಂಗಳ", "ಬುಧ", "ಗುರು", "ಶುಕ್ರ", "ಶನಿ", "ಭಾನು"]
            days_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

            for i in range(min(7, len(dates))):
                f_rain = rain_probs[i] if i < len(rain_probs) else 10
                f_max = max_temps[i] if i < len(max_temps) else 30
                f_min = min_temps[i] if i < len(min_temps) else 20
                f_code = codes[i] if i < len(codes) else 0

                f_cond_kn = "ಬಿಸಿಲು" if f_code <= 1 else ("ಮಳೆ" if f_code >= 51 else "ಮೋಡ")
                f_cond_en = "Sunny" if f_code <= 1 else ("Rain" if f_code >= 51 else "Cloudy")

                forecast_list.append({
                    "date": dates[i],
                    "day_index": i,
                    "max_temp": round(f_max, 1),
                    "min_temp": round(f_min, 1),
                    "rain_prob": f_rain or 0,
                    "condition_kn": f_cond_kn,
                    "condition_en": f_cond_en
                })

            weather_data["forecast"] = forecast_list
    except Exception as e:
        print(f"Open-Meteo fetch notice: {e}")
        # Provide fallback forecast
        for i in range(7):
            weather_data["forecast"].append({
                "date": f"Day {i+1}",
                "day_index": i,
                "max_temp": random.randint(28, 32),
                "min_temp": random.randint(19, 23),
                "rain_prob": random.choice([10, 20, 35, 60]),
                "condition_kn": "ಭಾಗಶಃ ಮೋಡ",
                "condition_en": "Partly Cloudy"
            })

    # Generate agricultural advisory
    advisory = get_weather_advisory(
        weather_data["temperature"],
        weather_data["humidity"],
        weather_data["rain_probability"],
        lang=lang
    )

    weather_data["advisory"] = advisory
    weather_data["districts"] = [
        {"key": k, "name_kn": v["name_kn"], "name_en": v["name_en"]}
        for k, v in DISTRICT_COORDINATES.items()
    ]

    return Response(weather_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def crops(request):
    """Crop tips database endpoint"""
    return Response({"crops": CROPS_DATA})


@api_view(['GET'])
@permission_classes([AllowAny])
def diseases(request):
    """Disease solutions directory endpoint"""
    return Response({"diseases": DISEASES_DATA})


@api_view(['GET'])
@permission_classes([AllowAny])
def schemes(request):
    """Government schemes directory endpoint"""
    return Response({"schemes": SCHEMES_DATA})


def _extract_features_from_query(query):
    text = query.lower()
    rainfall = 100
    temperature = 25
    humidity = 70
    soil_ph = 6.5

    if "rain" in text or "wet" in text or "ಮಳೆ" in text or "ನೀರು" in text:
        rainfall = 150
    elif "dry" in text or "drought" in text or "ಬರ" in text or "ಒಣ" in text:
        rainfall = 55
    elif "moderate" in text:
        rainfall = 100

    if "hot" in text or "warm" in text or "ಬಿಸಿಲು" in text:
        temperature = 31
    elif "cold" in text or "cool" in text or "ಚಳಿ" in text:
        temperature = 18
    elif "temperate" in text:
        temperature = 24

    if "humid" in text or "moist" in text:
        humidity = 82
    elif "dry" in text:
        humidity = 45

    if "acidic" in text or "ಆಮ್ಲ" in text:
        soil_ph = 5.5
    elif "alkaline" in text or "ಕ್ಷಾರ" in text:
        soil_ph = 7.8

    return [rainfall, temperature, humidity, soil_ph]


def _rule_based_prediction(query):
    cond = query.lower()
    if "rain" in cond or "wet" in cond or "ಮಳೆ" in cond:
        return "🌾 Rice / ಭತ್ತ (Excellent for high rainfall conditions)"
    if "hot" in cond or "dry" in cond or "ಬರ" in cond:
        return "🌻 Sorghum / ಜೋಳ or Ragi / ರಾಗಿ (Drought tolerant crops)"
    if "cold" in cond or "frost" in cond or "ಚಳಿ" in cond:
        return "🥔 Potato / ಆಲೂಗಡ್ಡೆ (Thrives in cool climate)"
    if "nutrient" in cond or "soil" in cond or "ಮಣ್ಣು" in cond:
        return "🌿 Legumes / ಬೇಳೆಕಾಳುಗಳು (Restores natural soil nitrogen)"
    return "🌽 Maize / ಮೆಕ್ಕೆಜೋಳ (High yield, adaptable crop recommendation)"


@api_view(['POST'])
@permission_classes([AllowAny])
def predict(request):
    """
    ML Crop Prediction endpoint:
    Uses trained Random Forest model if parameters or query given.
    """
    query = request.data.get("query", "")
    rainfall = request.data.get("rainfall")
    temperature = request.data.get("temperature")
    humidity = request.data.get("humidity")
    soil_ph = request.data.get("soil_ph")

    features = None
    if rainfall is not None and temperature is not None and humidity is not None and soil_ph is not None:
        try:
            features = [float(rainfall), float(temperature), float(humidity), float(soil_ph)]
        except ValueError:
            features = None

    if features is None and query:
        features = _extract_features_from_query(query)

    if ml_model is not None and features is not None:
        try:
            pred = ml_model.predict([features])[0]
            result = f"🌾 {pred} (ML Prediction based on Climate & Soil)"
        except Exception as e:
            print(f"ML Predict Error: {e}")
            result = _rule_based_prediction(query or "general")
    else:
        result = _rule_based_prediction(query or "general")

    if request.user.is_authenticated:
        try:
            CropPrediction.objects.create(user=request.user, query=query or "parameters", result=result)
        except Exception:
            pass

    return Response({"result": result, "features": features})


@api_view(['POST'])
@permission_classes([AllowAny])
def soil(request):
    soil_type = request.data.get("soil_type", "").lower()
    moisture = request.data.get("moisture", "")

    if "clay" in soil_type or "ಜೇಡಿ" in soil_type:
        advice = "ಜೇಡಿ ಮಣ್ಣು (Clay soil): ನೀರು ನಿಧಾನವಾಗಿ ಬಸಿಯುತ್ತದೆ. ಸಾವಯವ ಕಾಂಪೋಸ್ಟ್ ಸೇರಿಸಿ ಮತ್ತು ಅತಿಯಾಗಿ ನೀರು ಹಾಯಿಸಬೇಡಿ."
    elif "sand" in soil_type or "ಮರಳು" in soil_type:
        advice = "ಮರಳು ಮಣ್ಣು (Sandy soil): ತೇವಾಂಶ ಬೇಗ ಆವಿಯಾಗುತ್ತದೆ. ಮಲ್ಚಿಂಗ್ ಮಾಡಿ ಮತ್ತು ಲಘು ನೀರಾವರಿ ನೀಡಿ."
    elif "loam" in soil_type or "ಗೋಡು" in soil_type:
        advice = "ಗೋಡು ಮಣ್ಣು (Loam soil): ಕೃಷಿಗೆ ಅತ್ಯುತ್ತಮ ಮಣ್ಣು. ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ ಸೇರಿಸಿ ಫಲವತ್ತತೆ ಕಾಪಾಡಿ."
    else:
        advice = "ಮಣ್ಣಿನ ಫಲವತ್ತತೆ ಹೆಚ್ಚಿಸಲು ಪ್ರತಿವರ್ಷ ಎಕರೆಗೆ 4-5 ಟನ್ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ ಅಥವಾ ಎರೆಹುಳು ಗೊಬ್ಬರ ಸೇರಿಸಿ."

    if moisture:
        advice += f" ಪ್ರಸ್ತುತ ತೇವಾಂಶ: {moisture}."

    return Response({"soil_advice": advice})


@api_view(['POST'])
@permission_classes([AllowAny])
def forecast(request):
    days = int(request.data.get("days", 3))
    if days < 1:
        days = 3

    forecast_data = []
    conditions = ["Sunny / ಬಿಸಿಲು", "Partly Cloudy / ಮೋಡ", "Rainy / ಮಳೆ"]
    for i in range(days):
        forecast_data.append({
            "day": f"Day {i + 1}",
            "temperature": random.randint(22, 32),
            "condition": random.choice(conditions),
        })

    return Response({"forecast": forecast_data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def history(request):
    queries = QueryHistory.objects.filter(user=request.user).order_by('-timestamp')[:10]
    serializer = QueryHistorySerializer(queries, many=True)
    return Response({"history": serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def predictions(request):
    preds = CropPrediction.objects.filter(user=request.user).order_by('-timestamp')[:10]
    serializer = CropPredictionSerializer(preds, many=True)
    return Response({"predictions": serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def conversation(request):
    convs = Conversation.objects.filter(user=request.user).order_by('-timestamp')[:20]
    serializer = ConversationSerializer(convs, many=True)
    return Response({"conversation": serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({
        "username": request.user.username,
        "email": request.user.email,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    current_password = request.data.get('current_password', '')
    new_password = request.data.get('new_password', '')
    confirm_password = request.data.get('confirm_password', '')

    if not current_password or not new_password or not confirm_password:
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    if new_password != confirm_password:
        return Response({"error": "New password and confirm password do not match."}, status=status.HTTP_400_BAD_REQUEST)

    if len(new_password) < 6:
        return Response({"error": "Password must be at least 6 characters."}, status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    if not user.check_password(current_password):
        return Response({"error": "Current password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()

    try:
        send_mail(
            subject='Your AgriVoice password has changed',
            message='Your password was successfully updated.',
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@agrivoice.local'),
            recipient_list=[user.email] if user.email else [],
            fail_silently=True,
        )
    except Exception:
        pass

    return Response({"message": "Password updated successfully."})
