from pydantic import BaseModel

class Case(BaseModel):
    num_claims: int
    guilty: str
    victim: str
