from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained Elastic Net model
model = joblib.load("elastic_net_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            # Get user input
            income = float(request.form["income"])
            age = float(request.form["age"])
            rooms = float(request.form["rooms"])
            bedrooms = float(request.form["bedrooms"])
            population = float(request.form["population"])

            # Prepare features
            features = np.array([[income, age, rooms, bedrooms, population]])

            # Predict price
            prediction = model.predict(features)[0]
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
