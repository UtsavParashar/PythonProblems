from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def index():
    return [{"message": "FastAPI"}, 
            {"new_msg": "Test"}]

@app.get('/hello/{name}')
async def hello(name: str):
    return {'hello': name.capitalize()}

# python -m uvicorn main:app --reload

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)