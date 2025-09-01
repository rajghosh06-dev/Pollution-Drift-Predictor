import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('../data/pollution_data.csv')

# Features and target
X = df[['wind_speed', 'temperature', 'humidity']]
y = df['pollution_level']

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
plt.title('Actual vs Predicted Pollution Levels')
plt.xlabel('Sample Index')
plt.ylabel('Pollution Level')
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

# Scatter plot: Wind Speed vs Pollution Level
sns.scatterplot(x=df['wind_speed'], y=df['pollution_level'], hue=df['temperature'], palette='coolwarm')
plt.title('Wind Speed vs Pollution Level')
plt.xlabel('Wind Speed')
plt.ylabel('Pollution Level')
plt.tight_layout()
plt.savefig('scatter_wind_pollution.png')
plt.show()