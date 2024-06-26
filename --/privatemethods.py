class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property #getters
    def nombre(self):
        print("pasando por getter")
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        print("pasando por setters")
        if nombre.strip():
            self.__nombre = nombre
        return
    

perro = Perro("True")
print(perro.nombre)#Aún así obtener las propiedades privadas 