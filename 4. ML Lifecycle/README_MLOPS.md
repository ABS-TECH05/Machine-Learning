# Forest Fire Prediction - MLOps Version

This project now has:

- Flask web app
- Data versioning with DVC
- Model versioning with DVC
- Experiment tracking with MLflow
- Metrics saved in `reports/metrics.json`
- GitHub Actions CI pipeline
- Simple tests with Pytest

---

## 1. Install requirements

```bash
pip install -r requirements.txt
```

---

## 2. Run the full MLOps pipeline

```bash
dvc repro
```

This will:

1. Prepare the data
2. Train the model
3. Save the model in `models/`
4. Save metrics in `reports/metrics.json`
5. Save MLflow experiment logs in `mlruns/`

---

## 3. See metrics

```bash
dvc metrics show
```

Or open:

```text
reports/metrics.json
```

---

## 4. See MLflow experiment tracking

```bash
mlflow ui --backend-store-uri ./mlruns
```

Then open:

```text
http://127.0.0.1:5000
```

If your Flask app is already using port 5000, use:

```bash
mlflow ui --backend-store-uri ./mlruns --port 5001
```

Then open:

```text
http://127.0.0.1:5001
```

---

## 5. Run the Flask app locally

```bash
python application.py
```

Open:

```text
http://127.0.0.1:5000/predictdata
```

Health check:

```text
http://127.0.0.1:5000/health
```

---

## 6. Test API prediction

PowerShell:

```powershell
curl -Method POST "http://127.0.0.1:5000/predict" `
-H @{"Content-Type"="application/json"} `
-Body '{"Temperature":30,"RH":40,"Ws":10,"Rain":0,"FFMC":85,"DMC":20,"ISI":5,"Classes":1,"Region":1}'
```

Git Bash:

```bash
curl -X POST "http://127.0.0.1:5000/predict" \
-H "Content-Type: application/json" \
-d '{"Temperature":30,"RH":40,"Ws":10,"Rain":0,"FFMC":85,"DMC":20,"ISI":5,"Classes":1,"Region":1}'
```

---

## 7. Version your data and model

First time only:

```bash
git init
dvc init
```

Track raw data and model files:

```bash
dvc add data/raw/Algerian_forest_fires_cleaned_dataset.csv
dvc add models/ridge.pkl
dvc add models/scaler.pkl
```

Then commit DVC pointer files to Git:

```bash
git add .
git commit -m "add mlops pipeline with dvc and mlflow"
```

---

## 8. Optional: DVC remote storage

This project has a sample local DVC remote in `.dvc/config`:

```text
../dvc_storage
```

Push data/model versions there:

```bash
dvc push
```

For real cloud storage later, replace it with S3/GDrive/Azure.

Example S3:

```bash
dvc remote add -d myremote s3://your-bucket-name/path
dvc push
```

---

## 9. GitHub Actions

The file below runs the pipeline automatically when you push code:

```text
.github/workflows/mlops-ci.yml
```

It runs:

```bash
dvc repro
dvc metrics show
pytest -q
```

---

## 10. AWS Elastic Beanstalk deployment

For Beanstalk, zip the project contents and upload a new application version.

Important: zip the files inside the project folder, not the outer folder.

Your app entry point is:

```text
application.py
```

Your Procfile is:

```text
web: gunicorn application:application
```
