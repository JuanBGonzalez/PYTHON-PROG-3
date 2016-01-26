'''
Realizar toda la suma de los numeros pares entre 10 y 5000 sin contemplar a 100 y 1000
'''
s=0
x=10
for x in range(5000):
    if x%2==0 and x!=1000 and x!=100 :
        s=x+s
print(str(s))