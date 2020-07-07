# Curso de Python #42
# Expressões Regulares - RegEx Search - Curso de Python #40

import re # RegEx

texto="Curso de Python do CFB cursos, canal do youtube"

pesq=input("pesquisar: ")

res=re.search(pesq, texto)

if(res != None):
    pi=res.start()
    pf=res.end()
    tam=pf-pi
    print(res.start())
    print(res.end())
    print(tam)
else:
    print("não encontrado")

#qtde=len(res)

#print("Qtde: " + str(qtde))

#for t in res:
#    print(t)
    