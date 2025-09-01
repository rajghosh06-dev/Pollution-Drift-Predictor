# 🌍 Pollution Drift Predictor — Week 2

## 📌 Overview
This module builds upon Week 1 by introducing a proper machine learning workflow to predict pollution drift patterns. It includes:
- Data splitting (80% training, 20% testing)
- Model training and evaluation
- Enhanced visualizations for drift behavior
- Modular code structure for scalability

---

## 🧠 Objectives
- Implement a regression model to predict pollution drift
- Evaluate model performance using standard metrics
- Visualize pollution intensity and drift direction
- Refactor code for clarity and modularity

---

## 📁 Folder Structure

```
Week2/
├── train_model.py         # Model training and evaluation logic
├── visualization.py       # Graphs and plots for drift analysis
├── model_metrics.md       # Metric interpretations and results
├── README.md              # This file
```

## 🧪 Model Training Strategy

- **Data Split**: 80% training, 20% testing using `train_test_split`
- **Model Used**: Linear Regression (initial baseline)
- **Metrics Evaluated**:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

---

## 📊 Visualizations

Implemented using `matplotlib`, `seaborn`, and `plotly`:
- Line plot: Predicted vs Actual pollution levels
- Scatter plot: Drift direction vs pollution intensity
- Heatmap: Regional pollution concentration
- Residual plot: Error distribution

---

## 🛠️ How to Run

1. Ensure dependencies are installed:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn plotly
   ```

2. Run training:
   ```bash
   python train_model.py
   ```

3. Generate visualizations:
   ```bash
   python visualization.py
   ```

---

## 📈 Results Summary

| Metric | Value |
|--------|-------|
| R²     | 0.82  |
| MAE    | 3.45  |
| MSE    | 18.76 |

> *Note: These values are based on initial runs and may improve with tuning.*

---

## 🔮 Next Steps
- Try alternative models (Random Forest, XGBoost)
- Add hyperparameter tuning
- Integrate geospatial mapping for drift simulation
- Save trained model for deployment

---

## 👨‍💻 Author
Rishit Ghosh
Geethanjali College of Engineering and Technology, Cheeriyal, Telangana, India
- focused on modular design, reliable documentation, and technical clarity.

---

## 📄 License
MIT License
