# VISUALIZATION & DIAGNOSTICS
#(diagonistics only)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load saved model and test data
model = joblib.load("linear_regression_model.pkl")
X_test = pd.read_csv("X_test.csv")
y_test_vs_pred = pd.read_csv("y_test_vs_pred.csv")

y_test = y_test_vs_pred["Actual"]
y_pred = y_test_vs_pred["Predicted"]

# Line plot: Actual vs Predicted
plt.figure(figsize=(10, 5))
plt.plot(y_test.values, label='Actual', color='blue')
plt.plot(y_pred, label='Predicted', color='red')
plt.title('Actual vs Predicted SPM Levels')
plt.xlabel('Sample Index')
plt.ylabel('SPM')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('actual_vs_predicted.png')
plt.show()

# Residual plot
residuals = y_test - y_pred
sns.histplot(residuals, kde=True, color='purple')
plt.title('Residuals Distribution')
plt.xlabel('Error')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('residuals.png')
plt.show()

# Scatter plot: SO2 vs SPM with NO2 as hue
df = pd.read_csv("data/data.csv", encoding='ISO-8859-1', low_memory=False)
df = df[['so2', 'no2', 'spm']].dropna()
sns.scatterplot(x=df['so2'], y=df['spm'], hue=df['no2'], palette='coolwarm')
plt.title('SO2 vs SPM (colored by NO2)')
plt.xlabel('SO2')
plt.ylabel('SPM')
plt.tight_layout()
plt.savefig('scatter_so2_spm.png')
plt.show()

