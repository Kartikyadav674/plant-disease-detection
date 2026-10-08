import os
import json
from pathlib import Path
from PIL import Image
import numpy as np
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="PlantGuard AI - Crop Disease Diagnostic System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    /* Main container styling */
    .main-header {
        background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 50%, #40916c 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(27, 67, 50, 0.3);
    }
    .main-header h1 {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    .main-header p {
        font-size: 1.05rem;
        color: #d8f3dc;
        margin-bottom: 1rem;
    }
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
    }
    .badge {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(8px);
        padding: 0.35rem 0.85rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid rgba(255, 255, 255, 0.25);
    }
    .status-healthy {
        background-color: #d8f3dc;
        color: #1b4332;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        font-weight: 700;
        display: inline-block;
        border: 1px solid #74c69d;
    }
    .status-diseased {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        font-weight: 700;
        display: inline-block;
        border: 1px solid #f87171;
    }
    .card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.5rem;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.2rem;
    }
    .stProgress > div > div > div > div {
        background-color: #2d6a4f;
    }
</style>
""", unsafe_allow_html=True)

# Import Disease Metadata
try:
    from disease_info import CLASS_NAMES, CLASS_DETAILS
except ImportError:
    st.error("Missing disease_info.py module. Please verify project files.")
    st.stop()

# Helper: Load Keras Model with Caching
@st.cache_resource(show_spinner=False)
def load_disease_model():
    """Load model from .keras or .h5 with fallback."""
    import tensorflow as tf
    base_dir = Path(__file__).parent
    keras_path = base_dir / "trained_model.keras"
    h5_path = base_dir / "trained_model.h5"
    
    if keras_path.exists():
        try:
            return tf.keras.models.load_model(str(keras_path))
        except Exception as e:
            st.error(f"Error loading trained_model.keras: {e}")
            
    if h5_path.exists():
        try:
            return tf.keras.models.load_model(str(h5_path))
        except Exception as e:
            st.error(f"Error loading trained_model.h5: {e}")
            return None
            
    st.error("No model file ('trained_model.keras' or 'trained_model.h5') found in project directory.")
    return None

def preprocess_image(image: Image.Image, target_size=(128, 128)) -> np.ndarray:
    """Preprocess image matching model training pipeline."""
    # Ensure RGB
    if image.mode != "RGB":
        image = image.convert("RGB")
    # Resize to 128x128
    image_resized = image.resize(target_size, Image.Resampling.BILINEAR)
    img_array = np.array(image_resized, dtype=np.float32)
    # Model was trained directly on raw RGB uint8/float32 (0-255) without 1/255 rescaling
    expanded = np.expand_dims(img_array, axis=0)
    return expanded

# Sidebar Controls
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?auto=format&fit=crop&w=400&q=80", use_container_width=True)
    st.title("🌿 Navigation")
    app_mode = st.radio(
        "Select Section:",
        ["🔬 Disease Diagnosis", "📊 Model Performance", "📖 Disease Directory"],
        index=0
    )
    st.markdown("---")
    st.markdown("### 📌 Project Highlights")
    st.markdown("""
    - **Dataset**: PlantVillage (~88,000 images)
    - **Classes**: 38 Crop & Disease labels
    - **Test Accuracy**: **94.0%**
    - **Backbone**: Custom 5-Stage Deep CNN
    - **Input Resolution**: 128 × 128 px
    """)
    st.markdown("---")
    st.markdown("Created for Technical Portfolio & Interview Demonstration.")

# Main Header Banner
st.markdown("""
<div class="main-header">
    <h1>🌿 PlantGuard AI: Crop Pathology Diagnostics</h1>
    <p>Real-time deep learning computer vision system for automated agricultural leaf disease classification and precision treatment recommendations.</p>
    <div class="badge-container">
        <span class="badge">🎯 94% Validation Accuracy</span>
        <span class="badge">🌱 38 Plant Conditions</span>
        <span class="badge">🧠 5-Block CNN Architecture</span>
        <span class="badge">⚡ Sub-Second Inference</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- SECTION 1: LIVE DIAGNOSIS -----------------
