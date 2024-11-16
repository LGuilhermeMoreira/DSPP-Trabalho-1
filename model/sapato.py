from pydantic import BaseModel

class Sapato(BaseModel):
    id : int | None = None #opicional para rota de put
    modelo : str
    tamanho : int
    cor : int
    marca : str
    created_at : str

# O ideal seria criar uma seção dedicada a DTOs no projeto.
# Essa parte seria responsável por tratar o corpo das requisições.
# Haveria, por exemplo, o SapatoUpdateDTO e o SapatoCreateDTO.
# Além disso, existiria o SapatoDTO, que seria usado para tratar o retorno
# , evitando expor diretamente a entidade.