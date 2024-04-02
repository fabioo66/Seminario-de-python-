lista = range(50)
list_par = []
list_impar = []

for i in lista:
    if i % 2 == 0:
        list_par.append(i)
    else:
        list_impar.append(i)

print("Lista de numeros pares:")
for i in list_par:
    print(i)

print("Lista de numeros impares")
for i in list_impar:
    print(i)            
