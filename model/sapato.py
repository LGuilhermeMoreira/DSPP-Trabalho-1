from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime

class Sapato(BaseModel):
    id: UUID | None = None  # Opcional, útil para PUT
    modelo: str
    tamanho: int
    cor: str
    marca: str
    created_at: str

    def __init__(self, modelo: str, tamanho: int, cor: str, marca: str, **kwargs) -> None:
        # Gera um ID automaticamente se não for fornecido
        id = kwargs.get("id", uuid4())
        created_at = datetime.now().isoformat()
        super().__init__(id=id, modelo=modelo, tamanho=tamanho, cor=cor, marca=marca, created_at=created_at)
   
