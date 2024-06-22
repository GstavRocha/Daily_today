from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def checkApi():
    return {'hello': 'world'}