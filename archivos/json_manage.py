import json
from pathlib import Path

# Escribir JSON
# productos = [
#     {"id": 1, "name": "Surferboard"},
#     {"id": 2, "name": "Bici"},
#     {"id": 3, "name": "skate"},
# ]

# data = json.dumps(productos)
# Path("archivos/productos.json").write_text(data)


#Leer json 
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos= json.loads(data)

#modificar
productos[0]["name"] = "chanchito Feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))