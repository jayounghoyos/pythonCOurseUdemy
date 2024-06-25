from pathlib import Path

archivo = Path("archivos/prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
print(texto)

texto.insert(0,"holaMundo!")
# archivo.write_text(f"{texto}", "utf-8")
archivo.write_text("\n".join(texto), "utf-8")