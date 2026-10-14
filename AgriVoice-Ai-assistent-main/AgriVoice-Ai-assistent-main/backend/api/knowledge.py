# -*- coding: utf-8 -*-
"""
AgriVoice AI - Agricultural Knowledge Base & Natural Language Engine
Provides comprehensive domain intelligence in Kannada and English for:
1. Crop Advice 🌾
2. Weather Updates 🌦️
3. Disease & Pest Solutions 🦠
4. Government Schemes Info 📄
"""

# ==========================================
# 1. CROP TIPS DATABASE
# ==========================================
CROPS_DATA = [
    {
        "id": "ragi",
        "name_kn": "ರಾಗಿ (Finger Millet)",
        "name_en": "Finger Millet (Ragi)",
        "category": "millets",
        "season_kn": "ಮುಂಗಾರು (ಜುಲೈ - ಆಗಸ್ಟ್), ನೀರಾವರಿ (ಜನವರಿ - ಫೆಬ್ರವರಿ)",
        "season_en": "Kharif (July - August), Irrigated (January - February)",
        "soil_kn": "ಕೆಂಪು ಮರಳು ಮಿಶ್ರಿತ ಮಣ್ಣು, ಜೇಡಿ ಮಿಶ್ರಿತ ಮಣ್ಣು (pH 5.5 - 7.5)",
        "soil_en": "Red sandy loam, clay loam with good drainage (pH 5.5 - 7.5)",
        "water_kn": "ಬರ ನಿರೋಧಕ ಬೆಳೆ. ಬಿತ್ತನೆ, ತೆನೆ ಒಡೆಯುವ ಮತ್ತು ಕಾಳು ಕಟ್ಟುವ ಹಂತದಲ್ಲಿ ನೀರಿನ ಅಗತ್ಯವಿದೆ.",
        "water_en": "Drought tolerant. Critical watering stages: tillering, flowering, and grain filling.",
        "fertilizer_kn": "ಪ್ರತಿ ಎಕರೆಗೆ: 4 ಟನ್ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ, 40:20:15 ಕೆಜಿ NPK. ಬಿತ್ತನೆ ವೇಳೆ ಅರ್ಧ ಸಾರಜನಕ, ಸಂಪೂರ್ಣ ರಂಜಕ ಮತ್ತು ಪೊಟ್ಯಾಷ್ ನೀಡಿ.",
        "fertilizer_en": "Per acre: 4 tons FYM, 40:20:15 kg NPK. Apply full P, K and half N at sowing; remaining N at 30 days.",
        "pests_diseases_kn": "ಬೆಂಕಿ ರೋಗ (Blast), ಕಾಂಡ ಕೊರೆಯುವ ಹುಳು. ಪರಿಹಾರ: ಬೀಜೋಪಚಾರ (ಕ್ಯಾಪ್ಟಾನ್/ಕಾರ್ಬೆಂಡಾಜಿಮ್) ಮತ್ತು ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಣೆ.",
        "pests_diseases_en": "Blast disease, stem borer. Treatment: Seed treatment with Carbendazim (2g/kg), spray Neem oil.",
        "yield_kn": "ಎಕರೆಗೆ 14 - 18 ಕ್ವಿಂಟಾಲ್ (ನೀರಾವರಿಯಲ್ಲಿ 20 - 25 ಕ್ವಿಂಟಾಲ್)",
        "yield_en": "14 - 18 quintals per acre (20 - 25 quintals under irrigation)",
        "audio_summary_kn": "ರಾಗಿ ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಪೌಷ್ಟಿಕ ಬೆಳೆ. ಜುಲೈ-ಆಗಸ್ಟ್ ತಿಂಗಳಲ್ಲಿ ಕೆಂಪು ಮರಳು ಮಣ್ಣಿನಲ್ಲಿ ಬಿತ್ತನೆ ಮಾಡಲು ಸೂಕ್ತ. ಎಕರೆಗೆ 40:20:15 NPK ಗೊಬ್ಬರ ನೀಡಿ. ಬೆಂಕಿ ರೋಗಕ್ಕೆ ಬೀಜೋಪಚಾರ ಅತ್ಯಗತ್ಯ.",
        "audio_summary_en": "Ragi is ideal for July to August sowing in red sandy soil. Use 40:20:15 NPK per acre. Blast disease is common; protect with seed treatment.",
    },
    {
        "id": "paddy",
        "name_kn": "ಭತ್ತ (Paddy / Rice)",
        "name_en": "Paddy / Rice",
        "category": "cereals",
        "season_kn": "ಖಾರಿಫ್ (ಜೂನ್ - ಜುಲೈ), ರಬಿ (ನವೆಂಬರ್ - ಡಿಸೆಂಬರ್)",
        "season_en": "Kharif (June - July), Rabi (November - December)",
        "soil_kn": "ಆಳವಾದ ಫಲವತ್ತಾದ ಜೇಡಿ ಮಣ್ಣು ಅಥವಾ ಗೋಡು ಮಣ್ಣು (pH 6.0 - 7.0)",
        "soil_en": "Clayey loam, fertile alluvial soils with high water-holding capacity (pH 6.0 - 7.0)",
        "water_kn": "ಹೆಚ್ಚು ನೀರಿನ ಅಗತ್ಯವಿದೆ. ಸಸಿ ನೆಟ್ಟ 3-4 ವಾರಗಳವರೆಗೆ 2-3 ಸೆಂ.ಮೀ ನೀರು ನಿಲ್ಲಿಸಬೇಕು.",
        "water_en": "High water demand. Maintain 2-3 cm standing water during transplanting and active tillering.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 6 ಟನ್ ಕಾಂಪೋಸ್ಟ್, 50:25:25 ಕೆಜಿ NPK. ಸತು (Zinc Sulphate) 10 ಕೆಜಿ ನೀಡುವುದು ಕಡ್ಡಾಯ.",
        "fertilizer_en": "Per acre: 6 tons FYM, 50:25:25 kg NPK. Apply 10 kg Zinc Sulphate to avoid Khaira disease.",
        "pests_diseases_kn": "ಕಂದು ಜಿಗಿಹುಳು (BPH), ಎಲೆ ಕರಕಲು, ಬೆಂಕಿ ರೋಗ. ಪರಿಹಾರ: ಟ್ರೈಸೈಕ್ಲಾಜೋಲ್ 120 ಗ್ರಾಂ ಅಥವಾ ಬೇವಿನ ಎಣ್ಣೆ 5 ಮಿ.ಲೀ/ಲೀ.",
        "pests_diseases_en": "Brown Plant Hopper (BPH), Blast, Bacterial Leaf Blight. Treatment: Tricyclazole 0.6g/L or Neem oil spray.",
        "yield_kn": "ಎಕರೆಗೆ 25 - 30 ಕ್ವಿಂಟಾಲ್",
        "yield_en": "25 - 30 quintals per acre",
        "audio_summary_kn": "ಭತ್ತಕ್ಕೆ ಜೇಡಿ ಮಣ್ಣು ಮತ್ತು ನಿರಂತರ ತೇವಾಂಶ ಅಗತ್ಯ. ಜಿಂಕ್ ಸಲ್ಫೇಟ್ ಕೊರತೆಯಾಗದಂತೆ ಎಕರೆಗೆ 10 ಕೆಜಿ ಸತುವಿನ ಗೊಬ್ಬರ ನೀಡಿ. ಬೆಂಕಿ ರೋಗಕ್ಕೆ ಟ್ರೈಸೈಕ್ಲಾಜೋಲ್ ಸಿಂಪಡಿಸಿ.",
        "audio_summary_en": "Paddy needs fertile clay soil and steady water. Apply 10 kg Zinc Sulphate per acre to prevent yellowing. For blast disease, use Tricyclazole.",
    },
    {
        "id": "maize",
        "name_kn": "ಮೆಕ್ಕೆಜೋಳ (Maize / Corn)",
        "name_en": "Maize (Corn)",
        "category": "cereals",
        "season_kn": "ಖಾರಿಫ್ (ಜೂನ್ - ಜುಲೈ), ರಬಿ (ಅಕ್ಟೋಬರ್ - ನವೆಂಬರ್)",
        "season_en": "Kharif (June - July), Rabi (October - November)",
        "soil_kn": "ಚೆನ್ನಾಗಿ ನೀರು ಬಸಿದುಹೋಗುವ ಫಲವತ್ತಾದ ಕೆಂಪು ಅಥವಾ ಕಪ್ಪು ಗೋಡು ಮಣ್ಣು (pH 6.0 - 7.5)",
        "soil_en": "Well-drained red or black loamy soils (pH 6.0 - 7.5)",
        "water_kn": "ತೆನೆ ಮೂಡುವಾಗ ಮತ್ತು ಕಾಳು ಕಟ್ಟುವ ಹಂತದಲ್ಲಿ ನೀರು ಕಡಿಮೆಯಾಗಬಾರದು. ನೀರು ನಿಲ್ಲದಂತೆ ನೋಡಿಕೊಳ್ಳಿ.",
        "water_en": "Moisture is critical during tasseling, silking, and grain filling. Avoid waterlogging.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 60:30:20 ಕೆಜಿ NPK. 30 ಮತ್ತು 45 ದಿನಗಳಲ್ಲಿ ಸಾರಜನಕ ಮೇಲುಗೊಬ್ಬರ ನೀಡಿ.",
        "fertilizer_en": "Per acre: 60:30:20 kg NPK. Top-dress Nitrogen in splits at 30 and 45 days after sowing.",
        "pests_diseases_kn": "ಸೈನಿಕ ಹುಳು (Fall Armyworm). ಪರಿಹಾರ: ಇಮಾಮೆಕ್ಟಿನ್ ಬೆಂಜೋಯೇಟ್ 0.4 ಗ್ರಾಂ/ಲೀ ಅಥವಾ ಕ್ಲೋರಾಂಟ್ರಾನಿಲಿಪ್ರೋಲ್ 0.3 ಮಿ.ಲೀ/ಲೀ ಸಿಂಪಡಿಸಿ.",
        "pests_diseases_en": "Fall Armyworm (FAW), Stem borer. Treatment: Emamectin Benzoate (0.4g/L) or Chlorantraniliprole in the leaf whorl.",
        "yield_kn": "ಎಕರೆಗೆ 30 - 35 ಕ್ವಿಂಟಾಲ್",
        "yield_en": "30 - 35 quintals per acre",
        "audio_summary_kn": "ಮೆಕ್ಕೆಜೋಳಕ್ಕೆ ಸೈನಿಕ ಹುಳು ಪ್ರಮುಖ ಬಾಧೆ. ಲಕ್ಷಣ ಕಂಡ ತಕ್ಷಣ ಸುಳಿಯೊಳಗೆ ಇಮಾಮೆಕ್ಟಿನ್ ಬೆಂಜೋಯೇಟ್ ಸಿಂಪಡಿಸಿ. 45ನೇ ದಿನಕ್ಕೆ ಸಾರಜನಕ ಮೇಲುಗೊಬ್ಬರ ನೀಡಿ.",
        "audio_summary_en": "Maize needs vigilant control for Fall Armyworm. Apply Emamectin Benzoate directly into plant whorls. Ensure top-dress Nitrogen at 45 days.",
    },
    {
        "id": "sugarcane",
        "name_kn": "ಕಬ್ಬು (Sugarcane)",
        "name_en": "Sugarcane",
        "category": "commercial",
        "season_kn": "ಜನವರಿ - ಫೆಬ್ರವರಿ (ಏಕಸಾಲಿ) ಅಥವಾ ಜುಲೈ - ಆಗಸ್ಟ್ (ಅಡ್ಸಾಲಿ)",
        "season_en": "January - February (Eksali) or July - August (Adsali)",
        "soil_kn": "ಆಳವಾದ ಕಪ್ಪು ಜೇಡಿ ಅಥವಾ ಗೋಡು ಮಣ್ಣು (pH 6.5 - 8.0)",
        "soil_en": "Deep fertile black soils or alluvial loam (pH 6.5 - 8.0)",
        "water_kn": "ಹನಿ ನೀರಾವರಿ ಅತ್ಯುತ್ತಮ. 10-12 ದಿನಗಳಿಗೊಮ್ಮೆ ನೀರು ಹಾಯಿಸಬೇಕು.",
        "water_en": "Drip irrigation recommended. Water every 8-10 days in summer and 12-15 days in winter.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 100:40:50 ಕೆಜಿ NPK. 100-120 ದಿನಗಳ ಒಳಗೆ ರಸಗೊಬ್ಬರ ಪೂರ್ಣಗೊಳಿಸಿ ಮಣ್ಣು ಏರಿಸಿ.",
        "fertilizer_en": "Per acre: 100:40:50 kg NPK in splits up to 120 days followed by earthing up.",
        "pests_diseases_kn": "ಕೆಂಪು ಕೊಳೆತ ರೋಗ (Red Rot), ಮುಂಜಾನೆಯ ಸುಳಿ ಕೊರೆಯುವ ಹುಳು. ಪರಿಹಾರ: ರೋಗಮುಕ್ತ ಬಿತ್ತನೆ ಕಬ್ಬು ಬಳಕೆ, ಟ್ರೈಕೋಗ್ರಾಮ ಪರಾವಲಂಬಿ ಜೀವಿ ಬಳಕೆ.",
        "pests_diseases_en": "Red Rot, Early shoot borer. Treatment: Disease-free setts, Trichogramma cards, Carbofuran granules.",
        "yield_kn": "ಎಕರೆಗೆ 50 - 70 ಟನ್",
        "yield_en": "50 - 70 tons per acre",
        "audio_summary_kn": "ಕಬ್ಬಿಗೆ ಹನಿ ನೀರಾವರಿ ಬಳಸುವುದರಿಂದ ಶೇಕಡಾ 40 ರಷ್ಟು ನೀರು ಮತ್ತು ಗೊಬ್ಬರ ಉಳಿತಾಯವಾಗುತ್ತದೆ. 120 ದಿನದೊಳಗೆ ರಸಗೊಬ್ಬರ ಮುಗಿಸಿ ಮಣ್ಣು ಏರಿಸಿ.",
        "audio_summary_en": "Drip irrigation saves 40% water in sugarcane. Complete all fertilizer application within 120 days and perform earthing up.",
    },
    {
        "id": "cotton",
        "name_kn": "ಹತ್ತಿ (Cotton)",
        "name_en": "Cotton",
        "category": "commercial",
        "season_kn": "ಜೂನ್ - ಜುಲೈ (ಮುಂಗಾರು ಆರಂಭ)",
        "season_en": "June - July (Onset of Kharif monsoon)",
        "soil_kn": "ಕಪ್ಪು ಹತ್ತಿ ಮಣ್ಣು (Black Cotton Soil) ಅಥವಾ ಫಲವತ್ತಾದ ಗೋಡು ಮಣ್ಣು",
        "soil_en": "Deep black cotton soil with high moisture retention (pH 6.5 - 8.5)",
        "water_kn": "ಹೂವಾಡುವ ಮತ್ತು ಕಾಯಿ ಕಟ್ಟುವ ಹಂತದಲ್ಲಿ ನೀರಿನ ಕೊರತೆಯಾಗದಂತೆ ನೋಡಿಕೊಳ್ಳಿ.",
        "water_en": "Critical irrigation stages: flowering and boll development.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 60:30:30 ಕೆಜಿ NPK. ಮೆಗ್ನೀಸಿಯಮ್ ಸಲ್ಫೇಟ್ (5 ಕೆಜಿ) ಸಿಂಪಡಿಸಿದರೆ ಕೆಂಪು ರೋಗ ತಡೆಯಬಹುದು.",
        "fertilizer_en": "Per acre: 60:30:30 kg NPK. Foliar spray 1% Magnesium Sulphate to prevent leaf reddening.",
        "pests_diseases_kn": "ಗುಲಾಬಿ ಕಾಯಿಕೊರಕ (Pink Bollworm), ರಸ ಹೀರುವ ಕೀಟಗಳು. ಪರಿಹಾರ: ಮೋಹಕ ಬಲೆ (Pheromone traps), ಬೇವಿನ ಎಣ್ಣೆ, ಅಸಿಫೇಟ್ 1.5 ಗ್ರಾಂ/ಲೀ.",
        "pests_diseases_en": "Pink Bollworm, whiteflies, thrips. Treatment: Pheromone traps (8/acre), Neem oil, Acephate 1.5g/L.",
        "yield_kn": "ಎಕರೆಗೆ 10 - 15 ಕ್ವಿಂಟಾಲ್",
        "yield_en": "10 - 15 quintals per acre",
        "audio_summary_kn": "ಹತ್ತಿಯಲ್ಲಿ ಗುಲಾಬಿ ಕಾಯಿಕೊರಕ ತಡೆಯಲು ಎಕರೆಗೆ 8 ಮೋಹಕ ಬಲೆಗಳನ್ನು ಅಳವಡಿಸಿ. ಎಲೆ ಕೆಂಪಾಗುವುದನ್ನು ತಡೆಯಲು ಮೆಗ್ನೀಸಿಯಮ್ ಸಲ್ಫೇಟ್ ಸಿಂಪಡಿಸಿ.",
        "audio_summary_en": "Install 8 pheromone traps per acre for pink bollworm in cotton. Spray magnesium sulphate if leaves turn red.",
    },
    {
        "id": "tomato",
        "name_kn": "ಟೊಮೇಟೊ (Tomato)",
        "name_en": "Tomato",
        "category": "horticulture",
        "season_kn": "ವರ್ಷವಿಡೀ ಬೆಳೆಯಬಹುದು (ಜೂನ್-ಜುಲೈ, ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್, ಜನವರಿ-ಫೆಬ್ರವರಿ)",
        "season_en": "Year-round (June-July, Oct-Nov, Jan-Feb)",
        "soil_kn": "ಉತ್ತಮ ನೀರು ಬಸಿದುಹೋಗುವ ಮರಳು ಗೋಡು ಮಣ್ಣು (pH 6.0 - 7.0)",
        "soil_en": "Well-drained sandy loam rich in organic matter (pH 6.0 - 7.0)",
        "water_kn": "ನಿಯಮಿತ ನೀರಾವರಿ ಅಗತ್ಯ. ನೀರಿನ ಏರಿಳಿತದಿಂದ ಹಣ್ಣು ಬಿರುಕು ಬಿಡುತ್ತದೆ.",
        "water_en": "Regular irrigation required. Moisture fluctuation causes fruit cracking and blossom-end rot.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 8 ಟನ್ ಗೊಬ್ಬರ, 75:50:50 ಕೆಜಿ NPK. ಕ್ಯಾಲ್ಸಿಯಂ ಮತ್ತು ಬೋರಾನ್ ಲಘು ಪೋಷಕಾಂಶ ನೀಡಿ.",
        "fertilizer_en": "Per acre: 8 tons FYM, 75:50:50 kg NPK. Add Calcium Nitrate and Boron for fruit quality.",
        "pests_diseases_kn": "ಎಲೆ ಸುರುಟು ವೈರಸ್ (Leaf Curl), ಆರಂಭಿಕ ಎಲೆ ಕರಕಲು, ಹಣ್ಣು ಕೊರೆಯುವ ಹುಳು. ಪರಿಹಾರ: ಬಿಳಿ ನೊಣ ನಿಯಂತ್ರಣಕ್ಕೆ ಹಳದಿ ಜಿಗುಟು ಬಲೆ, ಮ್ಯಾಂಕೋಜೆಬ್ 2 ಗ್ರಾಂ/ಲೀ.",
        "pests_diseases_en": "Leaf Curl Virus (transmitted by whitefly), Early Blight, Fruit borer. Treatment: Yellow sticky traps, Mancozeb 2g/L, Neem oil.",
        "yield_kn": "ಎಕರೆಗೆ 15 - 25 ಟನ್ (ಹೈಬ್ರಿಡ್ ತಳಿಗಳಲ್ಲಿ 35 ಟನ್ ವರೆಗೆ)",
        "yield_en": "15 - 25 tons per acre (up to 35 tons in hybrids)",
        "audio_summary_kn": "ಟೊಮೇಟೊದಲ್ಲಿ ಎಲೆ ಸುರುಟು ರೋಗ ಬಿಳಿ ನೊಣದಿಂದ ಹರಡುತ್ತದೆ. ಹಳದಿ ಜಿಗುಟು ಬಲೆಗಳನ್ನು ಇರಿಸಿ. ಹಣ್ಣು ಬಿರುಕು ಬಿಡದಂತೆ ನಿಯಮಿತವಾಗಿ ನೀರು ಹಾಯಿಸಿ.",
        "audio_summary_en": "Tomato leaf curl spreads via whiteflies. Set yellow sticky traps immediately. Maintain consistent watering to stop fruit cracking.",
    },
    {
        "id": "arecanut",
        "name_kn": "ಅಡಿಕೆ (Arecanut)",
        "name_en": "Arecanut",
        "category": "plantation",
        "season_kn": "ಮೇ - ಜೂನ್ ಅಥವಾ ಸೆಪ್ಟೆಂಬರ್ - ಅಕ್ಟೋಬರ್ ನಲ್ಲಿ ನಾಟಿ",
        "season_en": "Planting in May - June or September - October",
        "soil_kn": "ಆಳವಾದ ಜಂಬಿಟ್ಟಿಗೆ (Laterite) ಅಥವಾ ಕೆಂಪು ಜೇಡಿ ಮಣ್ಣು (pH 5.5 - 6.5)",
        "soil_en": "Deep laterite or red loamy soils with good drainage (pH 5.5 - 6.5)",
        "water_kn": "ಬೇಸಿಗೆಯಲ್ಲಿ 5-7 ದಿನಗಳಿಗೊಮ್ಮೆ ನೀರು ಹಾಯಿಸಬೇಕು. ಹನಿ ಅಥವಾ ತುಂತುರು ನೀರಾವರಿ ಸೂಕ್ತ.",
        "water_en": "Irrigate every 5-7 days in summer. Drip or sprinkler irrigation prevents stress.",
        "fertilizer_kn": "ಪ್ರತಿ ಗಿಡಕ್ಕೆ ವಾರ್ಷಿಕವಾಗಿ: 100:40:140 ಗ್ರಾಂ NPK ಮತ್ತು 12 ಕೆಜಿ ಹಸಿರೆಲೆ/ಕಂಪೋಸ್ಟ್ ಗೊಬ್ಬರ.",
        "fertilizer_en": "Per palm per year: 100:40:140 g NPK plus 12 kg compost/green manure in two split doses.",
        "pests_diseases_kn": "ಕೊಳೆ ರೋಗ (Kole Roga / Mahali), ಹಿಂಗಾರ ಒಣಗುವ ರೋಗ. ಪರಿಹಾರ: ಮುಂಗಾರು ಮಳೆಗೆ ಮುನ್ನ 1% ಬೋರ್ಡೋ ದ್ರಾವಣ ಸಿಂಪಡಣೆ.",
        "pests_diseases_en": "Fruit rot (Kole Roga / Mahali), Inflorescence dieback. Treatment: Spray 1% Bordeaux mixture before monsoon.",
        "yield_kn": "ಪ್ರತಿ ಮರಕ್ಕೆ ವಾರ್ಷಿಕ 2.5 - 3.5 ಕೆಜಿ ಒಣಗಿದ ಅಡಿಕೆ (ಚಾಲಿ)",
        "yield_en": "2.5 - 3.5 kg dry chali per palm per year",
        "audio_summary_kn": "ಅಡಿಕೆಯಲ್ಲಿ ಕೊಳೆ ರೋಗ ತಡೆಗಟ್ಟಲು ಮುಂಗಾರು ಮಳೆ ಆರಂಭವಾಗುವ ಮುನ್ನವೇ ಶೇಕಡಾ 1 ರ ಬೋರ್ಡೋ ದ್ರಾವಣವನ್ನು ಗೊಂಚಲುಗಳಿಗೆ ಕಡ್ಡಾಯವಾಗಿ ಸಿಂಪಡಿಸಿ.",
        "audio_summary_en": "To prevent Kole Roga in arecanut, spray 1% Bordeaux mixture on nut bunches before the heavy monsoon rains start.",
    },
    {
        "id": "groundnut",
        "name_kn": "ಶೇಂಗಾ / ಕಡಲೆಕಾಯಿ (Groundnut)",
        "name_en": "Groundnut (Peanut)",
        "category": "oilseeds",
        "season_kn": "ಖಾರಿಫ್ (ಜೂನ್ - ಜುಲೈ), ರಬಿ/ಬೇಸಿಗೆ (ನವೆಂಬರ್ - ಡಿಸೆಂಬರ್)",
        "season_en": "Kharif (June - July), Summer/Rabi (November - December)",
        "soil_kn": "ಸಡಿಲವಾದ ಮರಳು ಗೋಡು ಮಣ್ಣು (pH 6.0 - 7.5). ಸುಲಭವಾಗಿ ಕಾಯಿ ಇಳಿಯಲು ಮಣ್ಣು ಸಡಿಲವಾಗಿರಬೇಕು.",
        "soil_en": "Light sandy loam with friable texture for easy peg penetration (pH 6.0 - 7.5)",
        "water_kn": "ಹೂವಾಡುವಾಗ ಮತ್ತು ಕಾಯಿ ಕಟ್ಟುವಾಗ ನೀರು ಕೊರತೆಯಾಗಬಾರದು.",
        "water_en": "Crucial stages: flowering and pegging. Avoid heavy standing water.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 10:20:10 ಕೆಜಿ NPK. ಜಿಪ್ಸಮ್ (Gypsum) 150-200 ಕೆಜಿ ಕಡ್ಡಾಯವಾಗಿ ಕಾಯಿ ಕಟ್ಟುವಾಗ ನೀಡಿ.",
        "fertilizer_en": "Per acre: 10:20:10 kg NPK. Apply 200 kg Gypsum at peg formation for pod development.",
        "pests_diseases_kn": "ಟਿੱಕ್ಕಾ ಎಲೆ ಚುಕ್ಕೆ ರೋಗ, ಸುರುಳಿ ಪೂಚಿ. ಪರಿಹಾರ: ಕಾರ್ಬೆಂಡಾಜಿಮ್ 1 ಗ್ರಾಂ/ಲೀ ಸಿಂಪಡಣೆ.",
        "pests_diseases_en": "Tikka leaf spot, leaf miner. Treatment: Spray Carbendazim (1g/L) or Mancozeb (2g/L).",
        "yield_kn": "ಎಕರೆಗೆ 10 - 15 ಕ್ವಿಂಟಾಲ್",
        "yield_en": "10 - 15 quintals per acre",
        "audio_summary_kn": "ಶೇಂಗಾ ಬೆಳೆಗೆ ಕಾಯಿ ಕಟ್ಟುವ 40-45 ನೇ ದಿನಕ್ಕೆ ಎಕರೆಗೆ 150 ಕೆಜಿ ಜಿಪ್ಸಮ್ ಹಾಕಿ. ಇದು ಕಾಯಿ ಗಟ್ಟಿಯಾಗಲು ಮತ್ತು ಎಣ್ಣೆ ಅಂಶ ಹೆಚ್ಚಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "audio_summary_en": "Apply 150-200 kg Gypsum per acre to groundnut at 40-45 days. This provides Calcium and Sulphur for solid pod filling.",
    },
    {
        "id": "redgram",
        "name_kn": "ತೊಗರಿ (Pigeon Pea / Toor Dal)",
        "name_en": "Pigeon Pea (Red Gram)",
        "category": "pulses",
        "season_kn": "ಖಾರಿಫ್ (ಜೂನ್ - ಜುಲೈ ಆರಂಭ)",
        "season_en": "Kharif (June to early July)",
        "soil_kn": "ಆಳವಾದ ಕಪ್ಪು ಮಣ್ಣು ಅಥವಾ ಕೆಂಪು ಗೋಡು ಮಣ್ಣು (pH 6.5 - 7.5)",
        "soil_en": "Deep black soils or well-drained loam (pH 6.5 - 7.5)",
        "water_kn": "ಬರ ಸಹಿಷ್ಣು. ಹೂ ಬಿಡುವ ಮತ್ತು ಕಾಯಿ ಬೆಳೆಯುವ ಸಮಯದಲ್ಲಿ ನೀರು ಸಿಕ್ಕರೆ ಇಳುವರಿ ದುಪ್ಪಟ್ಟಾಗುತ್ತದೆ.",
        "water_en": "Deep taproot provides drought resistance. Critical watering at flowering and pod filling.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 10:20:10 ಕೆಜಿ NPK. ರೈಜೋಬಿಯಂ ಜೈವಿಕ ಗೊಬ್ಬರದ ಬೀಜೋಪಚಾರ ಅತ್ಯಗತ್ಯ.",
        "fertilizer_en": "Per acre: 10:20:10 kg NPK. Treat seeds with Rhizobium culture to fix atmospheric nitrogen.",
        "pests_diseases_kn": "ಕಾಯಿಕೊರಕ ಹುಳು (Helicoverpa), ನೆಟೆ ರೋಗ (Wilt). ಪರಿಹಾರ: ಟ್ರೈಕೋಡರ್ಮಾ ಬೀಜೋಪಚಾರ, ಕ್ಲೋರಾಂಟ್ರಾನಿಲಿಪ್ರೋಲ್ ಸಿಂಪಡಣೆ.",
        "pests_diseases_en": "Pod borer (Helicoverpa armigera), Fusarium wilt. Treatment: Trichoderma seed treatment, spray Chlorantraniliprole 0.3ml/L.",
        "yield_kn": "ಎಕರೆಗೆ 8 - 12 ಕ್ವಿಂಟಾಲ್",
        "yield_en": "8 - 12 quintals per acre",
        "audio_summary_kn": "ತೊಗರಿಯಲ್ಲಿ ಕಾಯಿಕೊರಕ ಹುಳು ಬಾರದಂತೆ ಹೂವಾಡುವ ಹಂತದಲ್ಲೇ ಮೋಹಕ ಬಲೆ ಇರಿಸಿ ಮತ್ತು ಬೇವಿನ ಕಷಾಯ ಸಿಂಪಡಿಸಿ. ನೆಟೆ ರೋಗಕ್ಕೆ ಟ್ರೈಕೋಡರ್ಮಾ ಬಳಸಿ.",
        "audio_summary_en": "Control pod borer in red gram during early flowering using pheromone traps and neem spray. Use Trichoderma against wilt.",
    },
    {
        "id": "chilli",
        "name_kn": "ಮೆಣಸಿನಕಾಯಿ (Green Chilli)",
        "name_en": "Green Chilli",
        "category": "horticulture",
        "season_kn": "ಜೂನ್ - ಜುಲೈ ಅಥವಾ ಅಕ್ಟೋಬರ್ - ನವೆಂಬರ್",
        "season_en": "June - July or October - November",
        "soil_kn": "ಉತ್ತಮ ನೀರು ಬಸಿದುಹೋಗುವ ಫಲವತ್ತಾದ ಕಪ್ಪು ಅಥವಾ ಕೆಂಪು ಗೋಡು ಮಣ್ಣು (pH 6.5 - 7.5)",
        "soil_en": "Well-drained fertile loam or black soil rich in humus (pH 6.5 - 7.5)",
        "water_kn": "ಹದವಾದ ನೀರಾವರಿ. ನೀರು ನಿಂತರೆ ಬೇರು ಕೊಳೆತು ಗಿಡ ಒಣಗುತ್ತದೆ.",
        "water_en": "Moderate regular moisture. Avoid water stagnation to prevent root damping.",
        "fertilizer_kn": "ಎಕರೆಗೆ: 6 ಟನ್ ಗೊಬ್ಬರ, 40:20:20 ಕೆಜಿ NPK. ಲಘು ಪೋಷಕಾಂಶಗಳ ಸಿಂಪಡಣೆ.",
        "fertilizer_en": "Per acre: 6 tons FYM, 40:20:20 kg NPK with micronutrient sprays.",
        "pests_diseases_kn": "ನುಸಿ ರೋಗ (Thrips & Mites), ಬೂದಿ ರೋಗ. ಪರಿಹಾರ: ನೀಲಿ ಮತ್ತು ಹಳದಿ ಜಿಗುಟು ಬಲೆ, ಡೈಫೆಂಥಿಯುರಾನ್ 1 ಗ್ರಾಂ/ಲೀ ಅಥವಾ ಗಂಧಕ 2 ಗ್ರಾಂ/ಲೀ.",
        "pests_diseases_en": "Thrips, mites, powdery mildew. Treatment: Blue/yellow sticky traps, Diafenthiuron (1g/L), Wettable Sulphur (2g/L).",
        "yield_kn": "ಎಕರೆಗೆ ಹಸಿಮೆಣಸು 60 - 80 ಕ್ವಿಂಟಾಲ್ (ಒಣ ಮೆಣಸು 10 - 15 ಕ್ವಿಂಟಾಲ್)",
        "yield_en": "Green chilli: 60 - 80 quintals per acre (Dry: 10 - 15 quintals)",
        "audio_summary_kn": "ಮೆಣಸಿನಕಾಯಿಯಲ್ಲಿ ಎಲೆ ಮುದುಡುವ ನುಸಿ ರೋಗ ತಡೆಯಲು ನೀಲಿ ಮತ್ತು ಹಳದಿ ಬಲೆಗಳನ್ನು ಹಾಕಿ. ಗಂಧಕದ ಪುಡಿ ಸಿಂಪಡಿಸುವುದರಿಂದ ಬೂದಿ ರೋಗ ಹತೋಟಿಗೆ ಬರುತ್ತದೆ.",
        "audio_summary_en": "Install blue and yellow sticky traps to control thrips in chilli. Spray wettable sulphur for powdery mildew control.",
    }
]

