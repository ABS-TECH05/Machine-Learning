install:
	pip install -r requirements.txt

repro:
	dvc repro

metrics:
	dvc metrics show

mlflow:
	mlflow ui --backend-store-uri ./mlruns

run:
	python application.py

test:
	pytest -q
