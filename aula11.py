# PRACTICE - PYTHON 011"
# ARRAYS

import os
carros=[]
carro=input("Digite o nome do novo carro: ")
while carro != "-1":
    carros.append(carro)
    carro=input("Digite o nome do novo carro: ")

os.system ('clear')

for x in carros:
    print(x)

print("Fim do LOOP")