# ==========================================
# 2. DISEASE SOLUTIONS DIRECTORY
# ==========================================
DISEASES_DATA = [
    {
        "id": "tomato_leaf_curl",
        "crop": "Tomato / ಟೊಮೇಟೊ",
        "disease_kn": "ಎಲೆ ಸುರುಟು ರೋಗ (Leaf Curl Virus)",
        "disease_en": "Tomato Leaf Curl Virus (ToLCV)",
        "symptoms_kn": "ಎಲೆಗಳು ಮೇಲ್ಮುಖವಾಗಿ ಸುರುಟಿಕೊಳ್ಳುತ್ತವೆ, ಗಿಡದ ಬೆಳವಣಿಗೆ ಕುಂಠಿತವಾಗುತ್ತದೆ, ಎಲೆಗಳು ಸಣ್ಣದಾಗಿ ದಪ್ಪವಾಗುತ್ತವೆ.",
        "symptoms_en": "Upward curling and puckering of leaves, stunted plant growth, thickened leathery leaves.",
        "cause_kn": "ಬಿಳಿ ನೊಣ (Whitefly - Bemisia tabaci) ಈ ವೈರಸ್ ರೋಗವನ್ನು ಗಿಡದಿಂದ ಗಿಡಕ್ಕೆ ಹರಡುತ್ತದೆ.",
        "cause_en": "Transmitted by whiteflies (Bemisia tabaci).",
        "organic_remedy_kn": "ಎಕರೆಗೆ 15-20 ಹಳದಿ ಜಿಗುಟು ಬಲೆಗಳನ್ನು (Yellow sticky traps) ಅಳವಡಿಸಿ. 5 ಮಿ.ಲೀ ಬೇವಿನ ಎಣ್ಣೆ (10,000 ppm) ಪ್ರತಿ ಲೀಟರ್ ನೀರಿಗೆ ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿ.",
        "organic_remedy_en": "Install 15-20 yellow sticky traps per acre. Spray 5 ml neem oil (10,000 ppm) per liter water.",
        "chemical_remedy_kn": "ಬಿಳಿ ನೊಣ ನಿಯಂತ್ರಣಕ್ಕೆ: ಅಸಿಟಾಮಿಪ್ರಿಡ್ 0.5 ಗ್ರಾಂ/ಲೀ ಅಥವಾ ಥಯಾಮಿಥಾಕ್ಸಾಮ್ 0.3 ಗ್ರಾಂ/ಲೀ ಅಥವಾ ಡಯಾಫೆಂಥಿಯುರಾನ್ 1 ಗ್ರಾಂ/ಲೀ ಸಿಂಪಡಿಸಿ.",
        "chemical_remedy_en": "For whitefly vector control: Acetamiprid 0.5g/L or Thiamethoxam 0.3g/L or Diafenthiuron 1g/L.",
        "prevention_kn": "ಬೀಜ ಬಿತ್ತನೆ ಮಾಡುವಾಗ ನೈಲಾನ್ ನೆಟ್ ನರ್ಸರಿ ಬಳಸಿ. ಸೋಂಕಿತ ಗಿಡಗಳನ್ನು ಬೇರು ಸಮೇತ ಕಿತ್ತು ನಾಶಪಡಿಸಿ.",
        "prevention_en": "Raise seedlings under 40-mesh nylon nets. Uproot and burn infected plants early.",
        "audio_kn": "ಟೊಮೇಟೊ ಎಲೆ ಸುರುಟು ರೋಗವು ಬಿಳಿ ನೊಣದಿಂದ ಹರಡುತ್ತದೆ. ತಕ್ಷಣ ಹಳದಿ ಬಲೆಗಳನ್ನು ಅಳವಡಿಸಿ. ಬಿಳಿ ನೊಣ ನಿಯಂತ್ರಣಕ್ಕೆ ಅಸಿಟಾಮಿಪ್ರಿಡ್ ಅಥವಾ ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ."
    },
    {
        "id": "paddy_blast",
        "crop": "Paddy / ಭತ್ತ",
        "disease_kn": "ಬೆಂಕಿ ರೋಗ (Blast Disease)",
        "disease_en": "Paddy Blast (Magnaporthe oryzae)",
        "symptoms_kn": "ಎಲೆಗಳ ಮೇಲೆ ಕಣ್ಣಿನ ಆಕಾರದ (ಸ್ಪಿಂಡಲ್) ಕಂದು ಬಣ್ಣದ ಚುಕ್ಕೆಗಳು, ಕೊರಳ ಭಾಗ ಕಪ್ಪಾಗಿ ತೆನೆಗಳು ಮುರಿದು ಬೀಳುವುದು (ನೆಕ್ ಬ್ಲಾಸ್ಟ್).",
        "symptoms_en": "Spindle-shaped brown spots with grey centers on leaves; black lesions at neck node causing panicles to break.",
        "cause_kn": "ಮ್ಯಾಗ್ನಾಪೋರ್ತೆ ಒರೈಜೆ ಎಂಬ ಶಿಲೀಂಧ್ರ. ತೇವಾಂಶ ಮತ್ತು ಮೋಡ ಕವಿದ ವಾತಾವರಣದಲ್ಲಿ ವೇಗವಾಗಿ ಹರಡುತ್ತದೆ.",
        "cause_en": "Fungal pathogen Magnaporthe oryzae under high humidity, drizzle, and overcast skies.",
        "organic_remedy_kn": "ಸೂಡೋಮೊನಾಸ್ ಫ್ಲೋರೆಸೆನ್ಸ್ 5 ಗ್ರಾಂ/ಲೀ ಅಥವಾ ಬೇವಿನ ಕಷಾಯ 5% ಸಿಂಪಡಿಸಿ. ಸಾರಜನಕ ರಸಗೊಬ್ಬರವನ್ನು ಅತಿಯಾಗಿ ಬಳಸಬೇಡಿ.",
        "organic_remedy_en": "Foliar spray Pseudomonas fluorescens (5g/L) or 5% neem seed kernel extract. Avoid excess nitrogen.",
        "chemical_remedy_kn": "ಟ್ರೈಸೈಕ್ಲಾಜೋಲ್ (Tricyclazole 75% WP) 0.6 ಗ್ರಾಂ ಪ್ರತಿ ಲೀಟರ್ ನೀರಿಗೆ ಅಥವಾ ಐಸೊಪ್ರೊಥಿಯೋಲೇನ್ 1.5 ಮಿ.ಲೀ/ಲೀ ಸಿಂಪಡಿಸಿ.",
        "chemical_remedy_en": "Spray Tricyclazole 75% WP at 0.6g/L or Isoprothiolane at 1.5ml/L at first symptom.",
        "prevention_kn": "ಬೀಜೋಪಚಾರ: ಕಾರ್ಬೆಂಡಾಜಿಮ್ 2 ಗ್ರಾಂ ಪ್ರತಿ ಕೆಜಿ ಬೀಜಕ್ಕೆ ಬಳಸಿ.",
        "prevention_en": "Seed treatment with Carbendazim (2g/kg seed). Maintain balanced potassium fertilisation.",
        "audio_kn": "ಭತ್ತದ ಬೆಂಕಿ ರೋಗಕ್ಕೆ ಟ್ರೈಸೈಕ್ಲಾಜೋಲ್ 0.6 ಗ್ರಾಂ ಪ್ರತಿ ಲೀಟರ್ ನೀರಿಗೆ ಬೆರೆಸಿ ಸಿಂಪಡಿಸಿ. ಸಾರಜನಕ ಯೂರಿಯಾ ರಸಗೊಬ್ಬರವನ್ನು ಅತಿಯಾಗಿ ಹಾಕಬೇಡಿ."
    },
    {
        "id": "maize_fall_armyworm",
        "crop": "Maize / ಮೆಕ್ಕೆಜೋಳ",
        "disease_kn": "ಸೈನಿಕ ಹುಳು / ಲದ್ದಿ ಹುಳು (Fall Armyworm)",
        "disease_en": "Fall Armyworm (Spodoptera frugiperda)",
        "symptoms_kn": "ಎಲೆಗಳಲ್ಲಿ ರಂಧ್ರಗಳು, ಸುಳಿಯೊಳಗೆ ಹಿಕ್ಕೆ (ಲದ್ದಿ) ತುಂಬಿರುವುದು, ಎಲೆಗಳನ್ನು ತಿಂದಂತೆ ಜರಡಿಯಾಗುವುದು.",
        "symptoms_en": "Shot-holes in leaves, heavy sawdust-like frass inside whorls, ragged skeletonized leaves.",
        "cause_kn": "ಸ್ಪೊಡಾಪ್ಟೆರಾ ಫ್ರುಗಿಪೆರ್ಡಾ ಪತಂಗದ ಮರಿಹುಳುಗಳು. ರಾತ್ರಿ ವೇಳೆ ವೇಗವಾಗಿ ಗಿಡಗಳನ್ನು ತಿನ್ನುತ್ತವೆ.",
        "cause_en": "Larvae of Spodoptera frugiperda moth feeding inside the whorl.",
        "organic_remedy_kn": "ಸುಳಿಯೊಳಗೆ ಮರಳು ಮತ್ತು ಬೂದಿಯ ಮಿಶ್ರಣ (9:1 ಪ್ರಮಾಣ) ಹಾಕಿ. ಬೇವಿನ ಎಣ್ಣೆ 5 ಮಿ.ಲೀ/ಲೀ ಅಥವಾ ಬ್ಯಾವೆರಿಯಾ ಬಾಸ್ಸಿಯಾನಾ 5 ಗ್ರಾಂ/ಲೀ ಸಿಂಪಡಿಸಿ.",
        "organic_remedy_en": "Drop dry sand + wood ash mixture (9:1) into whorls. Spray Beauveria bassiana (5g/L) or neem oil.",
        "chemical_remedy_kn": "ಎಮಮೆಕ್ಟಿನ್ ಬೆಂಜೋಯೇಟ್ (Emamectin Benzoate 5% SG) 0.4 ಗ್ರಾಂ/ಲೀ ಅಥವಾ ಕ್ಲೋರಾಂಟ್ರಾನಿಲಿಪ್ರೋಲ್ (Coragen) 0.4 ಮಿ.ಲೀ/ಲೀ ಸುಳಿಯೊಳಗೆ ನೇರವಾಗಿ ಸಿಂಪಡಿಸಿ.",
        "chemical_remedy_en": "Direct spray into leaf whorl with Emamectin Benzoate 5% SG (0.4g/L) or Chlorantraniliprole 18.5% SC (0.4ml/L).",
        "prevention_kn": "ಬೆಳೆ ಬಿತ್ತಿದ 15 ದಿನಕ್ಕೆ ಎಕರೆಗೆ 5 ಮೋಹಕ ಬಲೆ (Pheromone traps) ಇರಿಸಿ. ಮಿಶ್ರ ಬೆಳೆಯಾಗಿ ಅಲಸಂದಿ ಬೆಳೆಯಿರಿ.",
        "prevention_en": "Install 5 pheromone traps per acre at 15 days. Intercrop with cowpea to encourage predators.",
        "audio_kn": "ಮೆಕ್ಕೆಜೋಳದ ಸುಳಿಯೊಳಗೆ ಮರಳು-ಬೂದಿ ಹಾಕಿ ಅಥವಾ ಎಮಮೆಕ್ಟಿನ್ ಬೆಂಜೋಯೇಟ್ 0.4 ಗ್ರಾಂ ಪ್ರತಿ ಲೀಟರ್ ನೀರಿಗೆ ಬೆರೆಸಿ ಸುಳಿಗೆ ಸಿಂಪಡಿಸಿ."
    },
    {
        "id": "sugarcane_red_rot",
        "crop": "Sugarcane / ಕಬ್ಬು",
        "disease_kn": "ಕೆಂಪು ಕೊಳೆತ ರೋಗ (Red Rot)",
        "disease_en": "Sugarcane Red Rot (Colletotrichum falcatum)",
        "symptoms_kn": "ಮೇಲಿನ ಎಲೆಗಳು ಹಳದಿಯಾಗಿ ಒಣಗುತ್ತವೆ. ಕಬ್ಬನ್ನು ಸೀಳಿದಾಗ ಒಳಭಾಗ ಕೆಂಪಾಗಿ ಬಿಳಿ ಪಟ್ಟಿಗಳು ಕಾಣಿಸುತ್ತವೆ ಮತ್ತು ಮದ್ಯದ ವಾಸನೆ ಬರುತ್ತದೆ.",
        "symptoms_en": "Third and fourth leaves turn yellow and dry; split canes show red internal tissues with crosswise white patches and alcoholic odour.",
        "cause_kn": "ಕೊಲೆಟೊಟ್ರೈಕಮ್ ಫಾಲ್ಕೇಟಮ್ ಶಿಲೀಂಧ್ರ. ಸೋಂಕಿತ ಬಿತ್ತನೆ ಕಬ್ಬು ಮತ್ತು ನೀರಿನ ಮೂಲಕ ಹರಡುತ್ತದೆ.",
        "cause_en": "Fungal infection via infected setts and irrigation runoff.",
        "organic_remedy_kn": "ಟ್ರೈಕೋಡರ್ಮಾ ಹರ್ಜಿಯಾನಮ್ 2.5 ಕೆಜಿ ಪ್ರತಿ ಎಕರೆಗೆ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರದೊಂದಿಗೆ ಬೆರೆಸಿ ಮಣ್ಣಿಗೆ ನೀಡಿ.",
        "organic_remedy_en": "Apply Trichoderma harzianum (2.5 kg/acre) mixed with FYM at planting.",
        "chemical_remedy_kn": "ಬಿತ್ತನೆ ತುಂಡುಗಳನ್ನು ಕಾರ್ಬೆಂಡಾಜಿಮ್ 1 ಗ್ರಾಂ/ಲೀ ದ್ರಾವಣದಲ್ಲಿ 15 ನಿಮಿಷ ಅದ್ದಿ ನಾಟಿ ಮಾಡಿ.",
        "chemical_remedy_en": "Sett treatment with Carbendazim (1g/L) for 15 minutes before planting.",
        "prevention_kn": "ರೋಗ ನಿರೋಧಕ ತಳಿಗಳಾದ Co 86032, Co 0238 ಬೆಳೆಯಿರಿ. ರೋಗ ಪೀಡಿತ ಜಮೀನಿನಲ್ಲಿ ಬೆಳೆ ಪರಿವರ್ತನೆ ಮಾಡಿ.",
        "prevention_en": "Plant resistant varieties like Co 86032. Practice crop rotation with paddy or pulses.",
        "audio_kn": "ಕಬ್ಬಿನ ಕೆಂಪು ಕೊಳೆತ ರೋಗ ತಡೆಗಟ್ಟಲು ರೋಗಮುಕ್ತ ಬಿತ್ತನೆ ಕಬ್ಬು ಬಳಸಿ ಮತ್ತು ನಾಟಿ ಮಾಡುವ ಮುನ್ನ ಕಾರ್ಬೆಂಡಾಜಿಮ್ ದ್ರಾವಣದಲ್ಲಿ ಅದ್ದಿ ಬಿತ್ತನೆ ಮಾಡಿ."
    },
    {
        "id": "cotton_pink_bollworm",
        "crop": "Cotton / ಹತ್ತಿ",
        "disease_kn": "ಗುಲಾಬಿ ಕಾಯಿಕೊರಕ ಹುಳು (Pink Bollworm)",
        "disease_en": "Pink Bollworm (Pectinophora gossypiella)",
        "symptoms_kn": "ಹೂವುಗಳು ಗುಲಾಬಿ ಆಕಾರದಲ್ಲಿ ಮುದುಡಿಕೊಳ್ಳುತ್ತವೆ (ರೊಸೆಟ್ ಹೂವುಗಳು), ಕಾಯಿಗಳ ಮೇಲೆ ಸಣ್ಣ ರಂಧ್ರಗಳು ಮತ್ತು ಲಿಂಟ್ ಕಪ್ಪಾಗುವುದು.",
        "symptoms_en": "Rosetted flowers that fail to open, premature boll dropping, boreholes with stained lint.",
        "cause_kn": "ಪೆಕ್ಟಿನೋಫೊರಾ ಗಾಸ್ಸಿಪಿಯೆಲ್ಲಾ ಹುಳು ಕಾಯಿಯೊಳಗೆ ಬೀಜಗಳನ್ನು ತಿನ್ನುತ್ತದೆ.",
        "cause_en": "Pectinophora gossypiella larvae feeding inside bolls.",
        "organic_remedy_kn": "ಎಕರೆಗೆ 8-10 ಮೋಹಕ ಬಲೆ (Pheromone traps) ಇರಿಸಿ. ಟ್ರೈಕೋಗ್ರಾಮಾ ಪರಾವಲಂಬಿ ಮೊಟ್ಟೆ ಕಾರ್ಡ್‌ಗಳನ್ನು (ಎಕರೆಗೆ 3) ಬಿಡಿ.",
        "organic_remedy_en": "Install 8-10 pheromone traps per acre. Release Trichogramma parasitoid cards (3 cards/acre).",
        "chemical_remedy_kn": "ಪ್ರೊಫೆನೋಫಾಸ್ 2 ಮಿ.ಲೀ/ಲೀ ಅಥವಾ ಸ್ಪಿನೊಸ್ಯಾಡ್ 0.4 ಮಿ.ಲೀ/ಲೀ ನೀರಿಗೆ ಬೆರೆಸಿ ಸಂಜೆ ವೇಳೆ ಸಿಂಪಡಿಸಿ.",
        "chemical_remedy_en": "Spray Profenophos 50% EC at 2ml/L or Spinosad 45% SC at 0.4ml/L during evening hours.",
        "prevention_kn": "ಬೆಳೆ ಅವಶೇಷಗಳನ್ನು ಸುಡದೆ ಮಣ್ಣಿಗೆ ಸೇರಿಸಿ ಅಥವಾ ನಾಶಪಡಿಸಿ. ದೀರ್ಘಕಾಲದ ತಳಿಗಳ ಬದಲು ಅಲ್ಪಾವಧಿ ತಳಿ ಬೆಳೆಯಿರಿ.",
        "prevention_en": "Avoid ratoon cotton crop. Destroy crop residues and observe timely terminal picking.",
        "audio_kn": "ಹತ್ತಿಯಲ್ಲಿ ಗುಲಾಬಿ ಕಾಯಿಕೊರಕ ನಿಯಂತ್ರಣಕ್ಕೆ ಎಕರೆಗೆ 8 ಮೋಹಕ ಬಲೆಗಳನ್ನು ಅಳವಡಿಸಿ. ತೀವ್ರ ಬಾಧೆಗೆ ಪ್ರೊಫೆನೋಫಾಸ್ ಅಥವಾ ಸ್ಪಿನೊಸ್ಯಾಡ್ ಸಿಂಪಡಿಸಿ."
    }
]

