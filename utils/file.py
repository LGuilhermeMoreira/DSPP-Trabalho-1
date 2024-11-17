from model.sapato import Sapato
import csv
import os

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

    def getSapatos(self):
        pass

    def getSapatoById(self, id : int):
        pass

    def updateSapato(self,id : int,sapato : Sapato):
        pass