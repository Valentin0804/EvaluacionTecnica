# -- EJERCICIO 1 --
lista = [1,10,6,8,15,2] 
print(lista)

# -- EJERCICIO 1.A -- 
mayor_1 = 0
posicion_1 = 0

for i in range(1, len(lista)):
    if mayor_1 < lista[i]:
        mayor_1 = lista[i]
        posicion_1  = i

print("El mayor es:", mayor_1)
print("La posición del mayor es:", posicion_1 )

# -- EJERCICIO 1.B --
mayor_2 = max(lista)
posicion_2 = lista.index(mayor_2)

print("El mayor es:", mayor_2)
print("La posición del mayor es:", posicion_2)

# -- EJERCICIO 2 --

lista_ordenada = sorted(lista)
print(lista_ordenada)

# -- EJERCICIO 3 --

n = len(lista)
lista_par = []
for i in range(n):
    if ((lista[i]%2)== 0):
        print('Número par: ',lista[i],' en posicion de la coleccion: ', i)
        # -- 4 --
        lista_par.append(lista[i])

print(lista_par)
