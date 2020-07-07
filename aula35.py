# Curso de Python #35
# Datas

import datetime

def linha():
    print("\n------------------------------------------\n")

data=datetime.datetime.now()
nasc_s=datetime.datetime(1973,3,13)
nasc_m=datetime.datetime(1971,7,4)

linha()
print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))
linha()
print(nasc_s)
print(nasc_s.strftime("%j"))
linha()
print(nasc_m)
print(nasc_m.strftime("%A"))

# %a - txt dia abreviado 
# %A - txt dia completo
# %w - num dia da semana
# %d - num dia do mes
# %b - txt mes abreviado
# %B - txt mes
# %m - num do mes
# %y - Ano com 2 dig
# %Y - Ano completo
# %H 00-23
# %I 00-12
# %p AM - PM
# %M minutos
# %S segundos
# %f microsegs
# %j Dia do ano - Dia julian 365
