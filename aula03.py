# tipo de  variaveis

import random

num_i=10
num_f=23.2
num_c=34j
num_r=random.randrange(0,60)

num_y=[
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60)
]

print ("Valor aleatorio = " + str(num_r))
print ("Valor : " + str(num_i) + " Tipo : " + str(type(num_i)))
print ("Valor : " + str(num_f) + " Tipo : " + str(type(num_f)))
print ("Valor : " + str(num_c) + " Tipo : " + str(type(num_c)))
print ("Valor 1: " + str(num_y[0]))
print ("Valor 2: " + str(num_y[1]))
print ("Valor 3: " + str(num_y[2]))
print ("Valor 4: " + str(num_y[3]))
print ("Valor 5: " + str(num_y[4]))
print ("Valor 6: " + str(num_y[5]))
