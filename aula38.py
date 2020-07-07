# PRACTICE - PYTHON 038"
# Json

import json

carros_dictionary={
    "marca":"Honda",
    "modelo":"HRV",
    "cor":"Prata"
}

#dictionary -> objeto json

carros_list=["honda","volks","ford","toyota"]

# list -> array json

carros_tupla=("carros","volks","ford","toyota")

#tupla -> array json


carros_j=json.dumps(carros_dictionary,indent=4,separators=(":","="),sort_keys=True)
#carros_j=json.dumps(carros_list)
#carros_j=json.dumps(carros_tupla)


print(carros_j)