from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="name of the patient")]
    email: EmailStr
    url: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)]
    height: int
    married: Optional[bool] = None
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/self.height**2, 2)
        return bmi

  
    @model_validator(mode="wrap")
    def validate_emergency_contact(cls, values, handler):
        model = handler(values)

        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError(
                "Patients older than 60 must have an emergency contact number"
            )

        return model

  
    @field_validator("email")
    @classmethod
    def mail_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        domain = value.split("@")[-1].lower()

        if domain not in valid_domains:
            raise ValueError("Invalid email domain")

        return value

 
    @field_validator("name")
    @classmethod
    def name_validator(cls, value):
        return value.upper()

   
    @field_validator("age")
    @classmethod
    def age_validator(cls, value):
        if not (0 < value < 100):
            raise ValueError("age should be in range 1–99")

        return value



def print_patient_data(p: Patient, action: str):
    print("Name           :", p.name)
    print("Age            :", p.age)
    print("Weight         :", p.weight)
    print("bmi            :", p.bmi)
    print("Married        :", p.married)
    print("Allergies      :", p.allergies)
    print("Contact Details:", p.contact_details)
    print("Action         :", action)
    print("-----------------------------------------")


def insert_patient_data(p: Patient):
    print_patient_data(p, "inserted")


def update_patient_data(p: Patient):
    print_patient_data(p, "updated")



patient_info = {
    "name": "divy",
    "email": "hello@hdfc.com",
    "url": "https://chatgpt.com",
    "age": 65,
    "weight": 75.3,
    'height': 103,
    # "married": True,
    # "allergies": ["pollen", "dust"],
    "contact_details": {
        "email": "helloworld12@hdfc.com",
        "phone": "243243585",
        # Add this only if age > 60:
        "emergency": "1234567890"
    }
}


p1 = Patient(**patient_info)
p2 = Patient(**patient_info)

insert_patient_data(p1)
update_patient_data(p2)
