/**
 * AgriVoice AI – Core Client Application
 * Handles Voice Input (Kannada/English), AI Answer Engine, Voice Output (TTS),
 * Live Weather API, Crop Tips Database, Disease Solutions, Government Schemes, and ML Predictor.
 */

// =============================================================================
// STATE & CONFIGURATION
// =============================================================================
const STATE = {
    currentLang: 'kn',        // 'kn' (Kannada) or 'en' (English)
    isListening: false,
    isSpeaking: false,
    autoSpeak: true,
    recognition: null,
    audioContext: null,
    lastAnswerAudioText: '',
    cropsData: [],
    diseasesData: [],
    schemesData: [],
    currentDistrict: 'mandya',
    activeTab: 'tab-voice'
};

// API Base URL (Relative works with server.js proxy on port 3000 or Django on port 8000)
const API_BASE = '';

// =============================================================================
// INITIALIZATION
// =============================================================================
document.addEventListener('DOMContentLoaded', () => {
    initNavigationTabs();
    initLanguageSelector();
    initSpeechRecognition();
    initVoiceControls();
    initQuickPrompts();
    initTextFallbackForm();
    initWeatherModule();
    initCropsModule();
    initDiseasesModule();
    initSchemesModule();
    initMLPredictorModule();

    // Check backend connection & load initial data
    loadInitialData();
});

// =============================================================================
// AUDIO TONES (Web Audio API for farmer feedback)
// =============================================================================
function playTone(type = 'start') {
    try {
        if (!STATE.audioContext) {
            STATE.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (STATE.audioContext.state === 'suspended') {
            STATE.audioContext.resume();
        }

        const osc = STATE.audioContext.createOscillator();
        const gain = STATE.audioContext.createGain();
        osc.connect(gain);
        gain.connect(STATE.audioContext.destination);

        const now = STATE.audioContext.currentTime;
        if (type === 'start') {
            // High chime for mic start
            osc.frequency.setValueAtTime(440, now);
            osc.frequency.exponentialRampToValueAtTime(880, now + 0.15);
            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
            osc.start(now);
            osc.stop(now + 0.25);
        } else if (type === 'success') {
            // Double pleasant chime
            osc.frequency.setValueAtTime(523.25, now);
            osc.frequency.setValueAtTime(659.25, now + 0.1);
            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            osc.start(now);
            osc.stop(now + 0.3);
        }
    } catch (e) {
        console.warn('Audio tone note:', e);
    }
}

// =============================================================================
// NAVIGATION & TABS
// =============================================================================
function initNavigationTabs() {
    const tabs = document.querySelectorAll('.nav-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.dataset.target;
            switchTab(targetId);
        });
    });

    // Header weather chip opens weather tab
    const weatherChip = document.getElementById('header-weather-chip');
    if (weatherChip) {
        weatherChip.addEventListener('click', () => switchTab('tab-weather'));
    }
}

