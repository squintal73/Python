# PRACTICE - PYTHON 014"
# DICTIONARY
# CHAVE/key - VALOR/Value

car={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2020",
    "Cor":"Prata"
}

if "Modelo" in car:
    print(car["Modelo"])

for c,v in car.items():
    print(c + " : " + v)

#car_get=car.get("Ano")
#print(car["Fabricante"])
#print(car_get)
#for x in car:
   # print(x) # CHAVES
   # print(car[x]) # VALORES

