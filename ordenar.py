nums = [2,4,3,4,5,6,7,8,9,10]

#nums.sort(reverse= True)
nums2 = sorted(nums) #Crea una nueva lista pero ordenada
print(nums)
print(nums2)

usuarios = [
    [1,"pasyo"],
    [2,"popeye"],
    [5,"noto"]
]
#el primer elemento debe ser ordenable o yo tengo que elegir
def ordena(elemento):
    return elemento[1]#Ordena dependiendo del item de elección

usuarios.sort(key=ordena)
print(usuarios)