from operator import attrgetter

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando instâncias de objetos
pessoa1 = Pessoa("Alice", 25)
pessoa2 = Pessoa("Bob", 30)
pessoa3 = Pessoa("Charlie", 22)

# Criando uma lista de objetos
pessoas = [pessoa1, pessoa2, pessoa3]

# Ordenando a lista com base no atributo 'idade'
pessoas_ordenadas = sorted(pessoas, key=attrgetter('idade'))

# Exibindo os resultados
for pessoa in pessoas_ordenadas:
    print(pessoa.nome, pessoa.idade)
    
my_list = [10, 20, 30, 40, 50]

# Procurando o índice do elemento 30 na lista
index_of_30 = my_list.index(30)
print(index_of_30)  # Saída: 2

# Procurando o índice do elemento 40 na lista a partir do índice 2
index_of_40_after_index_2 = my_list.index(40, 2)
print(index_of_40_after_index_2)  # Saída: 3

# Procurando o índice do elemento 20 na lista entre os índices 1 e 3
index_of_20_between_1_and_3 = my_list.index(20, 1, 3)
# Gera ValueError, pois 20 não está entre os índices 1 e 3 em my_list