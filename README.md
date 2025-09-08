# 🌫️ Pollution Drift Predictor

A modular machine learning project to predict **SPM (Suspended Particulate Matter)** levels based on pollutant concentrations like **SO₂** and **NO₂**, using historical air quality data from Hyderabad.

---

## 📁 Project Structure

```
Pollution-Drift-Predictor/
│
├── archive/              # Reusable modules, plots, and general notebooks
├── WEEK1/                # Data exploration and preprocessing
├── WEEK2/                # Model training and evaluation
├── WEEK3/                # Streamlit deployment and app interface
├── WEEK4/                # Final presentation and wrap-up
├── main data/            # Raw dataset (data.csv)
├── requirements.txt      # Python dependencies
├── LICENSE               # Open-source license
└── README.md             # Project overview (this file)
```

---

## 📆 Weekly Breakdown

### 🔹 WEEK1: Data Exploration
- Cleaned and visualized pollution data
- Explored relationships between pollutants and SPM
- Notebook: [`week1_model_exploration.ipynb`](WEEK1/notebooks/week1_model_exploration.ipynb)

### 🔹 WEEK2: Model Training
- Trained a Linear Regression model on SO₂ and NO₂
- Evaluated using R², MAE, MSE, and Error %
- Notebook: [`week2_model_training.ipynb`](WEEK2/notebooks/week2_model_training.ipynb)
- Model: [`linear_regression_model.pkl`](WEEK2/linear_regression_model.pkl)

### 🔹 WEEK3: Streamlit Deployment
- Built an interactive web app to predict SPM
- Includes risk interpretation, charting, and CSV export
- App: [`streamlit_app.py`](WEEK3/streamlit_app.py)
- Notebook (documentation): [`week3_streamlit_app.ipynb`](WEEK3/notebooks/week3_streamlit_app.ipynb)

### 🔹 WEEK4: Final Presentation
- Summarized findings and workflow in a presentation
- File: [`PollutionDrift_PPT.pptx`](WEEK4/PollutionDrift_PPT.pptx)

---

## 🧰 Archive Folder

The `archive/` directory contains reusable components:
- `src/`: Modular Python scripts for data ingestion, modeling, and visualization
- `assets/`: Saved plots and figures
- `notebooks/`: General-purpose notebooks like `model_exploration.ipynb`

---

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/rajghosh06-dev/Pollution-Drift-Predictor.git
cd Pollution-Drift-Predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run WEEK3/streamlit_app.py
```

---

## 📊 Model Metrics (WEEK2)

- R² Score: *0.82*
- MAE: *12.45 µg/m³*
- MSE: *245.67*
- Error Percentage: *48.46%*

---

## 👤 Author

**Rishit Ghosh**  
Internship Project | SkillFuture AIML Track  
Hyderabad, India

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
