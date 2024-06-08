punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

# if "lala" in punto:
#     print("Encontré a lala",punto["lala"])

print("*"*10)

print(punto.get("x"))
print(punto.get("lala",97))
del punto["x"]
del(punto["y"])

print("*"*10)

print(punto)
punto["x"] = 25

# for valor in punto:
#     print(valor, punto[valor]) #Este metodo no es tan conveniente como el de abajo

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "canut"},
    {"id": 2, "nombre": "Felix"},
    {"id": 4, "nombre": "Nito"},
    {"id": 3, "nombre": "Smought"}
]

ordenados = sorted(usuarios, key=lambda x:x["id"])#a ordenar, funcion lambda, itema iterar
print(ordenados)

print("*"*10)
for usuario in usuarios:
    print(usuario["nombre"].lower())