from fastapi import FastAPI,HTTPException
from model.sapato import Sapato
from utils.file import HandleFile
from dto.dto import CreateSapatoDto

DATABASE_PATH = './db/database.csv'

handleFile = HandleFile(DATABASE_PATH)
app = FastAPI()

@app.get(path='/')
async def root(): 
    return {
        "ping":"pong"
    }

# codigo referemte a funcionalidade 1
@app.post(path='/sapato/')
async def F1(dto: CreateSapatoDto):
    try:
        sapato = Sapato(
            modelo=dto.modelo,
            marca=dto.marca,
            tamanho=dto.tamanho,
            cor=dto.cor
        )
        response = handleFile.addSapato(sapato)
        return response
    except AttributeError as e:
        # Exceção se o DTO não tiver atributos esperados
        raise HTTPException(status_code=400, detail=f"Atributo ausente ou inválido: {e}")
    except Exception as e:
        # Captura outras exceções não esperadas
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao processar a requisição: {e}")
