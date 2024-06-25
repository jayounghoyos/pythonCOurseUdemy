import csv 


#Escribir
with open("archivo.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow([ ])