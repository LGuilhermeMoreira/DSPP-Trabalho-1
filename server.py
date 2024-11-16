from fastapi import FastAPI
from model.sapato import Sapato
from utils.file import HandleFile

DATABASE_PATH = './db/database.csv'

handleFile = HandleFile(DATABASE_PATH)
app = FastAPI()

@app.get(path='/')
async def root(): 
    return {
        "ping":"pong"
    }