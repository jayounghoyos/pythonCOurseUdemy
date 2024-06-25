from io import open

#escritura
# texto = "hola mundo! v:) ;)"

# archivo = open("holaMundo.txt","w") #(w)-> write
# archivo.write(texto)
# archivo.close()

#Solo lectura
# archivo = open("holaMundo.txt","r")
# texto = archivo.read()
# archivo.close()
# print(texto)

#Lectura como Lista
# archivo = open("holaMundo.txt","r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)


# #with & seek
# with open("holaMundo.txt", "r") as archivo:#With permite cerrarlo automaticamente
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)


#Agregar
archivo = open("holaMundo.txt", "a+")
archivo.write("pelea!!!!")
archivo.close()

#lectura y escritura
with open("holaMundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)