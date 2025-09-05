# 🌿 Week 1 – Pollution Drift Predictor (Environmental Monitoring & Pollution Control)

## 📌 Project Theme

This project falls under the theme of **Environmental Monitoring & Pollution Control**, focusing on the prediction and analysis of airborne pollution drift using environmental data. Week 1 lays the foundation by exploring pollutant patterns across Indian cities.

---

## 🎯 Objective

To explore and understand a real-world dataset related to air pollution, perform detailed exploratory data analysis (EDA), and identify key features for building a predictive model in Week 2.

---

## 📦 Dataset Used

- **Source:** Kaggle – [Air Pollution Analysis and Prediction](https://www.kaggle.com/code/guidosalimbeni/air-pollution-analysis-and-prediction)
- **File:** `data.csv`
- **Size:** ~62 MB
- **Description:** Historical daily ambient air quality data across multiple Indian cities, including pollutants like SO₂, NO₂, PM2.5, SPM, and metadata such as date, location, and state.

---

## 🧪 Exploratory Data Analysis (EDA)

Performed using `week1_analysis.ipynb`:

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

## 📈 Key Insights

- SO₂ and NO₂ show strong correlation with SPM, making them ideal predictors
- Pollution levels vary significantly across states and urban locations
- Seasonal trends in SPM are visible through monthly aggregation
- Data cleaning and visualization helped identify outliers and missing values

---

## 🛠️ Work Done

- Selected a domain-relevant dataset for pollution drift modeling
- Cleaned and explored the data using standard EDA techniques
- Identified SO₂ and NO₂ as key features for Week 2 modeling
- Structured the notebook with markdown and visual clarity
- Future-proofed time-series plots by updating deprecated resampling frequency

---

## 📁 Folder Structure

```
WEEK1/
├── week1_analysis.ipynb       # Jupyter notebook with EDA and visualizations
├── data.csv                   # Kaggle dataset used
├── README.md                  # Summary of Week 1 work (You're here)
```

---

## 🔮 Future Work

- Use SO₂ and NO₂ as input features for regression modeling in Week 2
- Train and evaluate a pollution prediction model
- Deploy the model via Streamlit in Week 3
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
