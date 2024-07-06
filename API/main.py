from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def getReady():
    return {"hello":"world"}

@app.get('/test')
def getTest():
    return {"teste de rota":"rota teste"}

getTest()