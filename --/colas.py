from collections import deque

fila = deque([1,2])
fila.append(3)
fila.append(3)
fila.append(3)
print(fila)
fila.popleft()
print(fila)
if not fila:
    print("fila vacía")