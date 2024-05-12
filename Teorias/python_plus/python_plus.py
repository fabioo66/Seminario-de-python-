def replace_bar(my_list):
    result = [elem.replace('///', '-') for elem in my_list]
    return result

def replace_dash(my_list):
    result = [elem.replace('--', 'NO') for elem in my_list]
    return result

my_list = ["BUENOS AIRES", "25 de Mayo", "25 de Mayo", "23408", "SI", "SI", "--", "SI", "SI", "SI"]
resultado = replace_dash(my_list)
print(resultado)
#---->["BUENOS AIRES", "25 de Mayo", "25 de Mayo", "23408", "SI", "SI", "NO", "SI", "SI", "SI"]

my_list = ["Formosa", "607419", "605507", "1912", "///", "296810", "295291", "1519", "///"]
print(replace_bar(my_list))
#---->["Formosa", "607419", "605507", "1912", "-", "296810", "295291", "1519", "-"]

import csv

try:
    with open('books.csv', 'r') as archivo:
        my_list = csv.reader(archivo)
        for row in my_list:
            print(row)
except FileNotFoundError:
    print("El archivo csv no se encontró.")
except Error as e:
    print(f"Error de formato CSV: {e}")
except Exception as e:
    print("Ocurrió un error:", e)