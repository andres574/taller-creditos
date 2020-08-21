num1 = int(input("ingrese el primer numero "))
num2 = int(input("ingrese el segundo numero "))

for numero in range(num1,num2):
    if numero % 2 != 0:
        print(numero)

