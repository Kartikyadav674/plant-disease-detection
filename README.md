# 🌿 PlantGuard AI: Crop Pathology Diagnostics & Advisory

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue.svg)](https://python.org)
[![Accuracy](https://img.shields.io/badge/Validation%20Accuracy-94.0%25-brightgreen.svg)]()

An end-to-end Deep Learning Computer Vision solution for automated plant leaf disease diagnosis and agronomic treatment recommendation across **38 classes** and **14 crop species**.

---

## 🌟 Key Highlights

- **94.0% Validation Accuracy** & **0.94 Weighted F1-Score** on 17,572 validation samples.
- **Trained on 87,907 images** from the benchmark PlantVillage dataset.
- **Deep 5-Block CNN Architecture** with over 6.5M parameters optimized via Adam (`lr=1e-4`).
- **Interactive Streamlit Web Dashboard** featuring:
  - 🔬 **Real-time leaf diagnosis** via photo upload or sample leaf selector.
  - 📋 **Agronomic action guides** with pathogen etiology, symptoms, and actionable treatment protocols.
  - 📊 **Training metrics & architecture inspector** visualizing epoch loss and accuracy trends.
  - 📖 **Disease Encyclopedia** covering all 38 supported crop conditions.

---

## 🏗️ Deep Convolutional Architecture

```mermaid
graph TD
    Input["Input Image (128x128x3 RGB)"] --> B1["Block 1: Conv2D(32) x2 + MaxPool2D(2,2)"]
    B1 --> B2["Block 2: Conv2D(64) x2 + MaxPool2D(2,2)"]
    B2 --> B3["Block 3: Conv2D(128) x2 + MaxPool2D(2,2)"]
    B3 --> B4["Block 4: Conv2D(256) x2 + MaxPool2D(2,2)"]
    B4 --> B5["Block 5: Conv2D(512) x2 + MaxPool2D(2,2)"]
    B5 --> Flatten["Flatten Layer"]
    Flatten --> Dense1["Dense(1500, ReLU)"]
    Dense1 --> Output["Dense(38, Softmax)"]
```

---

## 📁 Repository Structure

```text
├── app.py                      # Main Streamlit web application
├── disease_info.py             # 38-class metadata, causes & treatment recommendations
├── trained_model.keras         # Saved deep learning model (31.4 MB)
├── training_hist.json          # 10-epoch training & validation history
├── sample_images/              # Curated test images for instant one-click demo
├── requirements.txt            # Lightweight production dependencies for cloud deployment
├── .gitignore                  # Prevents pushing bulky 88k raw datasets to GitHub
├── Plant_disease_detection.ipynb # Complete training pipeline notebook
└── Test_Plant_Disease.ipynb    # Inference testing notebook
```

---

## 🚀 Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/plant-disease-detection.git
cd plant-disease-detection
```

### 2. Create and activate a virtual environment
```bash
python3.10 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deploying to Streamlit Cloud (Free Hosting)

1. Create a public repository on GitHub (e.g., `plant-disease-detection`).
2. Push your project code (`app.py`, `disease_info.py`, `trained_model.keras`, `sample_images/`, `requirements.txt`).
3. Visit [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.
4. Click **New app**, select your repository, set the main file path to `app.py`, and click **Deploy**.
5. Within 2-3 minutes, your live web app link is ready to share with recruiters and interviewers!
