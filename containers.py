class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - precio: {self.precio}"
    

class Categoria:
    productos = []

    def __init__(self,nombre,productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self,producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

p1 = Producto("suavitel", 321332131312)
p2 = Producto("cepillo", 321332131312)
p3 = Producto("comocs", 321332131312)
p4 = Producto("comoics", 321332131312)
p5 = Producto("chamoi", 321332131312)

aseo = Categoria("aseo",[p1,p2,p3,p4,p5])

aseo.imprimir()