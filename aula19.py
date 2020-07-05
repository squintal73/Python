# PRACTICE - PYTHON 019"
# FUCTION 03 -argumentos abrietarios

def soma (*num):
    r=0 
    for n in num:
        r+=n
    print("Soma = " + str(r))
    
soma(5,2,5)