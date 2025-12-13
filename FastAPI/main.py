from fastapi import FastAPI, Path, Query
import uvicorn
app = FastAPI()

@app.get("/")
async def index():
    return [{"message": "FastAPI"}, 
            {"new_msg": "Test"}]

@app.get('/hello/{name}/{age}')
async def hello(*, name:str=Path(..., min_length=3, max_length=10),
                age:int=Path(..., gt=10, le=100),
                percent: float=Query(..., ge=0, le=100)):
    return {'hello': name.capitalize(),
            'aged persons': age,
            'secured pecentage': percent}

# python -m uvicorn main:app --reload

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)