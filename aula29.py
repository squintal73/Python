# Curso de Python #29
# Iterators

carros=["HRV","Polo","Jetta","Cruze","Fusion"]

itCarros=iter(carros) 

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        #print("Fim da Lista")
        break 