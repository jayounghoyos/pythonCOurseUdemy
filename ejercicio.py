def palindromo(palabra):
    word = palabra.replace(" ", "").lower()  # Convertimos a minúsculas para evitar errores por mayúsculas
    return word == word[::-1]

print(palindromo("Amo la paloma"))  # Esto imprimirá True
