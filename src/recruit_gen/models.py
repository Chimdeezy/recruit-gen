from pydantic import BaseModel, Field

class Recruit(BaseModel):
    height: int = Field(gt=0)   # inches
    weight: int = Field(gt=0)   # lbs
