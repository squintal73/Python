# Consultar API viacep
# Fazendo uma requisição GET
# Data: 07/07/2020
# Autor: Sidnei Quintal
# V001.

import requests
import os

os.system("clear")
cep=input("Digite o CEP : ")

def consulta_cep(cep):
    url='http://viacep.com.br/ws/%s/json'%cep
    r = requests.get(url)
    r_json=r.json()
    logradouro = r_json['logradouro']
    localidade = r_json['localidade']
    status=r.status_code
    #print("Status de Conexao: " + str(status))
    return  logradouro,localidade
    
if __name__ == '__main__':
    logradouro, localidade = consulta_cep(cep)
    print ("Localidade: " + localidade)
    print ("Lougradouro: " + logradouro)
    



