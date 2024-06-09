lista = [1,3,4]
print(*lista)

lista2 = [4,5]

combinada = [*lista, *lista2]
print(combinada)


"""Desempaquetar diccionarios"""

punto1 = {"name": "mocos", "id":4}
punto2 = {"name": "pasto"}

nuevoPunto= {**punto1, **punto2}# con una solo id and name y con dos todo
print(nuevoPunto)