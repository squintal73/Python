texto=" Curso de Python "

palavra="python"

busca=palavra in texto

busca1=palavra.upper() in texto.upper()


print(busca)

print(busca1)

cidade="Sao Paulo"
dia=01
mes="Julho"
ano=2020
canal="CURSO SIDNEI"
data="{}, {} de {} de {}\n\n \"{}\""

print(data.format(cidade,dia,mes,ano,canal))

# boleano

auka=""
aula="S"

print(bool(auka))
print(bool(aula))

if aula:
    print("Aula Possui Texto")
else:
    print("Aula Nao possui Texto")


if auka:
    print("Auka Possui Texto")
else:
    print("Auka Nao possui Texto")