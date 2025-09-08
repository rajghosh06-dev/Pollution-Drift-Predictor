# 🌿 Week 1 – Pollution Drift Predictor (Environmental Monitoring & Pollution Control)

## 📌 Project Theme

This project falls under the theme of **Environmental Monitoring & Pollution Control**, focusing on the prediction and analysis of airborne pollution drift using environmental data. Week 1 lays the foundation by exploring pollutant patterns across Indian cities and establishing a baseline model.

---

## 🎯 Objective

To explore and understand a real-world dataset related to air pollution, perform detailed exploratory data analysis (EDA), and build an initial regression model to evaluate the predictive potential of available features.

---

## 📦 Dataset Used

- **Source:** Kaggle – [Air Pollution Analysis and Prediction](https://www.kaggle.com/code/guidosalimbeni/air-pollution-analysis-and-prediction)
- **File:** `data.csv`
- **Size:** ~62 MB
- **Description:** Historical daily ambient air quality data across multiple Indian cities, including pollutants like SO₂, NO₂, PM2.5, SPM, and metadata such as date, location, and state.

---

## 🧪 Exploratory Data Analysis (EDA)

Performed using `week1_model_exploration.ipynb`:

- 📥 Loaded dataset using `pandas`
- 🔍 Explored structure using:
  - `.info()` – data types and non-null counts
  - `.describe()` – statistical summaries
  - `.isnull().sum()` – missing value detection
- 📊 Visualized pollutant distributions:
  - Boxplots for SO₂, NO₂, and SPM
  - Bar charts comparing average SPM across states and top locations
  - Correlation heatmap for SO₂, NO₂, and SPM
  - Time-series plot of monthly average SPM using `sampling_date`

---

## 🧠 Initial Modeling

A basic Linear Regression model was trained using SO₂ and NO₂ as input features to predict SPM. This served as a baseline for comparison with refined models in Week 2.

### 📊 Evaluation Metrics

- R² Score: **0.1055**
- MAE: **110.01 µg/m³**
- MSE: **21546.16**
- Error Percentage: **48.46%**
- Custom Accuracy (±10%): **12.96%**

> These results indicate low predictive performance, reinforcing the need for deeper feature engineering and model refinement in Week 2.

---

## 📈 Key Insights

- SO₂ and NO₂ show strong correlation with SPM, making them ideal predictors
- Pollution levels vary significantly across states and urban locations
- Seasonal trends in SPM are visible through monthly aggregation
- Data cleaning and visualization helped identify outliers and missing values
- Initial modeling highlights the limitations of raw pollutant data without contextual enrichment

---

## 🛠️ Work Done

- Selected a domain-relevant dataset for pollution drift modeling
- Cleaned and explored the data using standard EDA techniques
- Identified SO₂ and NO₂ as key features for Week 2 modeling
- Built a baseline regression model and evaluated its performance
- Structured the notebook with markdown and visual clarity
- Future-proofed time-series plots by updating deprecated resampling frequency

---

## 📁 Folder Structure

```
WEEK1/
├── notebooks/
│   └── week1_model_exploration.ipynb   # EDA and baseline modeling
├── Documentation Week1.docx            # Summary document
├── Documentation Week1.pdf             # Exported version
├── README.md                           # Summary of Week 1 work (You're here)
```

---

## 🔮 Future Work

- Refine feature selection and data cleaning in Week 2
- Train and evaluate improved regression models using SO₂ and NO₂
- Log metrics and visualizations for reviewer clarity
- Deploy the final model via Streamlit in Week 3
- Explore geospatial mapping and seasonal drift simulation

---

## 👨‍💻 Author

**Rishit Ghosh**  
🎓 B.Tech in Computer Science and Engineering (AI/ML)  
🏫 Geethanjali College of Engineering and Technology, Telangana, India  
🧠 Focused on modular design, environmental impact, and real-world applications of AI

---

## 📬 Contact

📧 [rishitghosh06@gmail.com](mailto:rishitghosh06@gmail.com)  
🔗 [GitHub Profile](https://github.com/rajghosh06-dev)
