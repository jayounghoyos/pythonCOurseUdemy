from pathlib import Path
from pprint import pprint

path = Path("modulos")
# path.exists()
# path.mkadir()
# path.rmdir()
# path.rename("chanchito-feliz")

# for p in path.iterdir():
#     print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("*.py")] ##[nombre que quiero al comienzo]*.[extension]
archivos = [p for p in path.glob("**/*.py")] #todas las carpetas definidas en el paquete imcluye todos los .py

pprint(archivos)