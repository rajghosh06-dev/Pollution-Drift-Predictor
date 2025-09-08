# just a testing file, CONSIDER using app_streamlit.py instead

from flask import Flask, request, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load("../WEEK2/linear_regression_model.pkl")

HTML = """
<!doctype html>
<title>Pollution Drift Predictor</title>
<h2>Enter SO₂ and NO₂ levels to predict SPM</h2>
<form method="POST">
  SO₂: <input type="number" name="so2" step="0.1"><br><br>
  NO₂: <input type="number" name="no2" step="0.1"><br><br>
  <input type="submit" value="Predict">
</form>
{% if prediction %}
  <h3>Predicted SPM: {{ prediction }} µg/m³</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        so2 = float(request.form["so2"])
        no2 = float(request.form["no2"])
        prediction = round(model.predict([[so2, no2]])[0], 2)
    return render_template_string(HTML, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

# To run the app, use the command: python app_flask.py
