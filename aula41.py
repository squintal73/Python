# Curso de Python #40
# Expressões Regulares - RegEx findall - Curso de Python #40

import re # RegEx

texto="Curso de Python do CFB cursos"

pesq=input("pesquisar: ")

res=re.findall(pesq, texto)

print(res)

qtde=len(res)

print("Qtde: " + str(qtde))

for t in res:
    print(t)
    