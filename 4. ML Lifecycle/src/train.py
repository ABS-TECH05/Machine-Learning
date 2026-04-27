import argparse
import json
import os
import pickle

import pandas as pd
import yaml
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


FEATURES = ["Temperature", "RH", "Ws", "Rain", "FFMC", "DMC", "ISI", "Classes", "Region"]


def train(params_path: str = "params.yaml") -> None:
    with open(params_path, "r") as f:
        params = yaml.safe_load(f)

    data_path = params["data"]["processed_path"]
    target = params["data"]["target"]
    test_size = params["data"]["test_size"]
    random_state = params["data"]["random_state"]
    alpha = params["model"]["alpha"]

    df = pd.read_csv(data_path)
    X = df[FEATURES]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = Ridge(alpha=alpha)
    model.fit(X_train_scaled, y_train)

    preds = model.predict(X_test_scaled)

    metrics = {
        "r2_score": float(r2_score(y_test, preds)),
        "mae": float(mean_absolute_error(y_test, preds)),
        "mse": float(mean_squared_error(y_test, preds)),
        "rmse": float(mean_squared_error(y_test, preds) ** 0.5),
        "train_rows": int(X_train.shape[0]),
        "test_rows": int(X_test.shape[0]),
        "features": FEATURES,
    }

    os.makedirs("models", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    with open("models/ridge.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    with open("reports/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("Training complete.")
    print(json.dumps(metrics, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", default="params.yaml")
    args = parser.parse_args()
    train(args.params)
