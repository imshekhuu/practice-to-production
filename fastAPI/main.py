from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import computed_field, BaseModel, Field
from fastapi.responses import JSONResponse
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='enter you name')]
    city: Annotated[str, Field(..., description='enter your city name')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='enter the patient age')]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description='enter the gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='enter the height of the patient')]
    weight: Annotated[float, Field(..., gt=0, description='enter the weight of the patient')]

@computed_field
@property
def bmi(self) -> float:
    bmi = round(self.weight/(self.height**2),2)
    return bmi

@computed_field
@property
def verdict(self) -> str:
    if self.weight < 18.5:
        return 'underweight'
    elif self.weight < 30:
        return 'normal'
    else:
        return 'Obese'

def load_data():
    with open("patients.json", 'r') as file:
        data = json.load(file)

    return data

def save_data(data):
    with open("patients.json", 'w') as file:
        json.dump(data, file)


@app.get("/")
def hello():
    return{'massage':'Patient Management System APi'}

@app.get("/about")
def about():
    return{'massage': 'A Fully Functional API to Manage System'}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description = 'ID of the patients in the DB ', example = 'P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient not found')

@app.get("/sort")
def sort_patient(
    sort_by: str = Query(..., description="height, weight or bmi"),
    order: str = Query("asc", description="asc or desc")
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Choose from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or desc"
        )

    data = load_data()
    reverse = True if order == "desc" else False

    return sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse
    )

@app.post('/create')
def create_patient(Patient: Patient):

    data = load_data()
    if Patient.id in data:
        raise HTTPException(status_code=400, detail='patient already exists')
    
    data[Patient.id] =  Patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201, content={'massage': 'patient created succesfully✅'})