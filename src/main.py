from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from typing import Literal
import joblib


class crab_request(BaseModel):
    shucked_weight: float
    viscera_weight: float
    shell_weight: float
    sex: Literal["M", "F", "I"]


app = FastAPI()


@app.post("/predict")
async def root(data: crab_request):
    model_path = Path(__file__).resolve().parent.parent / "model" / "model.pkl"
    loaded_model = joblib.load(model_path)

    total_weight = data.shucked_weight + data.viscera_weight + data.shell_weight

    if data.sex == "F":
        sex = [1, 0, 0]
    elif data.sex == "I":
        sex = [0, 1, 0]
    else:
        sex = [0, 0, 1]
    test_data = [
        [
            total_weight,
            data.shucked_weight,
            data.viscera_weight,
            data.shell_weight,
            *sex,
        ]
    ]

    age_pred = loaded_model.predict(test_data)

    return {"age_in_months": round(float(age_pred[0]), 2)}
