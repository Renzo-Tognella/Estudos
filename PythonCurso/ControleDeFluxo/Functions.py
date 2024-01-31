def absTeste():
    x = int
    x = -112
    print(abs(x))
    #abs ele retorna o valor absoluto ou seja seria o modulo dele
def enumerar():
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))
    #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')] seria o mesmo q fazer isso
    print(list(enumerate(seasons)))
    seasons = list(enumerate(seasons, start=1))
    #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')] seria o mesmo q fazer isso
    print(seasons)
def evalTest():
    x = 1
    print(eval('x+1'))
def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x
def groupbyTest():
    groups = []
    uniquekeys = []
    data = sorted(data, key=keyfunc)
    for k, g in groupby(data, keyfunc):
        groups.append(list(g))      # Store group iterator as a list
        uniquekeys.append(k)
def soma(*numeros): #isso se chama xargs, quando passamos arguemento sem saber quantos serao.
    soma = 0
    for num in numeros:
        soma += num
    return soma
def carros(**carro):
    return carro
enumerar()
absTeste()
evalTest()
print(soma(3,4,5,6))

print(carros(marca='Gol', cor='Branco', motor='1.0'))
