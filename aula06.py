# PRACTICE - PYTHON 006"
# HASHS / ARRAYS

carros=["HRV","GOLF","ARGO","FOCUS"]
carros.append("FIT")
carros.append("FUSION")
carros.append("CAPTUR")

#carros.remove("FUSION")
carros.pop() # sempre remove o ultimo elemento da lista
# del carros[2]

carros2=["HRV1","GOLF2","ARGO2","F2OCUS"]

carros3=carros+carros2

print(str(len(carros3)) + " Carros na Lista")

print(carros3)
