# python -m uvicorn server:app --reload

from datetime import datetime
from fastapi import FastAPI,HTTPException,Request,Query
from model.sapato import Sapato
from utils.file import HandleFile
from dto.dto import CreateSapatoDto,UpdateSapatoDto
from utils.log import LogSystem,read_config
from fastapi.responses import FileResponse
from typing import Optional


DATABASE_PATH = './db/database.csv'
YAML_PATH = './config.yml'
ZIP_PATH = './db/produtos.zip'

config = read_config(YAML_PATH)
log_config = config["logging"]

handleFile = HandleFile(DATABASE_PATH)
handleLog = LogSystem(
    level=log_config["level"],
    log_file=log_config["file"],
    format=log_config["format"],
)
app = FastAPI()

@app.middleware('http')
async def F8(request: Request, call_next):
    start_time = datetime.now()  
    response = await call_next(request)  
    duration = (datetime.now() - start_time).total_seconds() 

    if 400 <= response.status_code < 500:
        log_level = "ERROR"
    elif response.status_code >= 500:
        log_level = "CRITICAL"
    else:
        log_level = "INFO"

    handleLog.add_log(
        f"{request.method} {request.url} | Status: {response.status_code} | Duration: {duration:.2f}s",
        level=log_level,
    )
    return response

@app.get(path='/')
async def root(): 
    return {
        "ping":"pong"
    }

# codigo referemte a funcionalidade 1
@app.post(path='/sapato/',status_code=201)
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
        raise HTTPException(status_code=400,  detail=f"Atributo ausente ou inválido: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao processar a requisição: {e}")

@app.get(path='/sapato/',status_code=200)
async def F2():
    try:
        response = handleFile.getSapatos()
        return response
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Ocorreu um erro no servidor: {e}')
    
@app.get(path='/sapato/{id}/',status_code=200)
async def F2_getById(id):
    try:
        response = handleFile.getSapatoById(id)
        if response is None:
            raise HTTPException(status_code=404,detail=f'id não encontrado')
        return response
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Ocorreu um erro no servidor: {e}')
    
@app.put(path='/sapato/{id}',status_code=200)
async def F3_update(id,body : UpdateSapatoDto):
    try:
        response = handleFile.updateSapato(id,body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Ocorreu um erro no servidor: {e}')

@app.delete(path='/sapato/{id}',status_code=200)
async def F3_delete(id):
    try:
        response = handleFile.deleteSapato(id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500,detail=f'Ocorreu um erro no servidor: {e}')
    

@app.get(path='/sapato/len',status_code=200)
async def F4():
    try:
        response = handleFile.getLenAllEntity()
        return response
    except Exception as e:    
        raise HTTPException(status_code=500,detail=f'Ocorreu um erro no servidor: {e}')
    
@app.get(path='/sapato/hash',status_code=200)
async def F7():
    try:
        response = handleFile.getHashFile()
        return response
    except Exception as e:    
        raise HTTPException(status_code=500,detail=f'Ocorreu um erro no servidor: {e}')
    

@app.get(path='/sapato/download-zip', status_code=200)
async def download_csv_zip():
    try:
        zip_path = './db/produtos.zip'
        handleFile.createZip(zip_path)
        return FileResponse(
            path=zip_path,
            filename='produtos.zip',
            media_type='application/zip'
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao gerar o arquivo ZIP: {e}")

@app.get(path='/sapato/filter', status_code=200)
async def filter_sapatos(
    modelo: Optional[str] = None,
    tamanho: Optional[int] = Query(None, alias="tamanho"),
    cor: Optional[str] = None,
    marca: Optional[str] = None
):
    try:
        response = handleFile.filterSapatos(
            modelo=modelo,
            tamanho=tamanho,
            cor=cor,
            marca=marca
        )
        if not response:
            raise HTTPException(status_code=404, detail="Nenhum sapato encontrado com os critérios fornecidos.")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro no servidor: {e}")

