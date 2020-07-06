# PRACTICE - PYTHON 026"
# TRY EXCEPT

#x=10
num=10

if not type(num) is int:
    raise Exception("Somente numeros")
else:
    print(num)

#if num < 1:
 #   raise Exception("Valor nao permitido")

try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do Tratamento")
    
#except NameError