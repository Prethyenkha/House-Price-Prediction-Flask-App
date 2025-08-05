# 🏠 House Price Prediction

Welcome to the **House Price Prediction Web App**!  
This project leverages advanced machine learning—**Elastic Net Regression**—and a modern web interface to predict California house prices using features like *income, house age, number of rooms, bedrooms, and population*.

---

## 🚀 Features

- 🎯 **Elastic Net Regression** with automated hyperparameter tuning for top-tier accuracy
- 🌐 **Intuitive Web Interface:** Enter housing features and get instant predictions
- ⚡ **Lightning-fast Results:** Predicted price displayed instantly after submission
- 💎 **Modern & Responsive UI:** Crafted with sleek HTML & CSS for seamless user experience
- 🔥 **Plug-and-play:** Ready-to-run Flask application—no extra setup needed!

---

## 🏗️ Project Structure

```
ElasticNetApp/
│── app.py                  # Flask app with prediction logic
│── elastic_net_model.pkl   # Pre-trained Elastic Net model (joblib format)
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
│
├── templates/
│     └── index.html        # Main webpage template
│
└── static/
      └── style.css         # Custom styling
│
└── model.ipynb             # Jupyter notebook for data analysis and model training
```

---

## 🔧 Installation & Usage

1. **Clone the repository or download the project folder:**
   ```bash
   git clone https://github.com/Prethyenkha/House-Price-Prediction-Flask-App.git
   cd House-Price-Prediction-Flask-App/ElasticNetApp
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Flask app:**
   ```bash
   python app.py
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000).

---

## 📦 Dependencies

- `Flask` - web framework
- `scikit-learn` - Elastic Net Regression
- `joblib` - Model serialization
- `numpy`, `pandas` - Data handling
- See `requirements.txt` for details

---

## 🧠 How It Works

1. **Model Training:**  
   The Elastic Net Regression model is trained (see `model.ipynb`) with California housing data and saved using `joblib`.

2. **Web Interface:**  
   Users input house features via the simple UI.

3. **Prediction:**  
   The Flask app loads the trained model and predicts the house price instantly.

---
## 🖼️ App Preview

<img width="1344" height="624" alt="Screenshot 2025-08-05 142358" src="https://github.com/user-attachments/assets/3aabd9e5-da64-4c10-91ac-4ead3df109b9" />

