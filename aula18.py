# PRACTICE - PYTHON 018"
# FUCTION 02 -argumentos abrietarios

def textos(*txt):
    for t in txt:   
        print(t)
   

textos("CDF Cursos","Python","Canal","Computador")


def carros(c="Valor Padrao"):
    print("Modelo : " + c)

carros("CAPTUR")