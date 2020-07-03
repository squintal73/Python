# PRACTICE - PYTHON 007"
# Operadores AND/OR

clima="chuva"

dinheiro=500

lugar=""

if clima=="sol" and dinheiro>300:
    lugar="clube"
else:
    lugar="cinema"

print("Vou ao " + lugar)

if clima=="sol" or (dinheiro>=300 and dinheiro<=500):
    lugar="clube"
else:
    lugar="cinema"

print("Vou ao " + lugar)

op="+"
res=0
a=1
b=2

if op=="+":
    res=a+b
elif op=="-":
    res=a-b
elif op=="*":
     res=a*b
else:
    print("operador invalido")

print(str(a) + op + str(b) + " = " + str(res))

# TABELA VEDADE

# AND
# V V = V
# V F = F
# F V = F
# F F = F

# OR 
# V V = V 
# V F = V
# F V = V
# F F = F 


