nums = (1,2,3,4) + (4,6,7,8)
print(nums)

transform = tuple([1,2])
print(transform)
nums.pop()
menosNumeros = nums[:2]
print(menosNumeros)

primero, segundo, *otros = nums
print(primero,segundo,otros)