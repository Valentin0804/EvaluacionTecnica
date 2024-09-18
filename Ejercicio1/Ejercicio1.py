# -- EJERCICIO 1 --
lista = [1,10,6,8,15,2] 

# -- 1.A -- 
mayor_1 = 0

for elemento in lista:
    if mayor_1 < elemento:
        mayor_1 = elemento

print(mayor_1)

# -- 1.B --
mayor_2 = max(lista)

print(mayor_2)

# -- 2 --

# -- V.1 --
lista_ordenada = sorted(lista)
print(lista_ordenada)

# -- V.2 --
n = len(lista)

for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)

# -- 3 --
lista_par = []
for i in range(n):
    if ((lista[i]%2)== 0):
        print('Número par: ',lista[i],'Posicion del número: ', i)
        # -- 4 --
        lista_par.append(lista[i])

print(lista_par)
