from pydantic import BaseModel

class Disease(BaseModel):
    name: str
    description: str