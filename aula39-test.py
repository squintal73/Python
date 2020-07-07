# PRACTICE - PYTHON 038"
# Json - desafio

import json

# {
#  "nome":"Bruno",
#  "time":"aviadores",
#  "vivo":"True",
#  "energia":100,
#  "mochila":["pederneira","corda","linha","arame"],
#  "aeronaves":[
#    {"tipo":"transporte","habilidade":80},
#    {"tipo":"ataque","habilidade":100},
#    {"tipo":"reconhecimento","habilidade":50}
#   ]
# }

jogador_j='{"nome":"Bruno","time":"aviadores","vivo":"True","energia":100,"mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

jog=json.loads(jogador_j)

#print(car["Modelo"])
#print(jog["mochila"])
#print(jog["aeronaves"])

# chaves

for c in jog:
    print(c)
    
# itens 

for i in jog.items():
    print(i)
    
# valores

for v in jog.values():
    print(v)

# nome do jogador

print(jog["nome"])

# itens da mochila

print("MOCHILA")

for im in jog["mochila"]:
    print(im)
    

# itens aeronaves

print("Aeronaves")

for a in jog["aeronaves"]:
    print(a["tipo"] + " - " + str(a["habilidade"]))
    