# ==========================================
# 3. GOVERNMENT SCHEMES DIRECTORY
# ==========================================
SCHEMES_DATA = [
    {
        "id": "pm_kisan",
        "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ (PM-Kisan)",
        "name_en": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
        "benefit_kn": "ವರ್ಷಕ್ಕೆ ₹6,000 ನೇರ ಆರ್ಥಿಕ ನೆರವು (ಪ್ರತಿ 4 ತಿಂಗಳಿಗೊಮ್ಮೆ ₹2,000 ಮೂರು ಕಂತುಗಳಲ್ಲಿ ರೈತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ನೇರವಾಗಿ ಜಮೆಯಾಗುತ್ತದೆ).",
        "benefit_en": "Direct income support of ₹6,000 per year in three equal instalments of ₹2,000 into Aadhaar-seeded bank account.",
        "eligibility_kn": "ಸ್ವಂತ ಜಮೀನು ಹೊಂದಿರುವ ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತ ಕುಟುಂಬಗಳು. ಇ-ಕೆವೈಸಿ (e-KYC) ಕಡ್ಡಾಯ.",
        "eligibility_en": "Landholder farmer families with cultivable landholding. e-KYC and land seeding mandatory.",
        "documents_kn": "ಆಧಾರ್ ಕಾರ್ಡ್, ಪಹಣಿ/ಆರ್‌ಟಿಸಿ (RTC), ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಮತ್ತು ಮೊಬೈಲ್ ಸಂಖ್ಯೆ.",
        "documents_en": "Aadhaar Card, Land RTC / Pahani records, bank passbook, and linked mobile number.",
        "apply_kn": "pmkisan.gov.in ವೆಬ್‌ಸೈಟ್ ಅಥವಾ ಗ್ರಾಮ ಒನ್ / ಬಾಪೂಜಿ ಸೇವಾ ಕೇಂದ್ರದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ. ಸಹಾಯವಾಣಿ: 155261.",
        "apply_en": "Apply via pmkisan.gov.in portal, CSC, or Grama One center. Helpline: 155261 / 1800-115-526.",
        "audio_kn": "ಪಿಎಂ ಕಿಸಾನ್ ಯೋಜನೆಯಡಿ ರೈತರಿಗೆ ವಾರ್ಷಿಕ 6,000 ರೂಪಾಯಿ ನೇರ ಸಹಾಯಧನ ದೊರೆಯುತ್ತದೆ. ಹಣ ಪಡೆಯಲು ನಿಮ್ಮ ಆಧಾರ್ ಇ-ಕೆವೈಸಿ ಮಾಡಿಸಿರಬೇಕು. ಸಹಾಯವಾಣಿ 155261."
    },
    {
        "id": "raitha_siri",
        "name_kn": "ರೈತ ಸಿರಿ ಯೋಜನೆ (ಕರ್ನಾಟಕ - Raitha Siri)",
        "name_en": "Raitha Siri Scheme (Karnataka Millet Mission)",
        "benefit_kn": "ಸಿರಿಧಾನ್ಯಗಳನ್ನು (ರಾಗಿ, ನವಣೆ, ಕೊರಲೆ, ಹಾರಕ, ಸಾಮೆ, ಬರಗು) ಬೆಳೆಯುವ ರೈತರಿಗೆ ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ ₹10,000 ಪ್ರೋತ್ಸಾಹಧನ ನೇರ ಖಾತೆಗೆ ಜಮೆ.",
        "benefit_en": "Incentive of ₹10,000 per hectare (up to 2 hectares, max ₹20,000) for farmers cultivating minor millets.",
        "eligibility_kn": "ಕರ್ನಾಟಕದ ರೈತರು ಸಿರಿಧಾನ್ಯಗಳನ್ನು ತಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ಬೆಳೆದಿರಬೇಕು ಮತ್ತು ಬೆಳೆ ಸಮೀಕ್ಷೆಯಲ್ಲಿ (Bele Sameekshe) ನಮೂದಾಗಿರಬೇಕು.",
        "eligibility_en": "Karnataka farmers registered under FRUITS ID cultivating certified millet crops.",
        "documents_kn": "ಫ್ರೂಟ್ಸ್ ಐಡಿ (FRUITS ID), ಪಹಣಿ (RTC), ಆಧಾರ್ ಕಾರ್ಡ್, ಬ್ಯಾಂಕ್ ವಿವರ.",
        "documents_en": "FRUITS ID, Land RTC record, Aadhaar card, bank account linked to NPCI.",
        "apply_kn": "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK) ಅಥವಾ fruits.karnataka.gov.in ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನೋಂದಾಯಿಸಿ.",
        "apply_en": "Register through local Raitha Samparka Kendra (RSK) or fruits.karnataka.gov.in portal.",
        "audio_kn": "ರೈತ ಸಿರಿ ಯೋಜನೆಯಲ್ಲಿ ಸಿರಿಧಾನ್ಯ ಬೆಳೆಯುವ ರೈತರಿಗೆ ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ 10,000 ರೂಪಾಯಿ ಪ್ರೋತ್ಸಾಹಧನ ನೀಡಲಾಗುತ್ತದೆ. ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಸಂಪರ್ಕಿಸಿ."
    },
    {
        "id": "krishi_bhagya",
        "name_kn": "ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆ (Krishi Bhagya Scheme)",
        "name_en": "Krishi Bhagya Scheme (Rainfed Agriculture Support)",
        "benefit_kn": "ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಾಣ (Farm Pond), ಪಾಲಿಥಿನ್ ಹೊದಿಕೆ, ಡೀಸೆಲ್ ಪಂಪ್‌ಸೆಟ್ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿ ಘಟಕಗಳಿಗೆ ಶೇಕಡಾ 80 ರಿಂದ 90 ರಷ್ಟು ಸಹಾಯಧನ.",
        "benefit_en": "80% to 90% subsidy for constructing farm ponds (Krishi Honda), polythene lining, diesel pumpsets, and sprinkler/drip units.",
        "eligibility_kn": "ಕರ್ನಾಟಕದ ಮಳೆಯಾಶ್ರಿತ ಪ್ರದೇಶಗಳ ರೈತರು. ಪರಿಶಿಷ್ಟ ಜಾತಿ/ಪಂಗಡದ ರೈತರಿಗೆ ಶೇ. 90, ಇತರ ರೈತರಿಗೆ ಶೇ. 80 ಸಹಾಯಧನ.",
        "eligibility_en": "Farmers in dryland/rainfed taluks of Karnataka. 90% subsidy for SC/ST farmers, 80% for general farmers.",
        "documents_kn": "ಪಹಣಿ, ಆಧಾರ್ ಕಾರ್ಡ್, ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್, ಜಾತಿ ಪ್ರಮಾಣಪತ್ರ (ಅನ್ವಯಿಸಿದರೆ).",
        "documents_en": "RTC land records, Aadhaar, bank passbook, caste certificate (if applicable).",
        "apply_kn": "ತಾಲ್ಲೂಕು ಕೃಷಿ ಇಲಾಖೆ ಕಚೇರಿ ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
        "apply_en": "Apply at the local Taluk Agriculture Department office or Raitha Samparka Kendra.",
        "audio_kn": "ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆಯಡಿ ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಾಣ ಮತ್ತು ಪಂಪ್‌ಸೆಟ್‌ಗೆ ಶೇಕಡಾ 80 ರಿಂದ 90 ರಷ್ಟು ಸಹಾಯಧನ ಸಿಗುತ್ತದೆ. ನಿಮ್ಮ ತಾಲ್ಲೂಕು ಕೃಷಿ ಇಲಾಖೆಯಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ."
    },
    {
        "id": "pmfby",
        "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆ (ಬೆಳೆ ವಿಮೆ - PMFBY)",
        "name_en": "Pradhan Mantri Fasal Bima Yojana (Crop Insurance)",
        "benefit_kn": "ಬರ, ಅತಿವೃಷ್ಟಿ, ಕೀಟಬಾಧೆ ಅಥವಾ ನೈಸರ್ಗಿಕ ವಿಕೋಪಗಳಿಂದ ಬೆಳೆ ನಷ್ಟವಾದರೆ ಗರಿಷ್ಠ ಪರಿಹಾರ. ಅತ್ಯಂತ ಕಡಿಮೆ ಪ್ರೀಮಿಯಂ: ಖಾರಿಫ್‌ಗೆ ಶೇ. 2, ರಬಿಗೆ ಶೇ. 1.5, ತೋಟಗಾರಿಕೆಗೆ ಶೇ. 5.",
        "benefit_en": "Comprehensive risk insurance for crop loss due to drought, floods, hailstorms, pests. Low premium: 2% for Kharif, 1.5% for Rabi, 5% for horticultural crops.",
        "eligibility_kn": "ಅಧಿಸೂಚಿತ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಯುವ ಎಲ್ಲಾ ರೈತರು (ಸಾಲಗಾರ ಮತ್ತು ಸಾಲಗಾರರಲ್ಲದ ರೈತರು).",
        "eligibility_en": "All farmers growing notified crops in notified areas.",
        "documents_kn": "ಪಹಣಿ, ಆಧಾರ್, ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್, ಬೆಳೆ ಬಿತ್ತನೆ ದೃಢೀಕರಣ ಪತ್ರ.",
        "documents_en": "RTC record, Aadhaar, bank passbook, sowing certificate from revenue inspector or self-declaration.",
        "apply_kn": "pmfby.gov.in ಅಥವಾ ಬ್ಯಾಂಕ್ ಶಾಖೆ, ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರಗಳಲ್ಲಿ ಕಟ್‌ಆಫ್ ದಿನಾಂಕದ ಒಳಗೆ ಪ್ರೀಮಿಯಂ ಪಾವತಿಸಿ. ಟೋಲ್-ಫ್ರೀ: 1800-180-1551.",
        "apply_en": "Enroll via pmfby.gov.in, commercial banks, or Grama One before seasonal cutoff dates. Helpline: 1800-180-1551.",
        "audio_kn": "ಬೆಳೆ ವಿಮೆ ಯೋಜನೆಯಿಂದ ಬರ ಅಥವಾ ಅತಿವೃಷ್ಟಿಯ ನಷ್ಟಕ್ಕೆ ಸಂಪೂರ್ಣ ಪರಿಹಾರ ಸಿಗುತ್ತದೆ. ಕೇವಲ ಶೇಕಡಾ 2 ಪ್ರೀಮಿಯಂ ಕಟ್ಟಿ ನಿಮ್ಮ ಬೆಳೆಯನ್ನು ವಿಮೆ ಮಾಡಿಸಿ."
    },
    {
        "id": "yashaswini",
        "name_kn": "ಯಶಸ್ವಿನಿ ಗ್ರಾಮೀಣ ಆರೋಗ್ಯ ಯೋಜನೆ (Yashaswini Health Scheme)",
        "name_en": "Yashaswini Cooperative Farmers Health Scheme",
        "benefit_kn": "ರೈತ ಕುಟುಂಬಗಳಿಗೆ ನಗದು ರಹಿತ ಶಸ್ತ್ರಚಿಕಿತ್ಸೆ ಮತ್ತು ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸೆ (ವಾರ್ಷಿಕ ₹5 ಲಕ್ಷದವರೆಗೆ ಚಿಕಿತ್ಸಾ ವೆಚ್ಚ ಸರ್ಕಾರ ಭರಿಸುತ್ತದೆ).",
        "benefit_en": "Cashless surgical and major healthcare coverage up to ₹5 Lakhs per family per year across network hospitals.",
        "eligibility_kn": "ಕರ್ನಾಟಕದ ಗ್ರಾಮೀಣ ಸಹಕಾರಿ ಸಂಘಗಳ ಸದಸ್ಯರು ಮತ್ತು ಅವರ ಅವಲಂಬಿತ ಕುಟುಂಬಸ್ಥರು.",
        "eligibility_en": "Members of rural cooperative societies in Karnataka and their dependents.",
        "documents_kn": "ಸಹಕಾರಿ ಸಂಘದ ಸದಸ್ಯತ್ವ ಗುರುತಿನ ಚೀಟಿ, ಪಡಿತರ ಚೀಟಿ (ರೇಷನ್ ಕಾರ್ಡ್), ಆಧಾರ್ ಕಾರ್ಡ್.",
        "documents_en": "Cooperative society membership passbook/ID, Ration Card, Aadhaar.",
        "apply_kn": "ನಿಮ್ಮ ಗ್ರಾಮದ ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರಿ ಸಂಘದಲ್ಲಿ (PKPS) ನೋಂದಾಯಿಸಿ ಯಶಸ್ವಿನಿ ಕಾರ್ಡ್ ಪಡೆಯಿರಿ.",
        "apply_en": "Apply at the local Primary Agricultural Credit Cooperative Society (PKPS).",
        "audio_kn": "ಯಶಸ್ವಿನಿ ಯೋಜನೆಯಡಿ ಸಹಕಾರಿ ಸಂಘದ ರೈತರಿಗೆ ವಾರ್ಷಿಕ 5 ಲಕ್ಷ ರೂಪಾಯಿವರೆಗೆ ಉಚಿತ ಆಸ್ಪತ್ರೆ ಚಿಕಿತ್ಸೆ ದೊರೆಯುತ್ತದೆ. ನಿಮ್ಮ ಸಹಕಾರಿ ಬ್ಯಾಂಕಿನಲ್ಲಿ ಕಾರ್ಡ್ ಪಡೆಯಿರಿ."
    },
    {
        "id": "pm_kusum",
        "name_kn": "ಪಿಎಂ ಕುಸುಮ್ ಸೋಲಾರ್ ಪಂಪ್ ಯೋಜನೆ (PM-KUSUM)",
        "name_en": "PM-KUSUM Solar Water Pump Scheme",
        "benefit_kn": "ಸೋಲಾರ್ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ ಅಳವಡಿಕೆಗೆ ಶೇಕಡಾ 80 ರವರೆಗೆ ಸಹಾಯಧನ (ಕೇಂದ್ರ 30%, ರಾಜ್ಯ 50%, ರೈತರ ಪಾಲು ಕೇವಲ 20%).",
        "benefit_en": "Up to 80% subsidy (30% Central + 50% State) for standalone solar water pumping systems.",
        "eligibility_kn": "ವಿದ್ಯುತ್ ಸಂಪರ್ಕವಿಲ್ಲದ ಅಥವಾ ಡೀಸೆಲ್ ಪಂಪ್ ಬಳಸುತ್ತಿರುವ ಸ್ವಂತ ಕೊಳವೆಬಾವಿ ಹೊಂದಿರುವ ರೈತರು.",
        "eligibility_en": "Individual farmers, panchayats, FPOs having suitable water source without grid electricity.",
        "documents_kn": "ಪಹಣಿ, ಆಧಾರ್, ಬ್ಯಾಂಕ್ ವಿವರ, ಕೊಳವೆಬಾವಿ ಪ್ರಮಾಣಪತ್ರ.",
        "documents_en": "RTC, Aadhaar, bank passbook, water source yield certificate.",
        "apply_kn": "kredl.karnataka.gov.in ಅಥವಾ ಬೆಸ್ಕಾಂ/ಮೆಸ್ಕಾಂ ಕಚೇರಿಗಳಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
        "apply_en": "Apply through KREDL portal (kredl.karnataka.gov.in) or local ESCOM office.",
        "audio_kn": "ಕುಸುಮ್ ಯೋಜನೆಯಲ್ಲಿ ಸೋಲಾರ್ ಪಂಪ್‌ಗೆ ಶೇಕಡಾ 80 ಸಹಾಯಧನ ಸಿಗುತ್ತದೆ. ಕರೆಂಟ್ ಇಲ್ಲದ ಜಮೀನುಗಳಿಗೆ ಇದು ವರದಾನವಾಗಿದೆ. ಕೆಆರ್‌ಇಡಿಎಲ್ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ."
    }
]

