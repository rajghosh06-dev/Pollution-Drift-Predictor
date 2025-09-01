import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import os

# Load dataset from WEEK2/data/
data_path = os.path.join("data", "data.csv")
df = pd.read_csv(data_path, encoding='ISO-8859-1', low_memory=False)

# Select features and target
# Update these column names based on your actual CSV headers
features = df[['wind_speed', 'temperature', 'humidity']]  # Example features
target = df['pollution_level']  # Target variable

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Printin results
print(f"R² Score: {r2:.4f}")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")

# Save metrics to model_metrics.md
with open("model_metrics.md", "w") as f:
    f.write("# 📊 Model Evaluation Metrics\n\n")
    f.write(f"- **R² Score**: {r2:.4f}\n")
    f.write(f"- **Mean Absolute Error (MAE)**: {mae:.2f}\n")
    f.write(f"- **Mean Squared Error (MSE)**: {mse:.2f}\n")


print("Columns in your dataset:")
print(df.columns.tolist())
