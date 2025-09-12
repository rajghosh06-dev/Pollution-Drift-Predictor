# 🌫️ Week 3 – Pollution Drift Predictor (Deployment & Interface)

This week focuses on deploying the trained Linear Regression model from Week 2 using a Streamlit-based front-end interface. The app allows users to input SO₂ and NO₂ concentrations and receive real-time predictions of Suspended Particulate Matter (SPM) levels.

---

## 🚀 Features

- **Interactive UI** built with Streamlit  
- **Dropdown inputs** for SO₂ and NO₂ concentrations  
- **Real-time prediction** of SPM using the trained model  
- **Pollution risk interpretation** (Safe, Moderate, Unhealthy, Hazardous)  
- **Bar chart visualization** of input pollutants vs predicted SPM  
- **Downloadable CSV** of prediction results  
- **Expandable model info section** for transparency  

---

## 📁 File Structure

```
WEEK3/
├── apps/
│   ├── app_flask.py              # Flask-based web interface
│   └── app_streamlit.py          # Streamlit-based web interface
├── notebooks/
│   └── week3_streamlit_app.ipynb # Notebook version of Streamlit app
├── outputs/                      # Visual output samples for README or documentation
│   ├── output_SAFE.png           # Screenshot showing Safe pollution level
│   ├── output_MODERATE.png       # Screenshot showing Moderate pollution level
│   └── output_HAZARDOUS.png      # Screenshot showing Hazardous pollution level
├── README.md                     # Summary, screenshots & instructions for Week 3
```

> Note: The model is loaded from `../WEEK2/models/random_forest_model.pkl`. This file is required but not included in the GitHub repository.

---

## 🧪 How to Run

1. Activate your virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run apps/app_streamlit.py
   ```

3. Open your browser at:
   ```
   http://localhost:8501/
   ```

---

## 📊 Sample Inputs

| SO₂ (µg/m³) | NO₂ (µg/m³) | Predicted SPM (µg/m³) | Risk Level |
|-------------|--------------|------------------------|------------|
| 12.0        | 45.0         | 180.32                 | 🟠 Unhealthy |
| 5.0         | 20.0         | 92.15                  | 🟡 Moderate |

---

## ℹ️ Model Details

- **Algorithm**: Linear Regression  
- **Trained on**: Historical air pollution data from Hyderabad  
- **Features**: SO₂ and NO₂  
- **Target**: SPM (Suspended Particulate Matter)  

[Check WEEK-2](../WEEK2)

---

## 📤 Output Samples
Below are screenshots of the app interface showing different pollution risk levels based on user inputs:

### 🟢 Safe
![Safe Output](outputs/output_SAFE.png)

---
### 🟡 Moderate
![Moderate Output](outputs/output_MODERATE.png)

---
### 🔴 Hazardous
![Hazardous Output](outputs/output_HAZARDOUS.png)

---

## 🧾 Credits

Built by **Rishit Ghosh**  
SkillFuture AIML Internship – Week 3 Submission  
GitHub Repo: [Pollution-Drift-Predictor](https://github.com/rajghosh06-dev/Pollution-Drift-Predictor)

---
