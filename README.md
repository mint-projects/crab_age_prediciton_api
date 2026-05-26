# Crab Age Prediction

![Crab Age Prediction banner](banner/crab.JPG)

FastAPI service for predicting crab age in months from crab weight measurements and sex. The model is loaded from `model/model.pkl` and exposed through a simple `/predict` endpoint.

## Overview

- Framework: FastAPI
- Model serving: `joblib`-loaded scikit-learn model
- Container: Docker
- Deployment: AWS ECS

## API

### `POST /predict`

Request body:

```json
{
  "shucked_weight": 0.3,
  "viscera_weight": 0.15,
  "shell_weight": 0.2,
  "sex": "M"
}
```

Response:

```json
{
  "age_in_months": 12.84
}
```

### Example with `curl`

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "shucked_weight": 0.3,
    "viscera_weight": 0.15,
    "shell_weight": 0.2,
    "sex": "M"
  }'
```

## Local Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd crab_age_prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn src.main:app --reload
```

Open the interactive docs at:

```text
http://127.0.0.1:8000/docs
```

## Docker

### Build locally

```bash
docker build -t crab-prediction-docker-repo .
```

### Run locally

```bash
docker run -p 8000:8000 crab-prediction-docker-repo
```

## Pull From DockerHub

If you just want to run the prebuilt image, pull it directly from DockerHub:

```bash
docker pull mtkprojectsdocker/crab-prediction-docker-repo
docker run -p 8000:8000 mtkprojectsdocker/crab-prediction-docker-repo
```

DockerHub image: [mtkprojectsdocker/crab-prediction-docker-repo](https://hub.docker.com/r/mtkprojectsdocker/crab-prediction-docker-repo)

## Deployment

This service was hosted on AWS ECS.

If you deploy your own copy, make sure the container exposes port `8000` and that the ECS task definition maps that port correctly.

## Project Structure

```text
.
├── Dockerfile
├── model/
│   └── model.pkl
├── notebook.ipynb
├── requirements.txt
└── src/
    ├── __init__.py
    └── main.py
```

## Notes

- The notebook is used for experimentation and model work.
- The API currently expects four inputs: `shucked_weight`, `viscera_weight`, `shell_weight`, and `sex`.
- The `sex` field accepts `M`, `F`, or `I`.
