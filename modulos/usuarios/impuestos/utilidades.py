if __name__ != "__main__":
    from ..gestion.CRUD import guardar
    print(__name__)

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()

if __name__ == "__main__":
    print("Tarea de mantenimiento")