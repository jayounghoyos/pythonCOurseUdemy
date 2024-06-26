class volar:
    def __init__(self):
        self.volador = True

    def volar(self):
        print("volando")

class nadar:
    def nadar(self):
        print("nadando")

class caminar:
    def caminar(self):
        print("caminado")

class Pato(nadar,caminar,volar):#Aplica de derecha a izquierda y los reemplaza
    def __init__(self):
        super().__init__()
        self.nada = True

    def vuela(self):
        super().volar()
        print("volar patito")

pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)