if app_mode == "🔬 Disease Diagnosis":
    col_input, col_result = st.columns([1, 1.2], gap="large")
    
    with col_input:
        st.subheader("1. Provide a Crop Leaf Image")
        source_type = st.radio(
            "Image Source:",
            ["Choose from Curated Sample Images", "Upload Leaf Photo"],
            horizontal=True
        )
        
        selected_image = None
        image_name = None
        
        if source_type == "Choose from Curated Sample Images":
            sample_dir = Path("sample_images")
            if sample_dir.exists():
                samples = sorted(list(sample_dir.glob("*.JPG")) + list(sample_dir.glob("*.jpg")) + list(sample_dir.glob("*.png")))
            else:
                samples = []
                
            sample_map = {p.name: p for p in samples}
            
            if sample_map:
                chosen_sample = st.selectbox(
                    "Select a sample test leaf:",
                    options=list(sample_map.keys()),
                    format_func=lambda x: f"Sample: {x.replace('.JPG', '').replace('.jpg', '')}"
                )
                if chosen_sample:
                    image_path = sample_map[chosen_sample]
                    selected_image = Image.open(image_path)
                    image_name = chosen_sample
            else:
                st.info("No sample images found in `sample_images/`. You can upload an image below.")
                
        else:
            uploaded_file = st.file_uploader(
                "Upload a clear photo of an affected plant leaf (JPG, JPEG, PNG):",
                type=["jpg", "jpeg", "png"]
            )
            if uploaded_file is not None:
                selected_image = Image.open(uploaded_file)
                image_name = uploaded_file.name

        if selected_image is not None:
            st.image(selected_image, caption=f"Selected Leaf: {image_name}", use_container_width=True)
        else:
            st.info("👆 Please select a sample leaf or upload an image to start diagnosis.")

    with col_result:
        st.subheader("2. Diagnostic Analysis & Recommendation")
        
        if selected_image is not None:
            with st.spinner("Analyzing leaf pathology with Deep CNN..."):
                model = load_disease_model()
                
                if model is None:
                    st.warning("Model could not be loaded. Please ensure `trained_model.keras` or `trained_model.h5` exists.")
                else:
                    # Preprocess and Predict
                    input_tensor = preprocess_image(selected_image)
                    preds = model.predict(input_tensor, verbose=0)[0]
                    
                    top_indices = np.argsort(preds)[::-1][:3]
                    top_idx = top_indices[0]
                    predicted_class = CLASS_NAMES[top_idx]
                    confidence = float(preds[top_idx]) * 100
                    
                    details = CLASS_DETAILS.get(predicted_class, {
                        'plant': 'Unknown',
                        'condition': predicted_class,
                        'status': 'Diseased',
                        'cause': 'N/A',
                        'description': 'Information unavailable.',
                        'treatment': 'Consult a local agricultural extension specialist.'
                    })
                    
                    # Result Card
                    is_healthy = details['status'] == 'Healthy'
                    status_badge = (
                        f'<span class="status-healthy">✓ HEALTHY SPECIMEN</span>'
                        if is_healthy
                        else f'<span class="status-diseased">⚠️ PATHOLOGY DETECTED</span>'
                    )
                    
                    st.markdown(f"""
                    <div style="background: {'#f0fdf4' if is_healthy else '#fff5f5'}; border: 1.5px solid {'#86efac' if is_healthy else '#fca5a5'}; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 1.1rem; color: #4b5563; font-weight: 600;">Host: <strong>{details['plant']}</strong></span>
                            {status_badge}
                        </div>
                        <h2 style="margin: 0.2rem 0; color: {'#166534' if is_healthy else '#991b1b'}; font-size: 1.6rem;">{details['condition']}</h2>
                        <p style="margin: 0; color: #374151; font-size: 0.95rem;"><strong>Diagnosis Confidence:</strong> {confidence:.2f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Top 3 Candidates
                    st.markdown("##### Model Probability Distribution (Top 3 Candidates)")
                    for idx in top_indices:
                        c_name = CLASS_NAMES[idx]
                        c_info = CLASS_DETAILS.get(c_name, {'condition': c_name})
                        prob = float(preds[idx]) * 100
                        st.write(f"**{c_info['condition']}** ({prob:.1f}%)")
                        st.progress(min(prob / 100.0, 1.0))
                    
                    # Actionable Botanical Advisory
                    st.markdown("---")
                    st.markdown("### 📋 Agronomist Action Guide")
                    
                    st.markdown(f"**🔬 Causal Organism / Etiology:** {details['cause']}")
                    st.markdown(f"**🔍 Symptom Profile:** {details['description']}")
                    
                    if is_healthy:
                        st.success(f"**🌱 Maintenance Recommendation:** {details['treatment']}")
                    else:
                        st.warning(f"**💊 Recommended Treatment & Control Plan:** {details['treatment']}")
        else:
            st.markdown("""
            <div style="padding: 2.5rem; text-align: center; border: 2px dashed #cbd5e1; border-radius: 12px; color: #64748b;">
                <p style="font-size: 1.1rem; margin: 0;">No leaf image provided yet.</p>
                <small>Select an image on the left to see instant classification and treatment advice.</small>
            </div>
            """, unsafe_allow_html=True)

# ----------------- SECTION 2: MODEL PERFORMANCE -----------------
elif app_mode == "📊 Model Performance":
    st.subheader("Model Evaluation & Training Metrics")
    
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.metric(label="Validation Accuracy", value="94.0%", delta="+3.5% vs baseline")
    with m_col2:
        st.metric(label="Training Accuracy", value="98.6%", delta="Epoch 10")
    with m_col3:
        st.metric(label="Dataset Size", value="87,907 imgs", delta="PlantVillage")
    with m_col4:
        st.metric(label="Target Classes", value="38 Categories", delta="14 Crops")
        
    st.markdown("---")
    
    # Load Training History
    hist_file = Path("training_hist.json")
    if hist_file.exists():
        with open(hist_file, "r") as f:
            hist_data = json.load(f)
            
        epochs = list(range(1, len(hist_data.get("accuracy", [])) + 1))
        
        c_acc, c_loss = st.columns(2)
        with c_acc:
            st.markdown("##### 📈 Training vs Validation Accuracy")
            import matplotlib.pyplot as plt
            fig_acc, ax_acc = plt.subplots(figsize=(6, 3.5))
            ax_acc.plot(epochs, hist_data["accuracy"], marker='o', label="Training Accuracy", color="#2d6a4f")
            ax_acc.plot(epochs, hist_data["val_accuracy"], marker='s', label="Validation Accuracy", color="#e76f51")
            ax_acc.set_xlabel("Epoch")
            ax_acc.set_ylabel("Accuracy")
            ax_acc.grid(True, linestyle="--", alpha=0.5)
            ax_acc.legend()
            st.pyplot(fig_acc)
            
        with c_loss:
            st.markdown("##### 📉 Training vs Validation Loss")
            fig_loss, ax_loss = plt.subplots(figsize=(6, 3.5))
            ax_loss.plot(epochs, hist_data["loss"], marker='o', label="Training Loss", color="#1d3557")
            ax_loss.plot(epochs, hist_data["val_loss"], marker='s', label="Validation Loss", color="#e63946")
            ax_loss.set_xlabel("Epoch")
            ax_loss.set_ylabel("Categorical Loss")
            ax_loss.grid(True, linestyle="--", alpha=0.5)
            ax_loss.legend()
            st.pyplot(fig_loss)
    
    st.markdown("---")
    st.markdown("### 🏗️ Deep Convolutional Architecture Specification")
    st.markdown("""
    | Stage | Layer Details | Output Dimensions | Description |
    | :--- | :--- | :--- | :--- |
    | **Input** | `ImageInput` | `(128, 128, 3)` | RGB crop leaf input |
    | **Block 1** | `Conv2D(32) x2` + `MaxPool2D(2,2)` | `(63, 63, 32)` | Low-level feature extraction (edges, colors) |
    | **Block 2** | `Conv2D(64) x2` + `MaxPool2D(2,2)` | `(30, 30, 64)` | Mid-level textures and lesion patterns |
    | **Block 3** | `Conv2D(128) x2` + `MaxPool2D(2,2)` | `(14, 14, 128)` | Complex foliage & spot geometries |
    | **Block 4** | `Conv2D(256) x2` + `MaxPool2D(2,2)` | `(6, 6, 256)` | High-level disease feature representations |
    | **Block 5** | `Conv2D(512) x2` + `MaxPool2D(2,2)` | `(2, 2, 512)` | Semantic pathology abstraction |
    | **Head** | `Flatten` → `Dense(1500, relu)` | `1500` | Fully connected feature integration |
    | **Output** | `Dense(38, softmax)` | `38` | Probability distribution over 38 classes |
    """)

# ----------------- SECTION 3: DISEASE DIRECTORY -----------------
elif app_mode == "📖 Disease Directory":
    st.subheader("Botanical Disease & Crop Encyclopedia")
    st.write("Browse symptoms, causes, and treatments across all 38 recognized disease and healthy classes.")
    
    # Filter by plant
    plants = sorted(list({details['plant'] for details in CLASS_DETAILS.values()}))
    selected_plant = st.selectbox("Filter by Crop / Host Plant:", ["All Plants"] + plants)
    
    for c_id, info in CLASS_DETAILS.items():
        if selected_plant != "All Plants" and info['plant'] != selected_plant:
            continue
            
        badge = "🟢 Healthy" if info['status'] == "Healthy" else "🔴 Diseased"
        with st.expander(f"{info['plant']} — {info['condition']} ({badge})"):
            st.markdown(f"**Condition:** {info['condition']}")
            st.markdown(f"**Causal Agent:** {info['cause']}")
            st.markdown(f"**Description & Symptoms:** {info['description']}")
            st.markdown(f"**Treatment / Management:** {info['treatment']}")
            st.caption(f"Raw Label Key: `{c_id}`")
