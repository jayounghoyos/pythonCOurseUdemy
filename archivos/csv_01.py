import csv 
from pprint import pprint 
import os

#Escribir
with open("./archivo.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["id","user", "text"])
    writer.writerow([100,1,"twit"])
    writer.writerow([100,2,"twit2"])


#leer
# with open("./archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     #pprint(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

#Actualizar csv
with open("./archivo.csv") as r, open("./archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000,1,"texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("./archivos/archivo.csv")
    os.rename("./archivos/archivo_temp.csv","archivos/archivo.csv")