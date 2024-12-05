from datetime import date
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    dob: date


user = User(id='1', name='John Doe', dob=[1, 2])
print(user)
