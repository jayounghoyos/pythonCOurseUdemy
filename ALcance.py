saludo = "Hola soy global"

def saludar():
    global saludo
    saludo = "Hola mundo"

print(saludo)
saludar()
print(saludo)