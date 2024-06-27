import setuptools
from pathlib import Path

#long_desc = Path("/holaMundoplayer/READMEPACKAGE.md")
# en este caso el readme no lo quiero usar. :)

setuptools.setup(
    name="holaMundoLayer",
    version="0.0.0",
    long_description="Este es de un tutorial de \"ultimate python\" de Udemy",
    packages=setuptools.find_packages(
        exclude=["mocks", "test", "--", "archivos", "exceptions", "indice_paquetes", "modulos", "paquetes_nativos", "rutas&Directorios", "sqlite"]
    )
)