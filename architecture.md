# KrishiMitra — System Architecture

## Overview

KrishiMitra is a Streamlit-based web application designed to run on low-end devices with minimal or no internet (after first-time setup). It uses a modular tab-based UI with five core modules.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                   Streamlit Frontend                │
│  ┌──────────┬──────────┬──────────┬──────────────┐  │
│  │  Crop    │ Disease  │ Fert &   │  Market  │Voice│  │
│  │  Recomm. │ Detect.  │ Water    │  Prices  │ AI  │  │
│  └────┬─────┴────┬─────┴────┬─────┴──────────┴──┬──┘  │
│       │          │          │                   │     │
│  ┌────▼──┐  ┌───▼────┐ ┌──▼──────┐       ┌───▼──┐  │
│  │Random │  │HuggFace│ │ Hardcod │       │pyttsx│  │
│  │Forest │  │PlantDis│ │ ed Data │       │ +TTS │  │
│  │(sklearn│  │Classif.│ │ (pandas)│       │      │  │
│  └───────┘  └────────┘ └─────────┘       └──────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐   │
│  │       Argos Translate (Offline NMT)          │   │
│  │         English ↔ Tamil / Hindi              │   │
│  └──────────────────────────────────────────────┘   │
│                                                     │
│  ┌──────────────────────────────────────────────┐   │
│  │       Location & Weather Context             │   │
│  │   District input / GPS / Simulated weather   │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

## Module Descriptions

### 1. Crop Recommendation
- **Model**: Random Forest Classifier (100 estimators, scikit-learn)
- **Input**: N, P, K (soil nutrients), temperature, humidity, pH, rainfall
- **Output**: Best crop name + estimated input cost
- **Data**: 20-class embedded dataset (rice, coconut, tomato, banana, etc.)
- **Offline**: ✅ Fully offline

### 2. Disease Detection
- **Model**: `dima806/plant-disease-classifier` (HuggingFace)
- **Input**: Leaf image (JPG/PNG)
- **Output**: Disease label + confidence + treatment advice
- **Offline**: ✅ After first download (~200MB)

### 3. Fertilizer & Water Guide
- **Type**: Rule-based lookup table
- **Input**: Crop selection
- **Output**: NPK dose (kg/acre) + water requirement (mm)
- **Offline**: ✅ Fully offline

### 4. Market Prices
- **Type**: Static dataset (AGMARKNET-style)
- **Covers**: Rice, Coconut, Tomato, Banana, Sugarcane (Coimbatore region)
- **Offline**: ✅ Fully offline
- **Future**: Can be connected to live AGMARKNET API

### 5. Voice + AI Advisor
- **Translation**: Argos Translate (offline neural MT)
- **TTS**: pyttsx3 (system voice)
- **Future**: Can be upgraded with Whisper (speech-to-text) + Ollama (local LLM)

---

## Data Flow

```
User Input (language selected)
        │
        ▼
Streamlit UI (tab-based)
        │
        ▼
Module Processing (ML model / lookup table / image model)
        │
        ▼
Translation via Argos Translate (if Tamil/Hindi selected)
        │
        ▼
Displayed in UI + Optional TTS via pyttsx3
```

---

## Deployment Options

| Option | Description |
|---|---|
| Local Machine | `streamlit run app.py` |
| Streamlit Cloud | Push to GitHub → deploy at share.streamlit.io |
| Raspberry Pi | Lightweight enough for Pi 4 (4GB RAM) |
| Android (future) | Kivy or BeeWare port possible |

---

## Future Enhancements

- [ ] Live weather integration (OpenWeatherMap API)
- [ ] Speech-to-text input (Whisper model)
- [ ] Local LLM advisor (Ollama + Mistral 7B)
- [ ] Live AGMARKNET market price API
- [ ] More regional languages (Telugu, Kannada, Malayalam)
- [ ] Soil test image analysis
- [ ] Drone/satellite NDVI integration
