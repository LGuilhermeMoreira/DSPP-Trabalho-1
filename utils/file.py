from model.sapato import Sapato
from uuid import UUID
import csv
import os
from dto.dto import UpdateSapatoDto
import zipfile
from typing import Optional

class HandleFile():
    path : str

    def __init__(self,path : str) -> None:
        self.path = path
        self.createFile()

    def createFile(self) -> None:
        # configurando os campos no csv
        if not os.path.exists(self.path) or os.path.getsize(self.path) == 0:
            dados = ["id", "modelo", "tamanho", "cor", "marca", "created_at"]
            with open(self.path, mode='w', newline='', encoding='utf-8') as arquivo:
                fileWriter = csv.writer(arquivo)
                fileWriter.writerow(dados)
    
    def addSapato(self,sapato : Sapato) -> Sapato:
        dados = [sapato.id,sapato.modelo,sapato.tamanho,sapato.cor,sapato.marca,sapato.created_at]
        with open(self.path,mode='a',newline='',encoding='utf-8') as arquivo:
            fileWriter = csv.writer(arquivo)
            fileWriter.writerow(dados)
        return sapato

    def getSapatos(self) -> list:
        dados = []
        with open(self.path, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                dados.append({
                    'id': linha['id'],
                    'modelo': linha['modelo'],
                    'tamanho': linha['tamanho'],
                    'cor': linha['cor'],
                    'marca': linha['marca'],
                    'created_at': linha['created_at'],
                })
        return dados
        

    def getSapatoById(self, id : UUID) -> dict:
        with open(self.path, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
               if linha['id'] == str(id):
                   return linha

    def updateSapato(self,id : UUID,sapato : UpdateSapatoDto) -> None:
        dados = []
        with open(self.path, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha['id'] == str(id):
                    linha['modelo'] = sapato.modelo
                    linha['tamanho'] = sapato.tamanho
                    linha['cor'] = sapato.cor
                    linha['marca'] = sapato.marca
                dados.append(linha)
        with open(self.path, mode='w', newline='', encoding='utf-8') as arquivo:
            fileWriter = csv.DictWriter(arquivo, fieldnames=['id', 'modelo', 'tamanho', 'cor', 'marca', 'created_at'])
            fileWriter.writeheader()
            fileWriter.writerows(dados)

    def deleteSapato(self,id : UUID) -> None:
        dados = []
        with open(self.path, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha['id'] != str(id):
                    dados.append(linha)
        with open(self.path, mode='w', newline='', encoding='utf-8') as arquivo:
            fileWriter = csv.DictWriter(arquivo, fieldnames=['id', 'modelo', 'tamanho', 'cor', 'marca', 'created_at'])
            fileWriter.writeheader()
            fileWriter.writerows(dados)

    def createZip(self, zip_path: str) -> str:

        if not os.path.exists(self.path):
            raise FileNotFoundError("Arquivo CSV não encontrado.")

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(self.path, arcname=os.path.basename(self.path))
        
        return zip_path

    def filterSapatos(
        self,
        modelo: Optional[str] = None,
        tamanho: Optional[str] = None,
        cor: Optional[str] = None,
        marca: Optional[str] = None,
    ) -> list:
        
        sapatos = self.getSapatos()
        
        if modelo:
            sapatos = [s for s in sapatos if s['modelo'].lower() == modelo.lower()]
        if tamanho:
            sapatos = [s for s in sapatos if s['tamanho'].lower() == cor.lower()]
        if cor:
            sapatos = [s for s in sapatos if s['cor'].lower() == cor.lower()]
        if marca:
            sapatos = [s for s in sapatos if s['marca'].lower() == marca.lower()]

        return sapatos