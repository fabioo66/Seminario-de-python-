''' 
Explicá qué hace el siguiente código. Proponé una mejora que utilice mejor las funcionalidades
vistas de Python sin usar pandas y explicá cuál es dicha mejora. Si considerás que este código
es el más adecuado, decinos por qué

import csv
name_file = 'files/area_protegida.csv'
data_set = open(name_file)
reader = csv.reader(data_set, delimiter=',')
header = next(reader)
print(header)
data_set.close()
'''

# El código proporcionado tiene el propósito de leer un archivo CSV llamado area_protegida.csv ubicado en la carpeta files y mostrar su encabezado
# El código es correcto, pero se puede mejorar utilizando la sentencia with para abrir el archivo y leerlo, de esta manera se asegura que el archivo se cierre correctamente al finalizar la lectura
# Además, que el tipo de codificacion del archivo no este especificado puede causar problemas en la lectura del archivo, por lo que se recomienda especificar el tipo de codificacion por ejemplo: utf-8
# La mejora propuesta es la siguiente:

import csv
name_file = 'files/area_protegida.csv'
with open(name_file, encoding='utf-8', newline='') as data_set:
    reader = csv.reader(data_set, delimiter=',')
    header = next(reader)
    print(header)  

# La mejora propuesta es mejor ya que se asegura que el archivo se cierre correctamente al finalizar la lectura, además de especificar el tipo de codificacion del archivo para evitar problemas en la lectura del archivo
# Agregamos el parametro newline='' para evitar problemas con la lectura de archivos CSV en Windows