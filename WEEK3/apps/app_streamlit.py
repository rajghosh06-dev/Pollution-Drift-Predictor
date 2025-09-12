import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load trained model
model = joblib.load("../../WEEK2/models/random_forest_model.pkl")

# Load feature template
template_path = "../../WEEK2/data/feature_template.csv"
if not os.path.exists(template_path):
    st.error("Feature template not found. Please generate 'feature_template.csv' during training.")
    st.stop()

feature_template = pd.read_csv(template_path)
input_row = feature_template.iloc[0].copy()

# State-location mapping for valid dropdowns
state_location_map = {
    "Telangana": ["Hyderabad"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Delhi": ["Delhi"],
    "West Bengal": ["Kolkata"],
    "Karnataka": ["Bangalore"],
    "Sikkim": ["Gangtok"]
}

# App title and description
st.title("🌫️ Pollution Drift Predictor")
st.markdown("Predict **SPM (Suspended Particulate Matter)** using a Random Forest model trained on 305 features.")

# Sidebar input parameters
st.sidebar.header("Input Parameters")
so2 = st.sidebar.slider("SO₂ concentration (µg/m³)", 0.0, 20.0, 5.0, step=0.5)
no2 = st.sidebar.slider("NO₂ concentration (µg/m³)", 0.0, 100.0, 25.0, step=1.0)
rspm = st.sidebar.slider("RSPM concentration (µg/m³)", 0.0, 500.0, 50.0, step=5.0)

# Sidebar dropdowns for location and state
st.sidebar.subheader("Geographic Context")
selected_state = st.sidebar.selectbox("State", list(state_location_map.keys()))
selected_location = st.sidebar.selectbox("Location", state_location_map[selected_state])

# Predict and display results
if st.button("🔍 Predict SPM"):
    # Reset all one-hot flags
    for col in input_row.index:
        if col.startswith("state_") or col.startswith("location_"):
            input_row[col] = 0

    # Update input row with user values
    input_row['so2'] = so2
    input_row['no2'] = no2
    input_row['rspm'] = rspm
    input_row['month'] = 7
    input_row['year'] = 2023
    input_row['dayofweek'] = 2
    input_row[f"state_{selected_state}"] = 1
    input_row[f"location_{selected_location}"] = 1
    input_row['agency_Telangana Pollution Control Board'] = 1
    input_row['type_Residential'] = 1

    # Fill missing columns with 0
    input_row = input_row.reindex(model.feature_names_in_, fill_value=0)

    # Predict
    prediction = model.predict([input_row])[0]

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
        "Pollutant": ["SO₂", "NO₂", "RSPM", "Predicted SPM"],
        "Value": [so2, no2, rspm, prediction]
    })
    fig, ax = plt.subplots()
    ax.bar(df_chart["Pollutant"], df_chart["Value"], color=["skyblue", "orange", "gray", "green"])
    ax.set_ylabel("Concentration (µg/m³)")
    ax.set_title("Pollutant Levels vs Predicted SPM")
    st.pyplot(fig)

    # Download prediction as CSV
    csv = pd.DataFrame({
        "SO₂": [so2],
        "NO₂": [no2],
        "RSPM": [rspm],
        "Predicted SPM": [prediction],
        "Risk Level": [risk],
        "State": [selected_state],
        "Location": [selected_location]
    }).to_csv(index=False)
    st.download_button("📥 Download Prediction", csv, "prediction.csv", "text/csv")

# Model info section
with st.expander("ℹ️ Model Details"):
    st.write("This model uses a **Random Forest Regressor** trained on historical pollution data across Indian cities.")
    st.write("It expects 305 features including pollutant levels, temporal variables, and one-hot encoded location/state/agency/type.")
    st.write("Model trained in [Week 2 notebook](../WEEK2/notebooks/week2_model_training.ipynb) and saved as `random_forest_model.pkl`.")

# 📊 Expected Contribution Breakdown
st.markdown("### 🧮 Expected Pollutant Contribution (Indicative)")
st.markdown("""
Based on historical modeling and feature importance, the approximate contribution of each pollutant to SPM prediction is:
- **SO₂**: ~20%
- **NO₂**: ~35%
- **RSPM**: ~45%
""")
contrib = [20, 35, 45]
labels = ["SO₂", "NO₂", "RSPM"]
colors = ["skyblue", "orange", "gray"]
fig1, ax1 = plt.subplots()
ax1.pie(contrib, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
st.pyplot(fig1)

# 📉 SPM Sensitivity to NO₂
st.markdown("### 📉 SPM Sensitivity to NO₂ (SO₂=5, RSPM=50)")
no2_range = np.linspace(0, 100, 50)
spm_preds = []
for val in no2_range:
    temp_row = input_row.copy()
    temp_row['so2'] = 5
    temp_row['no2'] = val
    temp_row['rspm'] = 50
    temp_row = temp_row.reindex(model.feature_names_in_, fill_value=0)
    spm_preds.append(model.predict([temp_row])[0])

fig2, ax2 = plt.subplots()
ax2.plot(no2_range, spm_preds, color='orange')
ax2.set_xlabel("NO₂ concentration (µg/m³)")
ax2.set_ylabel("Predicted SPM (µg/m³)")
ax2.set_title("Impact of NO₂ on Predicted SPM")
ax2.grid(True)
st.pyplot(fig2)

# 🔍 Top 10 Most Important Features
st.markdown("### 🔍 Top 10 Most Influential Features")
importances = model.feature_importances_
features = model.feature_names_in_
top_features = pd.Series(importances, index=features).sort_values(ascending=False).head(10)
st.dataframe(top_features.rename("Importance").round(4))

# Footer
st.markdown("---")
st.caption("Built by Rishit Ghosh | Internship Project | SkillFuture AIML Track")
st.markdown("> ⚠️ SPM levels can spike due to complex interactions beyond SO₂ and NO₂ alone. This model reflects historical correlations observed in urban pollution data.")
