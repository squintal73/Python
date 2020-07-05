# PRACTICE - PYTHON 022"
# FUCTION 05 -Lambda ou anomimas

#lambda arg:expr

soma=lambda a,b:a+b
print(soma (2,2))

print((lambda a,b:a+b)(2,3))

mult=lambda a,b,c:(a+b)*c
print(mult(2,5,3))

r=lambda x,func:x+func(x)

total=r(2,lambda x:x*x)

print(total)

total=r(2,lambda x:x+3)

print(total)