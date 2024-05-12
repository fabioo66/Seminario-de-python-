def replace_bar(my_list):
    result = [elem.replace('///', '-') for elem in my_list]
    return result

def replace_dash(my_list):
    result = [elem.replace('--', 'NO') for elem in my_list]
    return result


# Mi funcion
def replace_bar_and_dash(my_list):
    """This function receives a list and replaces 
    these characters '///' for '-' and '--' for 'NO'"""
    result = [elem.replace("///", "-").replace("--", "NO") for elem in my_list]
    return result


# La de chatgpt
def replace_chars(my_list, replacements):
    for target, replacement in replacements:
        my_list = [elem.replace(target, replacement) for elem in my_list]
    return my_list


my_list = ["BUENOS AIRES", "25 de Mayo", "25 de Mayo", "23408", "SI", "SI", "--", "SI", "SI", "SI"]
resultado = replace_dash(my_list)
print(resultado)
#---->["BUENOS AIRES", "25 de Mayo", "25 de Mayo", "23408", "SI", "SI", "NO", "SI", "SI", "SI"]

my_list = ["Formosa", "607419", "605507", "1912", "///", "296810", "295291", "1519", "///"]
print(replace_bar(my_list))
#---->["Formosa", "607419", "605507", "1912", "-", "296810", "295291", "1519", "-"]

print("------------------------------------------------------------------------------------")
my_list = ["Messi", "Watkins", "Lebron", "--", "///", "--", "Mayweather", "--", "///"]
print(replace_bar_and_dash(my_list))
#---->["Messi", "Watkins", "Lebron", "NO", "-", "NO", "Mayweather", "NO", "-"]

import csv

try:
    with open('books.csv', 'r') as archivo:
        my_list = csv.reader(archivo)
        for row in my_list:
            print(row)
except FileNotFoundError:
    print("El archivo csv no se encontró.")
except csv.Error as e:
    print(f"Error de formato CSV: {e}")
except Exception as e:
    print("Ocurrió un error:", e)