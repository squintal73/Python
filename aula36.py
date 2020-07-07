# PRACTICE - PYTHON 036"
# Json

import json
carros_json='{"marca":"Honda","modelo":"HRV","cor":"Prata"}'
carros=json.loads(carros_json)

# for x in carros.values(): imprimi os valores  "Honda"
# for x in carros.items(): imprimi os a linha tota ou o item "{"marca":"Honda"}"
# for x in carros(): imprimi a chave  "marca"

# for x in carros.items():
#    print(x)
    
for k,v  in carros.items():
    print(k,v)
    
