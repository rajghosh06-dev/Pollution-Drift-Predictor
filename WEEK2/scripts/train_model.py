# MODEL TRAINING & METRICS
# (Train + preprocess + evaluate + save)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os

# Load and clean dataset
data_path = os.path.join("data", "data.csv")
df = pd.read_csv(data_path, encoding='ISO-8859-1', low_memory=False)
df = df[['so2', 'no2', 'spm']].dropna()

# Define features and target
X = df[['so2', 'no2']]
y = df['spm']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing: StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit + transform
X_test_scaled = scaler.transform(X_test)        # only transform

# Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Print metrics
print("Model trained successfully")
print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")

# Save metrics
with open("model_metrics.md", "w") as f:
    f.write("#Model Evaluation Metrics\n\n")
    f.write(f"- **R² Score**: {r2:.4f}\n")
    f.write(f"- **Mean Absolute Error (MAE)**: {mae:.2f}\n")
    f.write(f"- **Mean Squared Error (MSE)**: {mse:.2f}\n")

# Save model and scaler
joblib.dump(model, "linear_regression_model.pkl")
joblib.dump(scaler, "scaler.pkl")

# Save test data and predictions
X_test.to_csv("X_test.csv", index=False)
pd.DataFrame({"Actual": y_test, "Predicted": y_pred}).to_csv("y_test_vs_pred.csv", index=False)

