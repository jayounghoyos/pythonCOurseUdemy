from pprint import pprint
string = "Hola mundo string :)"

def delEspacios(texto):
    return [char for char in texto if char != " "]#Var, iterable, logic

def cuentaCaracteres(lista):
    char_dict = {}
    for char in lista:
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1
    return char_dict

def ordena(dict):
    return sorted(dict.items(),key=lambda key:key[1], reverse=True)

def mayores(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def mensaje_mayores(dict):
    mensaje = "los que más se repiten son: \n"
    for key, valor in dict.items():
        mensaje += f"-> {key} con {valor} repeticiones \n"
    return mensaje

sinEspacios = delEspacios(string)
count = cuentaCaracteres(sinEspacios)
ordenado = ordena(count)
mayores = mayores(ordenado)
pprint(mensaje_mayores(mayores))
#pprint(count, width=2) #indent, width, depth