from Alimento import *
from operator import attrgetter
item1 = Banana()
item2 = Abacate()
item3 = Abacaxi()
lista = list()
lista.append(item1)
lista.append(item2)
lista.append(item3)
for alimento in lista:
    print(alimento.nome)   

item12 = Melancia()
item22 = Morango()
item32 = Banana()
lista2 = list()
lista2.append(item12)
lista2.append(item22)
lista2.append(item32)

for alimento in lista2:
    print(alimento.nome)   
print(' ')

lista.extend(lista2)

for alimento in lista:
    print(alimento.nome)   
print(' ')
item42 = Banana()
lista.insert(1, item42)

for alimento in lista:
    print(alimento.nome)   
print(' ')

lista.pop(1)
for alimento in lista:
    print(alimento.nome)   
print(' ')

lista.sort(key=attrgetter('nome'))
for alimento in lista:
    print(alimento.nome)   
print(' ')
