# GAME - PYTHON 001"
# ADIVINHA UM NUMERO
import random
import os
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu numero: "))
while(sorteado!=jogador):
    os.system('clear')
    if(sorteado>jogador):
        print("ERROU!!! - O numero eh maior")
    elif(sorteado<jogador):
        print("ERROU!!! - O numero eh menor")
    erros+=1
    jogador=int(input("Digite seu numero: "))
print("Numero " + str(jogador) + " Voce Acertou !!! em " + str(erros+1) + " Tentativas")
