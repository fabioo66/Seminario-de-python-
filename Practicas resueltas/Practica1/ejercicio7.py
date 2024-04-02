number_list = []

num = int(input("Ingrese un numero (la carga finaliza con el numero '9999') "))
while num != 9999:
    number_list.append(num)
    num = int(input())

#Imprimo lista
print("Lista de numeros :")
for num in number_list:
    print(num)

#convierto cada numero en str y lo agrego a la cadena con
#guiones de por medio excluyendo los numeros multiplos de 3
cadena = ""
for num in number_list:
    if num % 3 == 0:
        continue
    else:
        cadena += str(num)
        cadena += "-"

# borro el ultimo guion
cadena = cadena[:-1]

print(cadena)