class Usuario():
    def guardar(self):
        print("Guardando en BBDD")

class Sesion():
    def guardar(self):
        print("Guardando archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

user = Usuario()
sesion = Sesion()

guardar([sesion, user])