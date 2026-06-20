import streamlit as st
import joblib

# ─── Load Model ───────────────────────────────────────────
svm_model = joblib.load('svm_pipeline.pkl')

# ─── Sidebar ──────────────────────────────────────────────
st.sidebar.title("🩺 Clinical Assistant")

st.sidebar.info(
    "Enter a clinical brief summary and click Predict Disease."
)
if st.sidebar.button("🔄 Clear All"):
    st.session_state["clinical_text"] = ""
    st.rerun()
# ─── Page Config ──────────────────────────────────────────
st.set_page_config(
    page_title="Clinical Trial Disease Prediction System",
    page_icon="🏥",
    layout="centered"
)

# ─── Title ────────────────────────────────────────────────
st.markdown(
    """
    <h1 style='text-align:center; font-size:42px;'>
    🏥 Clinical Trial Disease Prediction System
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown("Enter a clinical study brief summary to predict the **Disease**")
st.divider()

# ─── Input ────────────────────────────────────────────────
user_input = st.text_area(
    "📝 Clinical Study Brief Summary:",
    height=150,
    placeholder="e.g. Patient has high blood sugar levels and requires insulin therapy...",
    key="clinical_text"
)

# ─── Predict Button ───────────────────────────────────────
if st.button("🔍 Predict Disease", use_container_width=True):
    
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text first!")
    
    else:
        prediction = svm_model.predict([user_input])
        
        st.success(f"✅ Predicted Disease Category:")
        st.markdown(f"""
        <div style="
            background-color: #EFF6FF;
            border-left: 5px solid #2563EB;
            padding: 20px;
            border-radius: 8px;
            font-size: 22px;
            font-weight: bold;
            color: #1E40AF;
        ">
        🩺 {prediction[0].title()}
        </div>
        """, unsafe_allow_html=True)

