usuarios = [
    [1,"pasyo"],
    [2,"popeye"],
    [5,"noto"]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

#map
#nombres = [usuario[0] for usuario in usuarios] #expresion for usuario in usuarios
#nombres = list(map(lambda usuario: usuario[0],usuarios))

#filtrar
# nombres = [usuario for usuario in usuarios if usuario[0] > 1]
usuarios_filtrados = list(filter(lambda usuario: usuario[0] > 2, usuarios))

print(usuarios_filtrados)