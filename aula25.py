# PRACTICE - PYTHON 024"
# POO - P2 / Herança

class NPC: #class Pai
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
        
    def info(self):
        print("Nome: " + self.nome)
        print("Time: " + str(self.time))
        print("Forca: " + str(self.forca))
        print("Municao: " + self.municao))
        print("Vivo: " + ("sim" if self.vivo else "nao"))
        print("Energia: " + str(self.energia))
        print("-------------------------------------")


class Soldado(NPC):
    def __init__():
        
