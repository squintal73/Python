# PRACTICE - PYTHON 038"
# Json - python - files

import json

with open('/home/squintal/PROJETOS/Python/jogador.json') as f:
    
    jog=json.load(f)

def linha():
    print("\n---------------------------------------------\n")

# chaves

for c in jog:
    print(c)
    

linha()    

# itens 

for i in jog.items():
    print(i)
    
linha()

# valores

for v in jog.values():
    print(v)

linha()
# nome do jogador

print(jog["nome"])

linha()
# itens da mochila

print("MOCHILA")

for im in jog["mochila"]:
    print(im)
    
linha()
# itens aeronaves

print("Aeronaves")

for a in jog["aeronaves"]:
    print(a["tipo"] + " - " + str(a["habilidade"]))
    

