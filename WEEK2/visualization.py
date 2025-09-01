import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

# Load dataset
data_path = os.path.join("data", "data.csv")
df = pd.read_csv(data_path, encoding='ISO-8859-1', low_memory=False)

# Clean and select relevant columns
df = df[['so2', 'no2', 'spm']].dropna()

# Features and target
X = df[['so2', 'no2']]
y = df['spm']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

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
sns.scatterplot(x=df['so2'], y=df['spm'], hue=df['no2'], palette='coolwarm')
plt.title('SO2 vs SPM (colored by NO2)')
plt.xlabel('SO2')
plt.ylabel('SPM')
plt.tight_layout()
plt.savefig('scatter_so2_spm.png')
plt.show()
