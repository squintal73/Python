# PRACTICE - PYTHON 023"
# POO - CLASSES/P1

class Carro:
    velMax=0
    ligado=False
    cor=""

c1=Carro()
c2=Carro()
c3=Carro()

c1.velMax=200
c1.cor="Preto"
c1.ligado=True

print("Velocidade Maxima: " + str(c1.velMax))
print("Cor: " + str(c1.cor))
estado="sim" if c1.ligado else "nao"
print("Ligado: " + estado)