import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

THRESHOLD = 0.6

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ---------- Custom Styling ----------
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 5px;
}

.sub-text {
    text-align: center;
    font-size: 18px;
    opacity: 0.7;
    margin-bottom: 30px;
}

/* Card style that adapts to dark/light mode */
.card {
    padding: 25px;
    border-radius: 15px;
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

/* Better button */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-size: 16px;
    font-weight: 600;
}

/* Remove weird white spacing blocks */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="main-title">💳 Credit Card Fraud Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">AI-Powered Real-Time Transaction Risk Analysis</div>', unsafe_allow_html=True)

st.divider()

# ---------- Layout ----------
col1, col2 = st.columns([1, 1])

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        step = st.number_input("Transaction Time Step", min_value=0, value=1)

        transaction_type = st.selectbox(
            "Transaction Type",
            label_encoder.classes_
        )

        amount = st.number_input("Transaction Amount", min_value=0.0, value=0.0)

        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        oldbalanceOrg = st.number_input("Sender Old Balance", min_value=0.0, value=0.0)
        newbalanceOrig = st.number_input("Sender New Balance", min_value=0.0, value=0.0)
        oldbalanceDest = st.number_input("Receiver Old Balance", min_value=0.0, value=0.0)
        newbalanceDest = st.number_input("Receiver New Balance", min_value=0.0, value=0.0)

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Prediction Button ----------
if st.button("🔍 Predict Transaction Risk"):

    encoded_type = label_encoder.transform([transaction_type])[0]

    input_data = pd.DataFrame([{
        "step": step,
        "type": encoded_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "newbalanceDest": newbalanceDest,
        "oldbalanceDest": oldbalanceDest
    }])

    prob = model.predict_proba(input_data)[0][1]
    prediction = 1 if prob > THRESHOLD else 0

    st.divider()
    st.subheader("📊 Prediction Result")
    st.metric("Fraud Probability", f"{prob:.2%}")

    if prediction == 1:
        st.error("⚠️ High Risk: Fraudulent Transaction Detected")
    else:
        st.success("✅ Low Risk: Legitimate Transaction")