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
- 🧱 Streamlit interface for real-time prediction  
- 🗂️ Week-wise folder structure for clarity and progression  

---

## 📁 Folder Structure

```
Pollution-Drift-Predictor/
├── WEEK1/                         # Dataset selection, problem definition, preprocessing
│   ├── pollution_data.csv
│   ├── preprocessing_notebook.ipynb
│   └── README.md
│
├── WEEK2/                         # Model training, evaluation, and visualization
│   ├── train_model.py
│   ├── visualization.py
│   ├── model_metrics.md
│   ├── linear_regression_model.pkl
│   └── README.md
│
├── WEEK3/                         # Streamlit deployment and prediction interface
│   ├── streamlit_app.py
│   ├── prediction.csv (optional)
│   └── README.md
│
├── WEEK4/                         # Final presentation and documentation
│   ├── PollutionDrift_PPT.pptx
│   └── README.md
│
├── LICENSE                        # MIT License
├── requirements.txt               # Python dependencies
└── README.md                      # Project overview (this file)
```

---

## 🧪 How It Works

1. 📂 **Load Data**  
   Pollution readings are loaded from a CSV file and cleaned using Pandas.

2. 🧹 **Preprocess Features**  
   Wind direction is converted into numeric angles to help the model interpret directional data.

3. 🧠 **Train Model**  
   A Linear Regression model is trained using wind speed, humidity, and wind angle.

4. 📈 **Make Predictions**  
   The model forecasts particulate pollution levels for unseen data.

5. 🎨 **Visualize Drift**  
   Pollution drift is visualized using scatter plots and bar charts.

6. 🖥️ **Deploy Interface**  
   A Streamlit app allows users to input SO₂ and NO₂ levels and receive real-time SPM predictions.

---

## 🛠️ Technologies Used

- 🐍 Python 3.11  
- 🧮 Pandas, NumPy  
- 🤖 Scikit-learn  
- 📊 Matplotlib, Seaborn  
- 🌐 Streamlit  
- 📈 Plotly (optional)

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

4. 🚀 Run the Streamlit app:
   ```bash
   streamlit run WEEK3/streamlit_app.py
   ```

---

## 📈 Sample Output

- 📊 Predicted SPM levels based on SO₂ and NO₂ inputs  
- 🛑 Pollution risk interpretation (Safe, Moderate, Unhealthy, Hazardous)  
- 📉 Bar chart comparing input pollutants vs predicted SPM  
- 📥 Downloadable CSV of prediction results

---

## 🧑‍💻 Author

**Rishit Ghosh**  
🎓 B.Tech in Computer Science and Engineering (AI/ML)  
🏫 Geethanjali College of Engineering and Technology, Telangana, Hyderabad, INDIA  
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
