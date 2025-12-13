from typing import List
from pydantic import BaseModel, Field

class Student(BaseModel):
    id: int
    name: str = Field(None, title="The description of the item", max_length=10)
    subjects: List[str] = []

data = {
    'id': 1,
    'name': 'RameshSInghparmar',
    'subjects': ['Maths', 'Accounting']
}

s1 = Student(**data)
print(f's1 - {s1}')
print(f's1 dict - {s1.model_dump()}')