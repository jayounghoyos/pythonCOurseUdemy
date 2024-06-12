class volar:
    def volar(self):
        print("volando")

class nadar:
    def nadar(self):
        print("nadando")

class caminar:
    def caminar(self):
        print("caminado")

class Pato(nadar,caminar,volar):#Aplica de derecha a izquierda y los reemplaza
    def programar(self):
        print("programando")

pato = Pato()