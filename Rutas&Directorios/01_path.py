from pathlib import Path

"""Windows"""
# Path(r"C:\Archivos de Programa\cat")
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("Documents/EAFIT")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name, #nombre del archivo con extension
    path.stem, #nombre sin su extension
    path.suffix, #Extension
    path.parent, #Directorio padre
    path.absolute() #La ruta absoluta del path
)

p = path.with_name("EAFIT")
print(p)
p = path.with_suffix(".exe")
print(p)
p = path.with_stem("felix")