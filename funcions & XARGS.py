def hola(nombre, apellido="felix"): #por defecto "Felix"
    print("Hola mundo")
    print(f"Bienvenido {nombre}, {apellido}")

hola("juan", "andres")
print("*"*10)

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(1,2,3,4)
suma(1,2)
suma(1,2,3,4,32,4)