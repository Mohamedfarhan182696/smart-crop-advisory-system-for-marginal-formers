# 🌾 KrishiMitra — Smart Crop Advisory System for Marginal Farmers

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/AI%20Powered-HuggingFace-yellow?style=for-the-badge&logo=huggingface" />
  <img src="https://img.shields.io/badge/Offline-Capable-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Languages-EN%20%7C%20Tamil%20%7C%20Hindi-orange?style=for-the-badge" />
</p>

> **A fully offline-capable, multilingual AI advisory platform built for small and marginal farmers — with crop recommendations, plant disease detection, market prices, and a voice assistant.**

---

## 📌 Problem Statement

Small and marginal farmers (who make up ~86% of India's farming community) face major challenges:
- **No access** to real-time crop advisory or expert knowledge
- **Language barriers** — most tools are English-only
- **Poor connectivity** in rural areas
- **Low awareness** of market prices, fertilizer usage, and disease management

**KrishiMitra** solves this by providing a single, easy-to-use app that works offline, speaks their language, and gives AI-powered guidance — right on any device.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌱 **Crop Recommendation** | ML-based recommendation using soil NPK, temperature, humidity, rainfall & pH |
| 📸 **Plant Disease Detection** | Upload a leaf photo → AI identifies disease + gives treatment advice |
| 💧 **Fertilizer & Water Guide** | Crop-specific fertilizer dose & irrigation requirements |
| 🛒 **Market Prices** | Local mandi prices + nearest market locations (Coimbatore/Tamil Nadu) |
| 🗣️ **Voice + AI Advisor** | Ask questions in Tamil, Hindi, or English — get spoken answers |
| 🌍 **Multilingual** | Full UI & responses in English, Tamil (தமிழ்), Hindi (हिंदी) |
| 📍 **Location-Aware** | GPS-based hyper-local recommendations for your district |
| 🔌 **Offline-First** | Works fully offline after the first model download |

---

## 🖥️ Demo Screenshots

> *(Add screenshots here after running the app locally)*

---

## 🗂️ Project Structure

```
KrishiMitra/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .gitignore              # Files to exclude from Git
├── README.md               # This file
├── data/
│   └── sample_crops.csv    # Embedded crop dataset (optional external file)
├── models/
│   └── (auto-downloaded on first run via HuggingFace)
└── docs/
    └── architecture.md     # System architecture notes
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/KrishiMitra.git
cd KrishiMitra
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Argos Translate Language Packages (for Tamil & Hindi)

```python
# Run once in Python shell or add a setup script
import argostranslate.package
argostranslate.package.update_package_index()
available = argostranslate.package.get_available_packages()
# Install en→ta and en→hi
for pkg in available:
    if pkg.from_code == "en" and pkg.to_code in ["ta", "hi"]:
        argostranslate.package.install_from_path(pkg.download())
```

Or run the provided setup script:
```bash
python setup_languages.py
```

### 5. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🧠 AI Models Used

| Component | Model | Source |
|---|---|---|
| Crop Recommendation | Random Forest Classifier (scikit-learn) | Trained on embedded dataset |
| Disease Detection | `dima806/plant-disease-classifier` | HuggingFace (auto-download) |
| Translation | Argos Translate | Offline neural translation |
| Voice Output | pyttsx3 | System TTS (offline) |

---

## 📊 Dataset

The crop recommendation model is trained on soil and climate parameters:

| Feature | Description |
|---|---|
| N, P, K | Nitrogen, Phosphorus, Potassium (kg/acre) |
| Temperature | °C |
| Humidity | % |
| pH | Soil pH value |
| Rainfall | mm/season |
| Label | Recommended crop (20 crops supported) |

**Crops supported:** Rice, Wheat, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut

---

## 🌏 Multilingual Support

| Language | Code | Status |
|---|---|---|
| English | `en` | ✅ Built-in |
| Tamil (தமிழ்) | `ta` | ✅ Via Argos Translate |
| Hindi (हिंदी) | `hi` | ✅ Via Argos Translate |

---

## 📍 Location & Weather

- Default location: **Coimbatore, Tamil Nadu** (10.79°N, 76.96°E)
- Supports custom district/pincode input
- Simulated hyper-local weather for offline use (Temperature, Humidity, Soil Moisture)
- Can be extended with OpenWeatherMap API for real-time data

---

## 🔧 Tech Stack

- **Frontend**: Streamlit
- **ML**: scikit-learn (Random Forest)
- **Computer Vision**: HuggingFace Transformers (image-classification pipeline)
- **Translation**: Argos Translate (offline)
- **Voice**: pyttsx3
- **Data**: pandas, Pillow

---

## 🏆 Built For

This project was developed as part of the **Smart India Hackathon (SIH)** under the theme of empowering small and marginal farmers with AI-powered agricultural advisory.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mohamed** — Built with ❤️ for Indian farmers

---

## 🙏 Acknowledgements

- [TNAU Coimbatore](https://www.tnau.ac.in/) for agricultural domain knowledge
- [AGMARKNET](https://agmarknet.gov.in/) for market price data reference
- [HuggingFace](https://huggingface.co/) for the plant disease model
- [Streamlit](https://streamlit.io/) for the rapid UI framework
