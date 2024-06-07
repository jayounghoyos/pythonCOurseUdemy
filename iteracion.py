mascotas = ["paco", "pato", "PASTO","pato", "PASTO","pato", "PASTO","pato", "PASTO"]


primero, segundo = [1, 2]
for indice, mascotas in enumerate(mascotas):
    print(indice, mascotas)#0 index
    #1 string content


print(mascotas.count("PASTO"))

if "PASTO" in mascotas:
    print(mascotas.index("PASTO"))