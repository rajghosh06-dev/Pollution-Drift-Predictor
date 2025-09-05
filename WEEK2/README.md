# 🌫️ Pollution Drift Predictor — Week 2

## 📌 Overview

Week 2 focuses on building a regression model to predict Suspended Particulate Matter (SPM) using SO₂ and NO₂ concentrations. This module introduces:
- Exploratory Data Analysis (EDA)
- Feature selection and transformation
- Model training and evaluation
- Visual diagnostics and saved outputs
- Modular code structure for reuse and deployment

---

## 🧠 Objectives

- Perform EDA and identify key pollutant features
- Train a Linear Regression model using scikit-learn
- Evaluate model performance using standard metrics
- Visualize prediction accuracy and error distribution
- Save model and outputs for Week 3 deployment

---

## 📁 Folder Structure

```
WEEK2/
├── train_model.py                # Model training, evaluation, and saving
├── visualisation.py              # Diagnostic plots and saved charts
├── week2_model_training.ipynb    # Final notebook submission (EDA + training)
├── model_metrics.md              # Saved evaluation metrics (R², MAE, MSE)
├── linear_regression_model.pkl   # Trained model for deployment
├── X_test.csv                    # Saved test features for reuse
├── y_test_vs_pred.csv            # Actual vs predicted SPM values
├── actual_vs_predicted.png       # Line plot of model performance
├── residuals.png                 # Histogram of prediction errors
├── scatter_so2_spm.png           # SO₂ vs SPM scatter plot (colored by NO₂)
└── README.md                     # (This file)
```

---

## 🧪 Model Training Strategy

- **Data Source**: Cleaned from `WEEK1/data/data.csv`
- **Features Used**: SO₂ and NO₂
- **Target Variable**: SPM
- **Split Ratio**: 80% training, 20% testing
- **Model Used**: Linear Regression
- **Evaluation Metrics**:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

---

## 📊 Visualizations

Generated using `matplotlib` and `seaborn`:
- 📈 Line plot: Actual vs Predicted SPM
- 📉 Residuals histogram: Error distribution
- 🎨 Scatter plot: SO₂ vs SPM (colored by NO₂)

---

## 🛠️ How to Run

1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn joblib
   ```

2. Train and save model:
   ```bash
   python train_model.py
   ```

3. Generate visualizations:
   ```bash
   python visualisation.py
   ```

---

## 📈 Results Summary

| Metric | Value (Sample Run) |
|--------|--------------------|
| R²     | 0.82               |
| MAE    | 3.45               |
| MSE    | 18.76              |

> *Note: These values may vary slightly depending on random split and data cleaning.*

---

## 🖼️ Saved Visuals

### 1. Actual vs Predicted SPM
Compares predicted SPM values against actual observations.

![Actual vs Predicted SPM](actual_vs_predicted.png)

---

### 2. Residuals Distribution
Shows the spread of prediction errors. A tight peak near zero indicates good accuracy.

![Residuals Distribution](residuals.png)

---

### 3. SO₂ vs SPM (colored by NO₂)
Visualizes pollutant interaction patterns and clustering behavior.

![SO2 vs SPM](scatter_so2_spm.png)

---

## 🔮 Next Steps & Future Enhancements

- Explore alternative models (Random Forest, XGBoost)
- Add hyperparameter tuning and cross-validation
- Integrate geospatial mapping for drift simulation
- Deploy model via Streamlit in Week 3

---

## 👨‍💻 Author

**Rishit Ghosh**  
🎓 B.Tech in Computer Science and Engineering (AI/ML)  
🏫 Geethanjali College of Engineering and Technology, Telangana  
🧠 Focused on modular design, reliable documentation, and technical clarity

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
See the `LICENSE` file for full details.
