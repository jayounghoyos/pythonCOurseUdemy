class Perro:

    def __init__(self, nombre,patas):
        self.nombre = nombre 
        self.patas = patas

    # def habla(self):
    #     print("Guau!")
    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("o",4)


Perro.habla()
p1 = Perro("o",4)


p3 = Perro.factory()
print(p3.patas,p3.nombre)