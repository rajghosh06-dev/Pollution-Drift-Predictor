# src/drift_model.py

def train_model(X, y):
    """
    Trains a simple linear regression model.
    Inputs:
        X - Features (wind_speed, humidity, wind_angle)
        y - Target (particulate_level)
    Returns:
        model - Trained model
    """
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)
    return model

def make_predictions(model, X_test):
    """
    Uses the trained model to predict particulate levels.
    Inputs:
        model - Trained model
        X_test - Test features
    Returns:
        predictions - Predicted values
    """
    return model.predict(X_test)
