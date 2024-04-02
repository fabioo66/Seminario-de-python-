lista = []

try:
    x = int(input("Ingrese una cadena de numeros (finaliza con el numero '9999')"))
except ValueError:
    print('Eso no es un numero')

while x != 9999:
    lista.append(x)
    try:
        x = int(input())
    except ValueError:
        print('Eso no es un numero')

print("Lista de números ingresados:")
for num in lista:
    if num < 0:
        print("Se ha encontrado un número negativo. Deteniendo la impresión.")
        break
    print("Numero: ", num)
