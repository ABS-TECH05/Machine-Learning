# Forest Fire Prediction - MLOps Version

This version adds a clean MLOps structure to your existing Flask project.

## What was added

- Data versioning with DVC
- Model versioning with DVC
- Reproducible training pipeline using `dvc.yaml`
- `params.yaml` for model parameters
- `reports/metrics.json` for model metrics
- Cleaner folder structure
- `/health` endpoint
- `/predict` JSON API endpoint
- AWS Elastic Beanstalk compatible `Procfile`

## Project structure

```text
.
├── application.py
├── requirements.txt
├── Procfile
├── params.yaml
├── dvc.yaml
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── reports/
├── src/
│   ├── prepare_data.py
│   └── train.py
├── templates/
├── notebooks/
└── legacy/
```

## First-time setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Initialize Git and DVC

```bash
git init
dvc init
```

## Track data and model files with DVC

```bash
dvc add data/raw/Algerian_forest_fires_cleaned_dataset.csv
dvc add data/raw/Algerian_forest_fires_dataset_UPDATE.csv
dvc add models/ridge.pkl
dvc add models/scaler.pkl
```

Then commit the small tracking files to Git:

```bash
git add .
git commit -m "Add MLOps structure with DVC versioning"
```

## Reproduce the ML pipeline

```bash
dvc repro
```

This runs:

1. `src/prepare_data.py`
2. `src/train.py`
3. saves updated models in `models/`
4. saves metrics in `reports/metrics.json`

## View metrics

```bash
dvc metrics show
```

## Change model version

Edit `params.yaml`, for example:

```yaml
model:
  alpha: 0.5
```

Then run:

```bash
dvc repro
git add params.yaml dvc.lock reports/metrics.json
git commit -m "Tune ridge alpha"
```

## Optional: Add S3 remote for real cloud model/data versioning

Create an S3 bucket first, then:

```bash
dvc remote add -d storage s3://YOUR-BUCKET-NAME/forest-fire-dvc
dvc push
git add .dvc/config
git commit -m "Add DVC S3 remote"
```

Later, on another system:

```bash
git clone YOUR_REPO_URL
cd YOUR_REPO
pip install -r requirements.txt
dvc pull
```

## Run locally

```bash
python application.py
```

Open:

```text
http://127.0.0.1:5000/predictdata
```

## Test JSON API

```bash
curl -X POST http://127.0.0.1:5000/predict ^
-H "Content-Type: application/json" ^
-d "{\"Temperature\":29,\"RH\":57,\"Ws\":18,\"Rain\":0,\"FFMC\":65.7,\"DMC\":3.4,\"ISI\":1.3,\"Classes\":0,\"Region\":0}"
```

## AWS Elastic Beanstalk redeploy

After testing locally, zip the project files and upload the new zip to Elastic Beanstalk.

Do not zip the outer folder. Zip the contents inside the project folder.

For Windows PowerShell:

```powershell
Compress-Archive -Path * -DestinationPath forest-fire-mlops.zip -Force
```

Then upload `forest-fire-mlops.zip` to Elastic Beanstalk as a new application version.