# ==========================================
# 4. KARNATAKA DISTRICT WEATHER HUBS
# ==========================================
DISTRICT_COORDINATES = {
    "mandya": {"name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "lat": 12.5238, "lon": 76.8973},
    "mysuru": {"name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "lat": 12.2958, "lon": 76.6394},
    "bengaluru": {"name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "lat": 12.9716, "lon": 77.5946},
    "hubballi": {"name_kn": "ಹುಬ್ಬಳ್ಳಿ - ಧಾರವಾಡ", "name_en": "Hubballi-Dharwad", "lat": 15.3647, "lon": 75.1240},
    "belagavi": {"name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "lat": 15.8497, "lon": 74.4977},
    "raichur": {"name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "lat": 16.2076, "lon": 77.3463},
    "kalaburagi": {"name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "lat": 17.3297, "lon": 76.8343},
    "shimoga": {"name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "lat": 13.9299, "lon": 75.5681},
    "davanagere": {"name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "lat": 14.4644, "lon": 75.9218},
    "hassan": {"name_kn": "ಹಾಸನ", "name_en": "Hassan", "lat": 13.0072, "lon": 76.1029},
    "tumakuru": {"name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "lat": 13.3409, "lon": 77.1006},
    "bagalkot": {"name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkot", "lat": 16.1691, "lon": 75.6615},
    "ballari": {"name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "lat": 15.1394, "lon": 76.9214},
    "udupi": {"name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "lat": 13.3409, "lon": 74.7421},
    "chikkamagaluru": {"name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "lat": 13.3161, "lon": 75.7720}
}


def get_weather_advisory(temp, humidity, rain_prob, lang="kn"):
    """Generate dynamic farming advice based on weather parameters"""
    if rain_prob >= 50:
        if lang == "kn":
            return {
                "headline": "🌧️ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ ಹೆಚ್ಚಿದೆ",
                "spraying": "❌ ಇಂದು ಯಾವುದೇ ಕ್ರಿಮಿನಾಶಕ ಅಥವಾ ರಸಗೊಬ್ಬರ ಸಿಂಪಡಿಸಬೇಡಿ (ಮಳೆಯಲ್ಲಿ ತೊಳೆದುಹೋಗುತ್ತದೆ).",
                "irrigation": "🛑 ಜಮೀನಿಗೆ ನೀರು ಹಾಯಿಸುವುದನ್ನು ನಿಲ್ಲಿಸಿ.",
                "drainage": "✅ ತೋಟ ಮತ್ತು ಗದ್ದೆಗಳಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ಬಸಿಗಾಲುವೆ (ಚರಂಡಿ) ತೆರವುಗೊಳಿಸಿ.",
                "audio": "ಇಂದು ಮಳೆಯ ಸಾಧ್ಯತೆ ಹೆಚ್ಚಿದೆ. ಕೀಟನಾಶಕ ಸಿಂಪಡಿಸಬೇಡಿ ಮತ್ತು ನೀರು ನಿಲ್ಲದಂತೆ ಚರಂಡಿ ಸ್ವಚ್ಛಗೊಳಿಸಿ."
            }
        else:
            return {
                "headline": "🌧️ High Probability of Rain",
                "spraying": "❌ Do not spray pesticides or foliar fertilizers today (will wash away).",
                "irrigation": "🛑 Suspend field irrigation.",
                "drainage": "✅ Clear drainage channels to prevent water stagnation in fields.",
                "audio": "High chance of rain today. Avoid spraying chemicals and ensure field drainage."
            }
    elif temp >= 34:
        if lang == "kn":
            return {
                "headline": "☀️ ಅಧಿಕ ತಾಪಮಾನ ಮತ್ತು ಬಿಸಿಲು",
                "spraying": "⚠️ ಸಿಂಪಡಣೆಯನ್ನು ಮುಂಜಾನೆ 9 ಗಂಟೆ ಮೊದಲು ಅಥವಾ ಸಂಜೆ 4 ಗಂಟೆಯ ನಂತರ ಮಾಡಿ.",
                "irrigation": "💧 ಮುಂಜಾನೆ ಅಥವಾ ಸಂಜೆ ಲಘು ನೀರಾವರಿ ನೀಡಿ, ಮಣ್ಣಿನ ತೇವಾಂಶ ಉಳಿಸಲು ಮಲ್ಚಿಂಗ್ ಬಳಸಿ.",
                "drainage": "✅ ಹನಿ ನೀರಾವರಿ ಬಳಸಿ ನೀರು ಆವಿಯಾಗುವುದನ್ನು ತಡೆಯಿರಿ.",
                "audio": "ಬಿಸಿಲು ಹೆಚ್ಚಿದೆ. ಮುಂಜಾನೆ ಅಥವಾ ಸಂಜೆ ವೇಳೆ ಮಾತ್ರ ನೀರು ಹಾಯಿಸಿ ಮತ್ತು ಸಿಂಪಡಣೆ ಮಾಡಿ."
            }
        else:
            return {
                "headline": "☀️ High Temperature Advisory",
                "spraying": "⚠️ Conduct spray operations before 9 AM or after 4 PM only.",
                "irrigation": "💧 Irrigate during cool morning or evening hours; practice mulching.",
                "drainage": "✅ Adopt drip irrigation to conserve soil moisture.",
                "audio": "High temperature alert. Irrigate and spray strictly during cool hours."
            }
    elif humidity >= 80:
        if lang == "kn":
            return {
                "headline": "🌫️ ಹೆಚ್ಚಿನ ಆರ್ದ್ರತೆ (ತೇವದ ವಾತಾವರಣ)",
                "spraying": "🌿 ಶಿಲೀಂಧ್ರ ಮತ್ತು ಎಲೆ ಚುಕ್ಕೆ ರೋಗಗಳ ಲಕ್ಷಣಗಳನ್ನು ಸೂಕ್ಷ್ಮವಾಗಿ ಗಮನಿಸಿ.",
                "irrigation": "💧 ಅತಿಯಾದ ನೀರು ನಿಲ್ಲದಂತೆ ಹದವಾದ ತೇವಾಂಶ ಕಾಯ್ದುಕೊಳ್ಳಿ.",
                "drainage": "✅ ಮುನ್ನೆಚ್ಚರಿಕೆಯಾಗಿ ಬೇವಿನ ಎಣ್ಣೆ ಅಥವಾ ಟ್ರೈಕೋಡರ್ಮಾ ಸಿಂಪಡಿಸಿ.",
                "audio": "ವಾತಾವರಣದಲ್ಲಿ ತೇವಾಂಶ ಹೆಚ್ಚಿದೆ. ಶಿಲೀಂಧ್ರ ರೋಗಗಳ ಬಗ್ಗೆ ಎಚ್ಚರವಿರಲಿ, ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ."
            }
        else:
            return {
                "headline": "🌫️ High Humidity Advisory",
                "spraying": "🌿 Monitor crops for fungal blights and mildew infections.",
                "irrigation": "💧 Avoid overwatering to prevent root dampening.",
                "drainage": "✅ Apply preventive neem oil or biocontrol agents.",
                "audio": "High humidity detected. Watch for fungal diseases and spray organic neem oil."
            }
    else:
        if lang == "kn":
            return {
                "headline": "🌤️ ಕೃಷಿ ಕೆಲಸಗಳಿಗೆ ಅನುಕೂಲಕರ ಹವಾಮಾನ",
                "spraying": "✅ ಕೀಟನಾಶಕ ಸಿಂಪಡಣೆ ಮತ್ತು ಮೇಲುಗೊಬ್ಬರ ನೀಡಲು ಸೂಕ್ತ ದಿನವಾಗಿದೆ.",
                "irrigation": "💧 ಬೆಳೆಯ ಅಗತ್ಯಕ್ಕೆ ತಕ್ಕಂತೆ ನಿಯಮಿತ ನೀರು ಹಾಯಿಸಿ.",
                "drainage": "✅ ಕಳೆ ಕೀಳುವಿಕೆ ಮತ್ತು ಮಣ್ಣು ಸಡಿಲಗೊಳಿಸುವ ಕೆಲಸ ಮಾಡಬಹುದು.",
                "audio": "ಇಂದು ಹವಾಮಾನವು ಉತ್ತಮವಾಗಿದೆ. ರಸಗೊಬ್ಬರ ನೀಡಲು ಮತ್ತು ಸಿಂಪಡಣೆಗೆ ಸೂಕ್ತ ದಿನ."
            }
        else:
            return {
                "headline": "🌤️ Favourable Farming Weather",
                "spraying": "✅ Favourable condition for pesticide spray and fertilizer application.",
                "irrigation": "💧 Provide scheduled crop irrigation.",
                "drainage": "✅ Ideal day for weeding, hoeing, and soil intercultural operations.",
                "audio": "Weather is pleasant and favourable for farm operations and spraying."
            }


# ==========================================
# 5. NATURAL LANGUAGE AGRICULTURAL MATCHING ENGINE
# ==========================================
def smart_agricultural_answer(query_text, lang="kn"):
    """
    Intelligent domain reasoning engine for farmer voice queries.
    Identifies topics: Crop advice, Weather updates, Disease solutions, Government schemes.
    Returns structured data with Kannada and English answers and audio text.
    """
    text = query_text.lower().strip()

    # ----------------------------------------------------
    # A. GOVERNMENT SCHEMES (ಯೋಜನೆಗಳು)
    # ----------------------------------------------------
    scheme_keywords = ["scheme", "yojana", "yojane", "pm kisan", "pm-kisan", "raitha siri", "siri",
                       "krishi bhagya", "bhagya", "fasal bima", "bima", "insurance", "yashaswini",
                       "kusum", "solar pump", "subsidy", "ಸಹಾಯಧನ", "ಯೋಜನೆ", "ಕಿಸಾನ್", "ರೈತ ಸಿರಿ",
                       "ಕೃಷಿ ಭಾಗ್ಯ", "ವಿಮೆ", "ಯಶಸ್ವಿನಿ", "ಕುಸುಮ್", "ಸೋಲಾರ್", "ಹಣ", "ಪಹಣಿ", "ಆರ್‌ಟಿಸಿ"]

    if any(k in text for k in scheme_keywords):
        # Match specific scheme
        if "pm kisan" in text or "ಕಿಸಾನ್" in text or "6000" in text:
            s = SCHEMES_DATA[0]
        elif "raitha siri" in text or "ರೈತ ಸಿರಿ" in text or "ಸಿರಿಧಾನ್ಯ" in text or "10000" in text:
            s = SCHEMES_DATA[1]
        elif "krishi bhagya" in text or "ಕೃಷಿ ಭಾಗ್ಯ" in text or "ಹೊಂಡ" in text or "farm pond" in text:
            s = SCHEMES_DATA[2]
        elif "fasal bima" in text or "ವಿಮೆ" in text or "insurance" in text or "pmfby" in text or "ನಷ್ಟ" in text:
            s = SCHEMES_DATA[3]
        elif "yashaswini" in text or "ಯಶಸ್ವಿನಿ" in text or "ಆಸ್ಪತ್ರೆ" in text or "health" in text:
            s = SCHEMES_DATA[4]
        elif "kusum" in text or "ಕುಸುಮ್" in text or "solar" in text or "ಸೋಲಾರ್" in text:
            s = SCHEMES_DATA[5]
        else:
            s = SCHEMES_DATA[0]

        if lang == "kn":
            answer = (
                f"📄 **{s['name_kn']}**\n\n"
                f"💰 **ಲಾಭ / ಪ್ರಯೋಜನ:** {s['benefit_kn']}\n\n"
                f"👨‍🌾 **ಅರ್ಹತೆ:** {s['eligibility_kn']}\n\n"
                f"📑 **ದಾಖಲೆಗಳು:** {s['documents_kn']}\n\n"
                f"📌 **ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ವಿಧಾನ:** {s['apply_kn']}"
            )
            audio = s['audio_kn']
        else:
            answer = (
                f"📄 **{s['name_en']}**\n\n"
                f"💰 **Benefits:** {s['benefit_en']}\n\n"
                f"👨‍🌾 **Eligibility:** {s['eligibility_en']}\n\n"
                f"📑 **Documents Needed:** {s['documents_en']}\n\n"
                f"📌 **How to Apply:** {s['apply_en']}"
            )
            audio = f"Information about {s['name_en']}. {s['benefit_en']} Contact local authorities to apply."

        return {
            "category": "scheme",
            "category_label": "ಸರ್ಕಾರಿ ಯೋಜನೆ 📄" if lang == "kn" else "Govt Scheme 📄",
            "title": s['name_kn'] if lang == "kn" else s['name_en'],
            "answer": answer,
            "audio_text": audio,
            "helpline": "1800-180-1551 (ಕಿಸಾನ್ ಕಾಲ್ ಸೆಂಟರ್)"
        }

    # ----------------------------------------------------
    # B. DISEASE & PEST SOLUTIONS (ರೋಗ & ಕೀಟ ಪರಿಹಾರ)
    # ----------------------------------------------------
    disease_keywords = ["disease", "pest", "worm", "curl", "yellow", "blast", "borer", "wilt", "rot",
                        "fungus", "spray", "ರೋಗ", "ಹುಳು", "ಸೈನಿಕ ಹುಳು", "ಎಲೆ", "ಸುರುಟು", "ಹಳದಿ",
                        "ಬೆಂಕಿ ರೋಗ", "ಕೊಳೆತ", "ಸಿಂಪಡಣೆ", "ಕೀಟ", "ಬೂದಿ ರೋಗ", "ನುಸಿ", "ಕಾಯಿಕೊರಕ"]

    if any(k in text for k in disease_keywords):
        if "ಟೊಮೇಟೊ" in text or "tomato" in text or "curl" in text or "ಸುರುಟು" in text:
            d = DISEASES_DATA[0]
        elif "ಭತ್ತ" in text or "paddy" in text or "rice" in text or "blast" in text or "ಬೆಂಕಿ" in text:
            d = DISEASES_DATA[1]
        elif "ಮೆಕ್ಕೆಜೋಳ" in text or "maize" in text or "corn" in text or "armyworm" in text or "ಸೈನಿಕ" in text:
            d = DISEASES_DATA[2]
        elif "ಕಬ್ಬು" in text or "sugarcane" in text or "red rot" in text or "ಕೆಂಪು" in text:
            d = DISEASES_DATA[3]
        elif "ಹತ್ತಿ" in text or "cotton" in text or "bollworm" in text:
            d = DISEASES_DATA[4]
        else:
            d = DISEASES_DATA[0]

        if lang == "kn":
            answer = (
                f"🦠 **{d['disease_kn']}** ({d['crop']})\n\n"
                f"🔍 **ಲಕ್ಷಣಗಳು:** {d['symptoms_kn']}\n\n"
                f"🌿 **ಸಾವಯವ ಪರಿಹಾರ:** {d['organic_remedy_kn']}\n\n"
                f"🧪 **ರಾಸಾಯನಿಕ ಸಿಂಪಡಣೆ:** {d['chemical_remedy_kn']}\n\n"
                f"🛡️ **ಮುನ್ನೆಚ್ಚರಿಕೆ:** {d['prevention_kn']}"
            )
            audio = d['audio_kn']
        else:
            answer = (
                f"🦠 **{d['disease_en']}** ({d['crop']})\n\n"
                f"🔍 **Symptoms:** {d['symptoms_en']}\n\n"
                f"🌿 **Organic Remedy:** {d['organic_remedy_en']}\n\n"
                f"🧪 **Chemical Spray:** {d['chemical_remedy_en']}\n\n"
                f"🛡️ **Prevention:** {d['prevention_en']}"
            )
            audio = f"For {d['disease_en']} in {d['crop']}: {d['organic_remedy_en']} If severe, spray {d['chemical_remedy_en']}"

        return {
            "category": "disease",
            "category_label": "ರೋಗ ಪರಿಹಾರ 🦠" if lang == "kn" else "Disease Solution 🦠",
            "title": d['disease_kn'] if lang == "kn" else d['disease_en'],
            "answer": answer,
            "audio_text": audio,
            "crop": d['crop']
        }

    # ----------------------------------------------------
    # C. WEATHER UPDATES (ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ)
    # ----------------------------------------------------
    weather_keywords = ["weather", "rain", "temperature", "forecast", "climate", "cloud",
                        "ಹವಾಮಾನ", "ಮಳೆ", "ಬಿಸಿಲು", "ತಾಪಮಾನ", "ಮುನ್ಸೂಚನೆ", "ಮೋಡ"]

    if any(k in text for k in weather_keywords):
        advisory = get_weather_advisory(28, 65, 20, lang)
        if lang == "kn":
            answer = (
                f"🌦️ **ಇಂದಿನ ಕೃಷಿ ಹವಾಮಾನ ವರದಿ**\n\n"
                f"🌡️ **ತಾಪಮಾನ:** 26°C - 30°C (ಹದವಾದ ಬಿಸಿಲು)\n"
                f"💧 **ಆರ್ದ್ರತೆ:** 65%\n"
                f"🌧️ **ಮಳೆಯ ಸಾಧ್ಯತೆ:** 15% (ಹಗುರ ಮೋಡ)\n\n"
                f"📢 **ರೈತರಿಗೆ ಸಲಹೆ:** {advisory['headline']}\n"
                f"• {advisory['spraying']}\n"
                f"• {advisory['irrigation']}\n"
                f"• {advisory['drainage']}"
            )
            audio = advisory['audio']
        else:
            answer = (
                f"🌦️ **Live Farming Weather Advisory**\n\n"
                f"🌡️ **Temperature:** 26°C - 30°C (Pleasant)\n"
                f"💧 **Humidity:** 65%\n"
                f"🌧️ **Precipitation:** 15% (Light clouds)\n\n"
                f"📢 **Farming Advisory:** {advisory['headline']}\n"
                f"• {advisory['spraying']}\n"
                f"• {advisory['irrigation']}\n"
                f"• {advisory['drainage']}"
            )
            audio = advisory['audio']

        return {
            "category": "weather",
            "category_label": "ಹವಾಮಾನ ಮಾಹಿತಿ 🌦️" if lang == "kn" else "Weather Advisory 🌦️",
            "title": "ಕೃಷಿ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ" if lang == "kn" else "Agricultural Weather Forecast",
            "answer": answer,
            "audio_text": audio
        }

    # ----------------------------------------------------
    # D. CROP ADVICE & TIPS (ಬೆಳೆ ಮಾಹಿತಿ & ಸಲಹೆ)
    # ----------------------------------------------------
    matched_crop = None
    if "ರಾಗಿ" in text or "ragi" in text or "millet" in text:
        matched_crop = CROPS_DATA[0]
    elif "ಭತ್ತ" in text or "paddy" in text or "rice" in text or "ಅಕ್ಕಿ" in text:
        matched_crop = CROPS_DATA[1]
    elif "ಮೆಕ್ಕೆಜೋಳ" in text or "maize" in text or "corn" in text or "ಜೋಳ" in text:
        matched_crop = CROPS_DATA[2]
    elif "ಕಬ್ಬು" in text or "sugarcane" in text:
        matched_crop = CROPS_DATA[3]
    elif "ಹತ್ತಿ" in text or "cotton" in text:
        matched_crop = CROPS_DATA[4]
    elif "ಟೊಮೇಟೊ" in text or "tomato" in text or "ಟೊಮ್ಯಾಟೊ" in text:
        matched_crop = CROPS_DATA[5]
    elif "ಅಡಿಕೆ" in text or "arecanut" in text or "ಅಡಕೆ" in text:
        matched_crop = CROPS_DATA[6]
    elif "ಶೇಂಗಾ" in text or "groundnut" in text or "ಕಡಲೆಕಾಯಿ" in text or "peanut" in text:
        matched_crop = CROPS_DATA[7]
    elif "ತೊಗರಿ" in text or "redgram" in text or "toor" in text or "ಬೇಳೆ" in text:
        matched_crop = CROPS_DATA[8]
    elif "ಮೆಣಸಿನಕಾಯಿ" in text or "chilli" in text or "ಖಾರ" in text:
        matched_crop = CROPS_DATA[9]

    if matched_crop:
        c = matched_crop
        if lang == "kn":
            answer = (
                f"🌾 **{c['name_kn']} - ಸಮಗ್ರ ಕೃಷಿ ಸಲಹೆ**\n\n"
                f"🗓️ **ಬಿತ್ತನೆ ಕಾಲ:** {c['season_kn']}\n\n"
                f"🌱 **ಮಣ್ಣು:** {c['soil_kn']}\n\n"
                f"💧 **ನೀರು ನಿರ್ವಹಣೆ:** {c['water_kn']}\n\n"
                f"🧪 **ರಸಗೊಬ್ಬರ (NPK):** {c['fertilizer_kn']}\n\n"
                f"🛡️ **ಕೀಟ & ರೋಗ ನಿಯಂತ್ರಣ:** {c['pests_diseases_kn']}\n\n"
                f"📈 **ನಿರೀಕ್ಷಿತ ಇಳುವರಿ:** {c['yield_kn']}"
            )
            audio = c['audio_summary_kn']
        else:
            answer = (
                f"🌾 **{c['name_en']} - Crop Advisory**\n\n"
                f"🗓️ **Sowing Season:** {c['season_en']}\n\n"
                f"🌱 **Soil Requirements:** {c['soil_en']}\n\n"
                f"💧 **Water & Irrigation:** {c['water_en']}\n\n"
                f"🧪 **Fertilizer Dosage:** {c['fertilizer_en']}\n\n"
                f"🛡️ **Pests & Diseases:** {c['pests_diseases_en']}\n\n"
                f"📈 **Expected Yield:** {c['yield_en']}"
            )
            audio = c['audio_summary_en']

        return {
            "category": "crop",
            "category_label": "ಬೆಳೆ ಸಲಹೆ 🌾" if lang == "kn" else "Crop Advice 🌾",
            "title": c['name_kn'] if lang == "kn" else c['name_en'],
            "answer": answer,
            "audio_text": audio
        }

    # General default agricultural guidance
    if lang == "kn":
        answer = (
            "🌾 **ಅಗ್ರಿವಾಯ್ಸ್ ಕೃಷಿ AI ಮಾರ್ಗದರ್ಶನ**\n\n"
            "ನಿಮ್ಮ ಪ್ರಶ್ನೆಗೆ ಸೂಕ್ತ ಉತ್ತರ ನೀಡಲು ಈ ಕೆಳಗಿನ ವಿಷಯಗಳನ್ನು ನೇರವಾಗಿ ಕೇಳಿ:\n"
            "• **ಬೆಳೆ ಸಲಹೆ:** ರಾಗಿ, ಭತ್ತ, ಮೆಕ್ಕೆಜೋಳ, ಕಬ್ಬು, ಟೊಮೇಟೊ ಅಥವಾ ಅಡಿಕೆ ಬಿತ್ತನೆ ಮತ್ತು ಗೊಬ್ಬರದ ವಿವರ.\n"
            "• **ಹವಾಮಾನ:** ಇಂದಿನ ಮಳೆ ಮುನ್ಸೂಚನೆ ಮತ್ತು ಸಿಂಪಡಣೆ ಸಲಹೆ.\n"
            "• **ರೋಗ ಪರಿಹಾರ:** ಎಲೆ ಸುರುಟು, ಬೆಂಕಿ ರೋಗ ಅಥವಾ ಸೈನಿಕ ಹುಳು ನಿಯಂತ್ರಣ.\n"
            "• **ಸರ್ಕಾರಿ ಯೋಜನೆ:** ಪಿಎಂ ಕಿಸಾನ್, ರೈತ ಸಿರಿ, ಕೃಷಿ ಭಾಗ್ಯ ಅಥವಾ ಬೆಳೆ ವಿಮೆ ವಿವರ."
        )
        audio = "ಅಗ್ರಿವಾಯ್ಸ್ ಕೃಷಿ ಸಹಾಯಕ್ಕೆ ಸ್ವಾಗತ. ಬೆಳೆ ಸಲಹೆ, ಹವಾಮಾನ, ರೋಗ ಪರಿಹಾರ ಅಥವಾ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಬಗ್ಗೆ ಮೈಕ್ ಒತ್ತಿ ಮಾತನಾಡಿ."
    else:
        answer = (
            "🌾 **AgriVoice Farming Guidance**\n\n"
            "Speak clearly into the microphone to ask about:\n"
            "• **Crop Advice:** Sowing time, fertilizers, water needs for Ragi, Paddy, Maize, Tomato, Sugarcane.\n"
            "• **Weather Updates:** Daily rain probability and spraying condition.\n"
            "• **Disease Diagnosis:** Leaf curl, paddy blast, armyworm remedies.\n"
            "• **Government Schemes:** PM-Kisan, Raitha Siri, Krishi Bhagya, and PMFBY insurance."
        )
        audio = "Welcome to AgriVoice AI. Please speak into the mic to ask about crops, weather, diseases, or government schemes."

    return {
        "category": "general",
        "category_label": "ಸಾಮಾನ್ಯ ಸಲಹೆ 💡" if lang == "kn" else "General Advice 💡",
        "title": "ಕೃಷಿ ಸಲಹೆಗಾರ" if lang == "kn" else "Farming Assistant",
        "answer": answer,
        "audio_text": audio
    }