function switchTab(targetId) {
    document.querySelectorAll('.nav-tab').forEach(t => {
        t.classList.toggle('active', t.dataset.target === targetId);
    });

    document.querySelectorAll('.tab-content').forEach(c => {
        c.classList.toggle('active', c.id === targetId);
    });

    STATE.activeTab = targetId;
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// =============================================================================
// LANGUAGE SWITCHER
// =============================================================================
function initLanguageSelector() {
    const knBtn = document.getElementById('lang-kn-btn');
    const enBtn = document.getElementById('lang-en-btn');

    knBtn.addEventListener('click', () => setLanguage('kn'));
    enBtn.addEventListener('click', () => setLanguage('en'));
}

function setLanguage(lang) {
    STATE.currentLang = lang;

    document.getElementById('lang-kn-btn').classList.toggle('active', lang === 'kn');
    document.getElementById('lang-en-btn').classList.toggle('active', lang === 'en');
    document.documentElement.lang = lang;

    // Update all text with data attributes
    document.querySelectorAll('[data-kn]').forEach(el => {
        const text = el.getAttribute(`data-${lang}`);
        if (text) {
            el.textContent = text;
        }
    });

    // Update placeholders
    document.querySelectorAll('[data-placeholder-kn]').forEach(el => {
        const ph = el.getAttribute(`data-placeholder-${lang}`);
        if (ph) {
            el.placeholder = ph;
        }
    });

    // Update speech recognition language
    if (STATE.recognition) {
        STATE.recognition.lang = lang === 'kn' ? 'kn-IN' : 'en-IN';
    }

    // Refresh weather advisory text for new language
    fetchWeatherData(STATE.currentDistrict);

    // Re-render crops & diseases in target language
    renderCrops();
    renderDiseases();
    renderSchemes();
}

// =============================================================================
// VOICE INPUT (SPEECH RECOGNITION)
// =============================================================================
function initSpeechRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const micBtn = document.getElementById('main-mic-btn');
    const statusText = document.getElementById('voice-status-text');
    const statusBadge = document.getElementById('voice-status-badge');
    const soundWave = document.getElementById('sound-wave-bars');
    const transcriptBox = document.getElementById('transcript-box');
    const transcriptText = document.getElementById('transcript-text');

    if (!SpeechRecognition) {
        console.warn('Web Speech API not natively supported on this browser.');
        if (statusText) {
            statusText.textContent = STATE.currentLang === 'kn' 
                ? 'ಧ್ವನಿ ಲಭ್ಯವಿಲ್ಲ, ಕೆಳಗಿನ ಪ್ರಶ್ನೆಗಳನ್ನು ಸ್ಪರ್ಶಿಸಿ' 
                : 'Mic not supported, tap questions below';
        }
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = STATE.currentLang === 'kn' ? 'kn-IN' : 'en-IN';
    STATE.recognition = recognition;

    recognition.onstart = () => {
        STATE.isListening = true;
        playTone('start');
        stopVoiceOutput();

        micBtn.classList.add('listening');
        soundWave.classList.add('active');
        statusBadge.className = 'voice-status-badge status-listening';
        statusText.textContent = STATE.currentLang === 'kn' ? '🎙️ ಆಲಿಸಲಾಗುತ್ತಿದೆ... ಮಾತನಾಡಿ' : '🎙️ Listening... Speak now';
        
        transcriptBox.style.display = 'block';
        transcriptText.textContent = STATE.currentLang === 'kn' ? 'ಆಲಿಸಲಾಗುತ್ತಿದೆ...' : 'Listening...';
    };

    recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            transcript += event.results[i][0].transcript;
        }
        transcriptText.textContent = transcript;

        // If finalized speech detected
        if (event.results[0].isFinal) {
            const finalQuery = transcript.trim();
            if (finalQuery.length > 0) {
                handleUserQuery(finalQuery);
            }
        }
    };

    recognition.onerror = (event) => {
        console.warn('Speech recognition event:', event.error);
        STATE.isListening = false;
        micBtn.classList.remove('listening');
        soundWave.classList.remove('active');
        statusBadge.className = 'voice-status-badge status-idle';
        
        if (event.error === 'not-allowed') {
            statusText.textContent = STATE.currentLang === 'kn' 
                ? '⚠️ ಮೈಕ್ರೋಫೋನ್ ಅನುಮತಿ ನೀಡಿ' 
                : '⚠️ Microphone permission denied';
        } else {
            statusText.textContent = STATE.currentLang === 'kn' 
                ? 'ಮೈಕ್ ಒತ್ತಿ ಮತ್ತೊಮ್ಮೆ ಮಾತನಾಡಿ' 
                : 'Tap mic and try speaking again';
        }
    };

    recognition.onend = () => {
        STATE.isListening = false;
        micBtn.classList.remove('listening');
        soundWave.classList.remove('active');
        statusBadge.className = 'voice-status-badge status-idle';
    };

    // Main mic button click handler
    micBtn.addEventListener('click', () => {
        if (STATE.isListening) {
            recognition.stop();
        } else {
            try {
                recognition.lang = STATE.currentLang === 'kn' ? 'kn-IN' : 'en-IN';
                recognition.start();
            } catch (err) {
                console.error('Recognition start error:', err);
            }
        }
    });
}

