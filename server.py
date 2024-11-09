from fastapi import FastAPI
from model.pessoa import Pessoa

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"Ola mundo!"}


@app.get('/{test}')
async def test(test : str,parametro_opicional:str = "Nenhum Parametro"):
    return {"message query":{
        "path parameter" : test,
        "query parameter" : parametro_opicional
    }}

@app.post('/')
async def post(pessoa : Pessoa):
    return {
        "request body" :pessoa
    }