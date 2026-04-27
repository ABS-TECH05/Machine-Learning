import os
import pickle

import numpy as np
from flask import Flask, request, render_template


application = Flask(__name__)
app = application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_pickle(*possible_paths):
    for path in possible_paths:
        full_path = os.path.join(BASE_DIR, path)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return pickle.load(f)
    raise FileNotFoundError(f"Could not find any of these files: {possible_paths}")


ridge_model = load_pickle("models/ridge.pkl", "ridge.pkl")
standard_scaler = load_pickle("models/scaler.pkl", "scaler.pkl")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json(force=True)

    features = np.array([[
        float(data["Temperature"]),
        float(data["RH"]),
        float(data["Ws"]),
        float(data["Rain"]),
        float(data["FFMC"]),
        float(data["DMC"]),
        float(data["ISI"]),
        float(data["Classes"]),
        float(data["Region"]),
    ]])

    scaled = standard_scaler.transform(features)
    prediction = ridge_model.predict(scaled)[0]
    return {"prediction": float(prediction)}


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        features = np.array([[
            float(request.form.get("Temperature")),
            float(request.form.get("RH")),
            float(request.form.get("Ws")),
            float(request.form.get("Rain")),
            float(request.form.get("FFMC")),
            float(request.form.get("DMC")),
            float(request.form.get("ISI")),
            float(request.form.get("Classes")),
            float(request.form.get("Region")),
        ]])

        scaled = standard_scaler.transform(features)
        result = ridge_model.predict(scaled)[0]
        return render_template("home.html", results=result)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
