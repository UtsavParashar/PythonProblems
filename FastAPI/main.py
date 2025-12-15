from fastapi import FastAPI, Path, Query, Body
from typing import List
import uvicorn
from pydantic import BaseModel, Field
app = FastAPI()


class Student(BaseModel):
    id: int
    name: str = Field(None, title='name of the student', max_length=10)
    subjects: List[str] = []


@app.post('/students/')
async def student_data(name: str = Body(...),
                       marks: int = Body(...)):
    return {"name": name,
            "marks": marks}

@app.post('/students/{college}')
async def student_coll_data(college: str,
                            age: int,
                            student: Student):
    retval = {"college": college,
              "age": age,
              **student.model_dump()}
    return retval


# python -m uvicorn main:app --reload

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)