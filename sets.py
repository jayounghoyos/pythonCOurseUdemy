#grupo o conjuntos de datos desordenados irrepetibles (CONJUNTOS en pocas palabras)
primer = {1,2,3,4,5,6,7,6,7,8,9}
print(primer)

segundo = [3,4,5,6,3,3,7]
segundo = set(segundo)
print(segundo)

#operaciones entre conjuntos
print(primer | segundo)#union de conjuntos
print(primer & segundo)#interseccion de conjuntos
print(primer - segundo)#diferencia de conjuntos
print(primer ^ segundo)#Diferencia simetrica