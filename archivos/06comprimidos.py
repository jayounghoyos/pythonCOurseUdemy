from zipfile import ZipFile
from pathlib import Path

#Escribir
with ZipFile("archivos/comprimidos.zip", "w") as zip:
    #curso-py
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)

#leer
with ZipFile("archivos/comprimidos.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("archivos/06comprimidos.py")
    print(info.file_size,
            info.compress_size)