// =============================================================================
// AI ANSWER SYSTEM & QUERY HANDLER
// =============================================================================
async function handleUserQuery(question) {
    if (!question || question.trim().length === 0) return;

    const statusBadge = document.getElementById('voice-status-badge');
    const statusText = document.getElementById('voice-status-text');
    const answerCard = document.getElementById('answer-card');
    const answerTitle = document.getElementById('answer-title');
    const answerBody = document.getElementById('answer-body');
    const categoryBadge = document.getElementById('answer-category-badge');
    const langTag = document.getElementById('answer-lang-tag');

    // UI state: processing
    statusBadge.className = 'voice-status-badge status-processing';
    statusText.textContent = STATE.currentLang === 'kn' ? '⚡ ಕೃಷಿ AI ಉತ್ತರಿಸುತ್ತಿದೆ...' : '⚡ AgriVoice AI analyzing...';

    try {
        const response = await fetch(`${API_BASE}/api/ask/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                question: question,
                language: STATE.currentLang,
                model: 'auto'
            })
        });

        if (!response.ok) {
            throw new Error(`Server returned HTTP ${response.status}`);
        }

        const data = await response.json();
        playTone('success');

        // Render Answer Card
        answerCard.style.display = 'block';
        answerTitle.textContent = data.title || (STATE.currentLang === 'kn' ? 'ಕೃಷಿ ಸಲಹೆಗಾರ ಉತ್ತರ' : 'Farming Advisory');
        answerBody.innerHTML = formatMarkdown(data.answer);
        categoryBadge.textContent = data.category_label || '🌾 ಬೆಳೆ ಸಲಹೆ';
        langTag.textContent = STATE.currentLang === 'kn' ? 'ಕನ್ನಡ' : 'English';

        STATE.lastAnswerAudioText = data.audio_text || data.answer;

        // Reset voice status text
        statusBadge.className = 'voice-status-badge status-idle';
        statusText.textContent = STATE.currentLang === 'kn' ? 'ಮೈಕ್ ಒತ್ತಿ ಮಾತನಾಡಿ' : 'Tap mic and speak';

        // Auto-speak voice output
        if (STATE.autoSpeak && STATE.lastAnswerAudioText) {
            speakVoiceOutput(STATE.lastAnswerAudioText, STATE.currentLang);
        }

        // Scroll smoothly to answer
        answerCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    } catch (err) {
        console.error('Ask Query Error:', err);
        statusBadge.className = 'voice-status-badge status-idle';
        statusText.textContent = STATE.currentLang === 'kn' ? 'ಉತ್ತರ ಪಡೆಯಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ' : 'Could not fetch response';
    }
}

function formatMarkdown(text) {
    if (!text) return '';
    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/• (.*?)(?:\n|$)/g, '<li>$1</li>')
        .replace(/\n\n/g, '<br><br>');
}

// =============================================================================
// VOICE OUTPUT (TTS: Browser SpeechSynthesis + gTTS Streaming Fallback)
// =============================================================================
function initVoiceControls() {
    const replayBtn = document.getElementById('replay-voice-btn');
    const stopBtn = document.getElementById('stop-voice-btn');
    const toggleAudioBtn = document.getElementById('toggle-audio-btn');
    const audioIcon = document.getElementById('audio-icon');
    const audioLabel = document.getElementById('audio-label');

    if (replayBtn) {
        replayBtn.addEventListener('click', () => {
            if (STATE.lastAnswerAudioText) {
                speakVoiceOutput(STATE.lastAnswerAudioText, STATE.currentLang);
            }
        });
    }

    if (stopBtn) {
        stopBtn.addEventListener('click', stopVoiceOutput);
    }

    if (toggleAudioBtn) {
        toggleAudioBtn.addEventListener('click', () => {
            STATE.autoSpeak = !STATE.autoSpeak;
            audioIcon.textContent = STATE.autoSpeak ? '🔊' : '🔇';
            audioLabel.textContent = STATE.autoSpeak 
                ? (STATE.currentLang === 'kn' ? 'ಧ್ವನಿ ಆನ್' : 'Voice ON') 
                : (STATE.currentLang === 'kn' ? 'ಧ್ವನಿ ಆಫ್' : 'Voice OFF');
            
            if (!STATE.autoSpeak) {
                stopVoiceOutput();
            }
        });
    }
}

function speakVoiceOutput(text, lang = 'kn') {
    if (!text) return;
    stopVoiceOutput();

    // Priority 1: Web Speech API window.speechSynthesis
    if ('speechSynthesis' in window) {
        const cleanText = text.replace(/[*#]/g, '').trim();
        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = lang === 'kn' ? 'kn-IN' : 'en-IN';
        utterance.rate = 0.95; // Slightly slower for crisp clarity
        utterance.pitch = 1.0;

        // Try to match a native Indian or Kannada voice
        const voices = window.speechSynthesis.getVoices();
        const targetVoice = voices.find(v => v.lang.startsWith(lang) || v.lang.includes(lang === 'kn' ? 'kn' : 'en-IN'));
        if (targetVoice) {
            utterance.voice = targetVoice;
        }

        utterance.onstart = () => { STATE.isSpeaking = true; };
        utterance.onend = () => { STATE.isSpeaking = false; };
        utterance.onerror = () => { 
            STATE.isSpeaking = false;
            // If browser TTS fails, fallback to backend gTTS streaming
            streamBackendTTS(cleanText, lang);
        };

        window.speechSynthesis.speak(utterance);
        return;
    }

    // Priority 2: Fallback to backend gTTS stream
    streamBackendTTS(text, lang);
}

function streamBackendTTS(text, lang = 'kn') {
    const audioPlayer = document.getElementById('tts-audio-player');
    if (!audioPlayer) return;

    try {
        const cleanText = encodeURIComponent(text.replace(/[*#]/g, '').trim().substring(0, 200));
        audioPlayer.src = `${API_BASE}/api/tts/?lang=${lang}&text=${cleanText}`;
        audioPlayer.play().catch(e => console.warn('Audio play notice:', e));
    } catch (e) {
        console.error('Backend TTS Stream Error:', e);
    }
}

function stopVoiceOutput() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    const audioPlayer = document.getElementById('tts-audio-player');
    if (audioPlayer) {
        audioPlayer.pause();
        audioPlayer.currentTime = 0;
    }
    STATE.isSpeaking = false;
}

// =============================================================================
// QUICK PROMPT CHIPS & TEXT FALLBACK
// =============================================================================
function initQuickPrompts() {
    const chips = document.querySelectorAll('.prompt-chip');
    chips.forEach(chip => {
        chip.addEventListener('click', () => {
            const query = STATE.currentLang === 'kn' ? chip.dataset.query : (chip.dataset.queryEn || chip.dataset.query);
            
            const transcriptBox = document.getElementById('transcript-box');
            const transcriptText = document.getElementById('transcript-text');
            if (transcriptBox && transcriptText) {
                transcriptBox.style.display = 'block';
                transcriptText.textContent = query;
            }

            handleUserQuery(query);
        });
    });
}

function initTextFallbackForm() {
    const form = document.getElementById('text-ask-form');
    const input = document.getElementById('text-query-input');

    if (form && input) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const q = input.value.trim();
            if (q.length > 0) {
                const transcriptBox = document.getElementById('transcript-box');
                const transcriptText = document.getElementById('transcript-text');
                if (transcriptBox && transcriptText) {
                    transcriptBox.style.display = 'block';
                    transcriptText.textContent = q;
                }

                handleUserQuery(q);
                input.value = '';
            }
        });
    }
}

// =============================================================================
// TAB 2: LIVE WEATHER & ADVISORY
// =============================================================================
function initWeatherModule() {
    const select = document.getElementById('district-select');
    const refreshBtn = document.getElementById('refresh-weather-btn');
    const advisoryAudioBtn = document.getElementById('advisory-audio-btn');

    if (select) {
        select.addEventListener('change', (e) => {
            STATE.currentDistrict = e.target.value;
            fetchWeatherData(STATE.currentDistrict);
        });
    }

    if (refreshBtn) {
        refreshBtn.addEventListener('click', () => fetchWeatherData(STATE.currentDistrict));
    }

    if (advisoryAudioBtn) {
        advisoryAudioBtn.addEventListener('click', () => {
            const headline = document.getElementById('advisory-headline').textContent;
            const spray = document.getElementById('advisory-spraying').textContent;
            const textToSpeak = `${headline}. ${spray}`;
            speakVoiceOutput(textToSpeak, STATE.currentLang);
        });
    }

    // Initial weather load
    fetchWeatherData('mandya');
}

async function fetchWeatherData(districtKey = 'mandya') {
    try {
        const res = await fetch(`${API_BASE}/api/weather/?city=${districtKey}&lang=${STATE.currentLang}`);
        if (!res.ok) throw new Error('Weather API error');
        const data = await res.json();

        // Update Header Mini Weather
        const headerTemp = document.getElementById('header-temp');
        const headerCity = document.getElementById('header-city');
        if (headerTemp) headerTemp.textContent = `${data.temperature}°C`;
        if (headerCity) headerCity.textContent = STATE.currentLang === 'kn' ? data.city_name_kn : data.city_name_en;

        // Update Weather Hero
        const cityBadge = document.getElementById('weather-city-badge');
        const mainTemp = document.getElementById('weather-main-temp');
        const mainCond = document.getElementById('weather-main-cond');
        const mainIcon = document.getElementById('weather-main-icon');
        const humVal = document.getElementById('weather-humidity');
        const rainVal = document.getElementById('weather-rain-prob');
        const windVal = document.getElementById('weather-wind');
        const sprayStatus = document.getElementById('weather-spray-status');

        if (cityBadge) cityBadge.textContent = `${STATE.currentLang === 'kn' ? data.city_name_kn : data.city_name_en} ${STATE.currentLang === 'kn' ? 'ಜಿಲ್ಲೆ' : 'District'}`;
        if (mainTemp) mainTemp.textContent = `${data.temperature}°C`;
        if (mainCond) mainCond.textContent = STATE.currentLang === 'kn' ? data.condition_kn : data.condition_en;
        if (humVal) humVal.textContent = `${data.humidity}%`;
        if (rainVal) rainVal.textContent = `${data.rain_probability}%`;
        if (windVal) windVal.textContent = `${data.wind_speed} km/h`;

        // Weather icon
        if (mainIcon) {
            if (data.icon === 'sunny') mainIcon.textContent = '☀️';
            else if (data.icon === 'rainy') mainIcon.textContent = '🌧️';
            else if (data.icon === 'thunderstorm') mainIcon.textContent = '⛈️';
            else mainIcon.textContent = '⛅';
        }

        // Spray condition badge
        if (sprayStatus) {
            if (data.rain_probability >= 50) {
                sprayStatus.textContent = STATE.currentLang === 'kn' ? 'ಸಿಂಪಡಿಸಬೇಡಿ ❌' : 'Avoid Spray ❌';
                sprayStatus.style.color = '#f87171';
            } else {
                sprayStatus.textContent = STATE.currentLang === 'kn' ? 'ಅನುಕೂಲಕರ ✅' : 'Favourable ✅';
                sprayStatus.style.color = '#86efac';
            }
        }

        // Advisory Card
        if (data.advisory) {
            const adv = data.advisory;
            const hLine = document.getElementById('advisory-headline');
            const spray = document.getElementById('advisory-spraying');
            const irrig = document.getElementById('advisory-irrigation');
            const drain = document.getElementById('advisory-drainage');

            if (hLine) hLine.textContent = adv.headline || 'ಕೃಷಿ ಸಲಹೆ';
            if (spray) spray.textContent = adv.spraying || '';
            if (irrig) irrig.textContent = adv.irrigation || '';
            if (drain) drain.textContent = adv.drainage || '';
        }

        // 7-Day Forecast Grid
        const forecastGrid = document.getElementById('forecast-cards-grid');
        if (forecastGrid && data.forecast) {
            forecastGrid.innerHTML = data.forecast.map((f, idx) => {
                const dayName = getDayName(f.date, idx, STATE.currentLang);
                const condText = STATE.currentLang === 'kn' ? f.condition_kn : f.condition_en;
                const icon = f.rain_prob >= 50 ? '🌧️' : (f.max_temp >= 32 ? '☀️' : '⛅');

                return `
                    <div class="forecast-card">
                        <div class="forecast-day">${dayName}</div>
                        <div class="forecast-icon">${icon}</div>
                        <div class="forecast-temps">${f.max_temp}° <span>/ ${f.min_temp}°</span></div>
                        <span class="forecast-rain-pill">💧 ${f.rain_prob}%</span>
                    </div>
                `;
            }).join('');
        }

    } catch (err) {
        console.error('Weather fetch error:', err);
    }
}

function getDayName(dateStr, index, lang) {
    const daysKn = ['ಭಾನುವಾರ', 'ಸೋಮವಾರ', 'ಮಂಗಳವಾರ', 'ಬುಧವಾರ', 'ಗುರುವಾರ', 'ಶುಕ್ರವಾರ', 'ಶನಿವಾರ'];
    const daysEn = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    try {
        const d = new Date(dateStr);
        if (!isNaN(d.getDay())) {
            return lang === 'kn' ? daysKn[d.getDay()] : daysEn[d.getDay()];
        }
    } catch (e) {}

    return lang === 'kn' ? `ದಿನ ${index + 1}` : `Day ${index + 1}`;
}

// =============================================================================
// TAB 3: CROP TIPS DATABASE
// =============================================================================
function initCropsModule() {
    const searchInput = document.getElementById('crop-search-input');
    const pills = document.querySelectorAll('.cat-pill');

    if (searchInput) {
        searchInput.addEventListener('input', () => renderCrops());
    }

    pills.forEach(pill => {
        pill.addEventListener('click', () => {
            pills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            renderCrops();
        });
    });
}

async function loadCropsData() {
    try {
        const res = await fetch(`${API_BASE}/api/crops/`);
        if (res.ok) {
            const data = await res.json();
            STATE.cropsData = data.crops || [];
            renderCrops();
        }
    } catch (e) {
        console.warn('Crops API note:', e);
    }
}

function renderCrops() {
    const grid = document.getElementById('crops-grid');
    if (!grid) return;

    const searchTerm = (document.getElementById('crop-search-input')?.value || '').toLowerCase();
    const activeCat = document.querySelector('.cat-pill.active')?.dataset.cat || 'all';

    const filtered = STATE.cropsData.filter(crop => {
        const nameKn = (crop.name_kn || '').toLowerCase();
        const nameEn = (crop.name_en || '').toLowerCase();
        const matchesSearch = nameKn.includes(searchTerm) || nameEn.includes(searchTerm);
        const matchesCat = activeCat === 'all' || crop.category === activeCat;
        return matchesSearch && matchesCat;
    });

    if (filtered.length === 0) {
        grid.innerHTML = `<p style="grid-column: 1/-1; text-align: center; color: var(--text-muted); padding: 2rem;">${STATE.currentLang === 'kn' ? 'ಯಾವುದೇ ಬೆಳೆ ಕಂಡುಬಂದಿಲ್ಲ.' : 'No crops found matching search.'}</p>`;
        return;
    }

    grid.innerHTML = filtered.map(crop => {
        const name = STATE.currentLang === 'kn' ? crop.name_kn : crop.name_en;
        const season = STATE.currentLang === 'kn' ? crop.season_kn : crop.season_en;
        const soil = STATE.currentLang === 'kn' ? crop.soil_kn : crop.soil_en;
        const water = STATE.currentLang === 'kn' ? crop.water_kn : crop.water_en;
        const fert = STATE.currentLang === 'kn' ? crop.fertilizer_kn : crop.fertilizer_en;
        const pest = STATE.currentLang === 'kn' ? crop.pests_diseases_kn : crop.pests_diseases_en;
        const yld = STATE.currentLang === 'kn' ? crop.yield_kn : crop.yield_en;
        const audioText = STATE.currentLang === 'kn' ? crop.audio_summary_kn : crop.audio_summary_en;

        return `
            <div class="crop-card">
                <div>
                    <div class="crop-card-header">
                        <h3 class="crop-name">${name}</h3>
                        <span class="crop-cat-tag">${crop.category}</span>
                    </div>

                    <div class="crop-detail-list">
                        <div class="crop-detail-row">
                            <strong>🗓️ ${STATE.currentLang === 'kn' ? 'ಬಿತ್ತನೆ ಕಾಲ:' : 'Season:'}</strong>
                            <span>${season}</span>
                        </div>
                        <div class="crop-detail-row">
                            <strong>🌱 ${STATE.currentLang === 'kn' ? 'ಮಣ್ಣು:' : 'Soil:'}</strong>
                            <span>${soil}</span>
                        </div>
                        <div class="crop-detail-row">
                            <strong>💧 ${STATE.currentLang === 'kn' ? 'ನೀರು:' : 'Water:'}</strong>
                            <span>${water}</span>
                        </div>
                        <div class="crop-detail-row">
                            <strong>🧪 ${STATE.currentLang === 'kn' ? 'ಗೊಬ್ಬರ:' : 'Fertilizer:'}</strong>
                            <span>${fert}</span>
                        </div>
                        <div class="crop-detail-row">
                            <strong>🛡️ ${STATE.currentLang === 'kn' ? 'ರೋಗ ನಿರ್ವಹಣೆ:' : 'Pest/Disease:'}</strong>
                            <span>${pest}</span>
                        </div>
                    </div>
                </div>

                <div class="crop-card-footer">
                    <span class="crop-yield-badge">📈 ${yld}</span>
                    <button class="audio-ctrl-btn crop-listen-btn" data-audio="${encodeURIComponent(audioText)}">
                        <span>🔊 ${STATE.currentLang === 'kn' ? 'ಕೇಳಿ' : 'Listen'}</span>
                    </button>
                </div>
            </div>
        `;
    }).join('');

    // Attach audio listeners to buttons
    document.querySelectorAll('.crop-listen-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const text = decodeURIComponent(btn.dataset.audio);
            speakVoiceOutput(text, STATE.currentLang);
        });
    });
}

// =============================================================================
// TAB 4: DISEASE DOCTOR
// =============================================================================
function initDiseasesModule() {
    const tags = document.querySelectorAll('.crop-tag-btn');
    tags.forEach(btn => {
        btn.addEventListener('click', () => {
            tags.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderDiseases();
        });
    });
}

async function loadDiseasesData() {
    try {
        const res = await fetch(`${API_BASE}/api/diseases/`);
        if (res.ok) {
            const data = await res.json();
            STATE.diseasesData = data.diseases || [];
            renderDiseases();
        }
    } catch (e) {
        console.warn('Diseases API note:', e);
    }
}

function renderDiseases() {
    const grid = document.getElementById('diseases-grid');
    if (!grid) return;

    const activeFilter = document.querySelector('.crop-tag-btn.active')?.dataset.filter || 'all';

    const filtered = STATE.diseasesData.filter(d => {
        if (activeFilter === 'all') return true;
        return (d.crop || '').toLowerCase().includes(activeFilter.toLowerCase());
    });

    grid.innerHTML = filtered.map(d => {
        const name = STATE.currentLang === 'kn' ? d.disease_kn : d.disease_en;
        const sym = STATE.currentLang === 'kn' ? d.symptoms_kn : d.symptoms_en;
        const org = STATE.currentLang === 'kn' ? d.organic_remedy_kn : d.organic_remedy_en;
        const chem = STATE.currentLang === 'kn' ? d.chemical_remedy_kn : d.chemical_remedy_en;
        const prev = STATE.currentLang === 'kn' ? d.prevention_kn : d.prevention_en;
        const audioText = STATE.currentLang === 'kn' ? (d.audio_kn || sym) : (d.disease_en + ': ' + chem);

        return `
            <div class="disease-card">
                <div>
                    <h3 class="disease-card-title">${name}</h3>
                    <span class="disease-crop-name">🌱 ${d.crop}</span>
                </div>

                <div class="disease-info-block">
                    <strong>🔍 ${STATE.currentLang === 'kn' ? 'ರೋಗ ಲಕ್ಷಣಗಳು:' : 'Symptoms:'}</strong>
                    <span>${sym}</span>
                </div>

                <div class="remedy-split">
                    <div class="remedy-box remedy-organic">
                        <strong>🌿 ${STATE.currentLang === 'kn' ? 'ಸಾವಯವ ಪರಿಹಾರ:' : 'Organic Remedy:'}</strong>
                        <span>${org}</span>
                    </div>
                    <div class="remedy-box remedy-chemical">
                        <strong>🧪 ${STATE.currentLang === 'kn' ? 'ರಾಸಾಯನಿಕ ಸಿಂಪಡಣೆ:' : 'Chemical Spray:'}</strong>
                        <span>${chem}</span>
                    </div>
                </div>

                <div class="disease-info-block">
                    <strong>🛡️ ${STATE.currentLang === 'kn' ? 'ಮುನ್ನೆಚ್ಚರಿಕೆ ಕ್ರಮ:' : 'Prevention:'}</strong>
                    <span>${prev}</span>
                </div>

                <button class="audio-ctrl-btn disease-listen-btn" style="align-self: flex-start;" data-audio="${encodeURIComponent(audioText)}">
                    <span>🔊 ${STATE.currentLang === 'kn' ? 'ಪರಿಹಾರ ಕೇಳಿ' : 'Listen Remedy'}</span>
                </button>
            </div>
        `;
    }).join('');

    document.querySelectorAll('.disease-listen-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const text = decodeURIComponent(btn.dataset.audio);
            speakVoiceOutput(text, STATE.currentLang);
        });
    });
}

// =============================================================================
// TAB 5: GOVERNMENT SCHEMES
// =============================================================================
function initSchemesModule() {
    // Event listeners if any
}

async function loadSchemesData() {
    try {
        const res = await fetch(`${API_BASE}/api/schemes/`);
        if (res.ok) {
            const data = await res.json();
            STATE.schemesData = data.schemes || [];
            renderSchemes();
        }
    } catch (e) {
        console.warn('Schemes API note:', e);
    }
}

function renderSchemes() {
    const grid = document.getElementById('schemes-grid');
    if (!grid) return;

    grid.innerHTML = STATE.schemesData.map(s => {
        const name = STATE.currentLang === 'kn' ? s.name_kn : s.name_en;
        const ben = STATE.currentLang === 'kn' ? s.benefit_kn : s.benefit_en;
        const elig = STATE.currentLang === 'kn' ? s.eligibility_kn : s.eligibility_en;
        const doc = STATE.currentLang === 'kn' ? s.documents_kn : s.documents_en;
        const apply = STATE.currentLang === 'kn' ? s.apply_kn : s.apply_en;
        const audioText = STATE.currentLang === 'kn' ? s.audio_kn : `${s.name_en}: ${s.benefit_en}`;

        return `
            <div class="scheme-card">
                <div>
                    <div class="scheme-header">
                        <h3 class="scheme-title">${name}</h3>
                    </div>

                    <div class="scheme-benefit-box">
                        💰 <strong>${STATE.currentLang === 'kn' ? 'ಸಹಾಯಧನ & ಲಾಭ:' : 'Benefit & Subsidy:'}</strong> ${ben}
                    </div>

                    <div class="scheme-details">
                        <div><strong>👨‍🌾 ${STATE.currentLang === 'kn' ? 'ಅರ್ಹತೆ:' : 'Eligibility:'}</strong> ${elig}</div>
                        <div><strong>📑 ${STATE.currentLang === 'kn' ? 'ಅಗತ್ಯ ದಾಖಲೆಗಳು:' : 'Documents:'}</strong> ${doc}</div>
                        <div><strong>📌 ${STATE.currentLang === 'kn' ? 'ಅರ್ಜಿ ವಿಧಾನ:' : 'How to Apply:'}</strong> ${apply}</div>
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; border-top: 1px solid var(--border-light); padding-top: 0.75rem;">
                    <a href="tel:18001801551" class="audio-ctrl-btn" style="text-decoration: none;">
                        <span>📞 ಸಹಾಯವಾಣಿ</span>
                    </a>
                    <button class="audio-ctrl-btn scheme-listen-btn" data-audio="${encodeURIComponent(audioText)}">
                        <span>🔊 ${STATE.currentLang === 'kn' ? 'ವಿವರ ಕೇಳಿ' : 'Listen Details'}</span>
                    </button>
                </div>
            </div>
        `;
    }).join('');

    document.querySelectorAll('.scheme-listen-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const text = decodeURIComponent(btn.dataset.audio);
            speakVoiceOutput(text, STATE.currentLang);
        });
    });
}

// =============================================================================
// TAB 6: AI ML CROP PREDICTOR
// =============================================================================
function initMLPredictorModule() {
    const form = document.getElementById('ml-predict-form');
    const presets = document.querySelectorAll('.preset-btn');
    const listenPredBtn = document.getElementById('listen-prediction-btn');

    presets.forEach(btn => {
        btn.addEventListener('click', () => {
            document.getElementById('input-rainfall').value = btn.dataset.rain;
            document.getElementById('input-temp').value = btn.dataset.temp;
            document.getElementById('input-humidity').value = btn.dataset.hum;
            document.getElementById('input-ph').value = btn.dataset.ph;
        });
    });

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const rain = document.getElementById('input-rainfall').value;
            const temp = document.getElementById('input-temp').value;
            const hum = document.getElementById('input-humidity').value;
            const ph = document.getElementById('input-ph').value;

            const submitBtn = document.getElementById('predict-submit-btn');
            submitBtn.textContent = STATE.currentLang === 'kn' ? 'ಲೆಕ್ಕಾಚಾರ ಮಾಡಲಾಗುತ್ತಿದೆ...' : 'Analyzing...';
            submitBtn.disabled = true;

            try {
                const res = await fetch(`${API_BASE}/api/predict/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        rainfall: rain,
                        temperature: temp,
                        humidity: hum,
                        soil_ph: ph
                    })
                });

                if (res.ok) {
                    const data = await res.json();
                    document.getElementById('result-placeholder').style.display = 'none';
                    const activeContent = document.getElementById('result-active-content');
                    activeContent.style.display = 'block';

                    const cropTitle = document.getElementById('predicted-crop-name');
                    cropTitle.textContent = data.result;

                    const summaryBox = document.getElementById('features-summary');
                    summaryBox.innerHTML = `
                        <span class="feat-pill">🌧️ ಮಳೆ: ${rain} mm</span>
                        <span class="feat-pill">🌡️ ತಾಪಮಾನ: ${temp} °C</span>
                        <span class="feat-pill">💧 ಆರ್ದ್ರತೆ: ${hum} %</span>
                        <span class="feat-pill">🧪 pH: ${ph}</span>
                    `;

                    if (STATE.autoSpeak) {
                        speakVoiceOutput(data.result, STATE.currentLang);
                    }
                }
            } catch (err) {
                console.error('ML Prediction error:', err);
            } finally {
                submitBtn.textContent = STATE.currentLang === 'kn' ? '🌾 ಬೆಳೆ ಶಿಫಾರಸು ಪಡೆಯಿರಿ' : '🌾 Predict Best Crop';
                submitBtn.disabled = false;
            }
        });
    }

    if (listenPredBtn) {
        listenPredBtn.addEventListener('click', () => {
            const cropTitle = document.getElementById('predicted-crop-name').textContent;
            speakVoiceOutput(cropTitle, STATE.currentLang);
        });
    }
}

// =============================================================================
// INITIAL DATA LOADER
// =============================================================================
function loadInitialData() {
    loadCropsData();
    loadDiseasesData();
    loadSchemesData();
}
