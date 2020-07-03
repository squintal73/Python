
# PRACTICE - PYTHON 010"
# LOOP - WHILE

import os
os.system('clear')

i=0
while i<11:
    print(i)
    i+=1
    if(i>=5):
        break
print("Fim do LOOP > " + str(i))

carros=["HRV","GOLF","ARGO","FOCUS"]

i=0
tam=len(carros)
print("tamanho > " + str(tam))
while i<tam:
    print(carros[i])
    i+=1
    
# if(i>=5):
# break
print("Fim do LOOP > " + str(i))
