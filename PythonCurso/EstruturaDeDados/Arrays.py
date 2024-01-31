#usamos quando temos uma lista muito grande e estamos tendo problema de performance ']
from array import array
cores = ['verde', 'amarelo', 'azul', 'vermelho']
valores = [10, 20, 30, 40]
print(cores)
print(valores)
print()
cores = array('u', ['v', 'a', 'a', 'v'])
valores = array('i',[10, 20, 30, 40])
print(cores)
print(valores)