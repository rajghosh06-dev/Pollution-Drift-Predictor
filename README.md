# 🌫️ Pollution Drift Predictor

An AI-powered system to forecast airborne pollution drift using environmental data such as wind speed, wind direction, humidity, and timestamp. Originally designed for construction sites, this tool has been generalized to support broader urban and industrial applications.

---

## 🎯 AIM

AI-based pollution drift forecasting using environmental data.

---

## 🚀 Project Overview

This project predicts how particulate pollution spreads across locations based on environmental conditions. It uses a simple machine learning model to forecast pollution levels and visualize drift patterns, helping support environmental monitoring and decision-making.

---

## 🧠 Features

- 📥 Modular data ingestion and preprocessing  
- 🤖 Lightweight regression model for prediction  
- 📊 Visualizations of pollution drift patterns  
- 🧪 Jupyter notebook for testing and exploration  
- 🧱 Clean folder structure for scalability and clarity  

---

## 📁 Folder Structure

```
Pollution-Drift-Predictor/
├── model_exploration.ipynb       # Main notebook for testing and analysis
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── data/
│   └── sample_inputs.csv         # Input dataset
├── src/
│   ├── drift_model.py            # Model training and prediction
│   ├── data_ingestion.py         # Data loading and preprocessing
│   └── visualizer.py             # Plotting functions
```

---

## 🧪 How It Works

1. 📂 **Load Data**  
   Pollution readings are loaded from a CSV file using `data_ingestion.py`.

2. 🧹 **Preprocess Features**  
   Wind direction is converted into numeric angles to help the model interpret directional data.

3. 🧠 **Train Model**  
   A simple Linear Regression model is trained using wind speed, humidity, and wind angle.

4. 📈 **Make Predictions**  
   The model forecasts particulate pollution levels for unseen data.

5. 🎨 **Visualize Drift**  
   Pollution drift is visualized using scatter plots colored by wind direction.

---

## 🛠️ Technologies Used

- 🐍 Python 3.11  
- 🧮 Pandas, NumPy  
- 🤖 Scikit-learn  
- 📊 Matplotlib, Seaborn  
- 🌐 Plotly (optional for interactive plots)

---

## 📦 Installation

1. 🔄 Clone the repository:
   ```bash
   git clone https://github.com/rajghosh06-dev/Pollution-Drift-Predictor.git
   ```

2. 🧪 Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. 🚀 Run the notebook:
   ```bash
   jupyter notebook model_exploration.ipynb
   ```

---

## 📈 Sample Output

- 📊 Predicted pollution levels based on wind and humidity  
- 🗺️ Visual plots showing how pollution drifts across directions  
- 📐 Model evaluation metrics (R² score, MSE)

---

## 🧑‍💻 Author

**Rishit Ghosh**  
🎓 B.Tech in Computer Science and Engineering (AI/ML)  
🏫 Geethanjali College of Engineering and Technology, Telangana  
🧠 Focused on modular design, environmental impact, and real-world applications of AI.

---

## 📬 Contact

For questions, suggestions, or collaborations:  
📧 [rishitghosh06@gmail.com](mailto:rishitghosh06@gmail.com)  
🔗 [GitHub Profile](https://github.com/rajghosh06-dev)

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
See the [LICENSE](LICENSE) file for full details.
