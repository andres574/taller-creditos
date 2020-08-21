 
contador = 0
gano = 0
perdio = 0

while contador < 15:
    nota = int(input("ingrese la nota: "))
    if nota >= 3:
        gano += int(1)
    else:
        perdio += int(1)
    contador += int(1)

print("la cantidad de alumnos que suspendieron son "+str(perdio))
print("la cantidad de alumnos aprobaron sons "+str(gano))