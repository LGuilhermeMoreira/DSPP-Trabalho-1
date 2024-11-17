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
   

# O ideal seria criar uma seção dedicada a DTOs no projeto.
# Essa parte seria responsável por tratar o corpo das requisições.
# Haveria, por exemplo, o SapatoUpdateDTO e o SapatoCreateDTO.
# Além disso, existiria o SapatoDTO, que seria usado para tratar o retorno
# , evitando expor diretamente a entidade.