from model.sapato import Sapato

class HandleFile():
    path : str

    def __init__(self,path : str) -> None:
        self.createFile(path=path)

    def createFile(self,path):
        pass

    def addSapato(self,sapato : Sapato):
        pass

    def getSapatos(self):
        pass

    def getSapatoById(self, id : int):
        pass

    def updateSapato(self,id : int,sapato : Sapato):
        pass