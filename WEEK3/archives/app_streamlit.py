## run using streamlit run app_streamlit.py

import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("../WEEK2/linear_regression_model.pkl")

# App title and description
st.title("🌫️ Pollution Drift Predictor")
st.markdown("Predict **SPM (Suspended Particulate Matter)** based on SO₂ and NO₂ levels.")

# Sidebar input parameters
st.sidebar.header("Input Parameters")
so2_options = [round(x, 1) for x in range(0, 21)]
no2_options = [round(x, 1) for x in range(0, 101, 5)]
so2 = st.sidebar.selectbox("SO₂ concentration (µg/m³)", so2_options)
no2 = st.sidebar.selectbox("NO₂ concentration (µg/m³)", no2_options)

# Predict and display results
if st.button("🔍 Predict SPM"):
    prediction = model.predict([[so2, no2]])[0]
    st.success(f"Predicted SPM Level: **{prediction:.2f} µg/m³**")

    # Pollution risk interpretation
    if prediction < 50:
        risk = "🟢 Safe"
    elif prediction < 100:
        risk = "🟡 Moderate"
    elif prediction < 200:
        risk = "🟠 Unhealthy"
    else:
        risk = "🔴 Hazardous"
    st.markdown(f"### 🛑 Pollution Risk Level: **{risk}**")

    # Bar chart visualization
    st.markdown("### 📈 Prediction Chart")
    df_chart = pd.DataFrame({
        "Pollutant": ["SO₂", "NO₂", "Predicted SPM"],
        "Value": [so2, no2, prediction]
    })
    fig, ax = plt.subplots()
    ax.bar(df_chart["Pollutant"], df_chart["Value"], color=["skyblue", "orange", "green"])
    ax.set_ylabel("Concentration (µg/m³)")
    ax.set_title("Pollutant Levels vs Predicted SPM")
    st.pyplot(fig)

    # Download prediction as CSV
    csv = pd.DataFrame({
        "SO₂": [so2],
        "NO₂": [no2],
        "Predicted SPM": [prediction],
        "Risk Level": [risk]
    }).to_csv(index=False)
    st.download_button("📥 Download Prediction", csv, "prediction.csv", "text/csv")

# Model info section
with st.expander("ℹ️ Model Details"):
    st.write("This model uses Linear Regression trained on historical pollution data from Hyderabad.")
    st.write("Features: SO₂ and NO₂")
    st.write("Target: SPM (Suspended Particulate Matter)")

# Footer
st.markdown("---")
st.caption("Built by Rishit Ghosh | Internship Project | SkillFuture AIML Track")

##SPM (Suspended Particulate Matter) can spike due to complex interactions, not just SO₂ and NO₂ alone. Your model is trained on historical data, and it’s reflecting that elevated NO₂ levels often correlate with high particulate pollution in urban zones.
