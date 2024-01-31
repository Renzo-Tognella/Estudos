set1 = {'a', 'b', 'j'}
set2 = {'a', 'b', 'd'}
set3 = {'c', 'd', 'f'}
set4 = {'a', 'b', 'c'}
set5 = {'a', 'b', 'c', 'd', 'f'}

set4 = set1.union(set3)
print(set4)

set5 = set1.difference(set3) # a diferença dos itens existente em set1 q n existem em set 3
print(set5)

set6 = set1.symmetric_difference(set3) # a simeteria da diferença dos dois
print(set6)

set7 = set1.intersection(set2)#intersecçao
print(set7)

set8 = set1.isdisjoint(set3) #Sao conjutos totalmente diferentes?
print(set8)

set9 = set5.issubset(set4) #Set 4 é um subconjunto de set5? 
print(set9)

set10 = set4.issuperset(set5) #Set 4 é um 
print(set10)