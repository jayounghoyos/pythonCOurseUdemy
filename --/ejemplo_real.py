from abc import ABC, abstractmethod

"""
Un método abstracto en Python es un método declarado en una clase base (abstracta) 
sin implementación. Las clases derivadas (subclases) deben proporcionar su propia 
implementación para estos métodos. Esto asegura que todas las subclases cumplan con 
una interfaz común definida por la clase base.

Para usar métodos abstractos y clases abstractas en Python, se emplea el módulo abc 
(Abstract Base Classes):

1. Importar ABC y abstractmethod:
   - `ABC` es la base para todas las clases abstractas.
   - `abstractmethod` es un decorador que define métodos abstractos.

2. Definir una Clase Abstracta:
   - Una clase abstracta hereda de `ABC` y puede tener métodos abstractos.

3. Declarar Métodos Abstractos:
   - Los métodos abstractos se decoran con `@abstractmethod`.

4. Crear Subclases:
   - Las subclases deben implementar todos los métodos abstractos para ser instanciadas.
"""

class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id: {_id} en la tabl: {self.tabla}")

class Usuario(Model):
    tabla = "usuario"

    def guardar(self):
        print(f"Guardando usuario.")

usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)

# Ahora no se puede implementar un método abstracto
# para que los que hereden sean los que lo usen
# mod = Model()
