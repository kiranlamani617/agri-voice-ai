# -*- coding: utf-8 -*-
from django.urls import path
from .views import (
    ask,
    crops,
    diseases,
    schemes,
    weather_view,
    tts_view,
    forecast,
    predict,
    soil,
    history,
    predictions,
    conversation,
    home,
    profile,
    change_password,
)

urlpatterns = [
    path('', home),
    path('ask/', ask),
    path('tts/', tts_view),
    path('weather/', weather_view),
    path('crops/', crops),
    path('diseases/', diseases),
    path('schemes/', schemes),
    path('predict/', predict),
    path('soil/', soil),
    path('forecast/', forecast),
    path('history/', history),
    path('predictions/', predictions),
    path('conversation/', conversation),
    path('profile/', profile),
    path('profile/change-password/', change_password),
]
