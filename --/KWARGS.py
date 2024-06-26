"""Empaquetar parametros en uno solo"""
def get_product(**datos):
    print(datos["id"])

get_product(id="id", nombre="iphone", desc="Es un iphone")