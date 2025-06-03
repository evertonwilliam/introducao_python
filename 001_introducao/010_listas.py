'''
Aprendendo Python - Listas
# Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. Elas são mutáveis, ou seja, podem ser alteradas após a criação.
# Neste exemplo, vamos explorar como criar, acessar e manipular listas em Python.

# Desenvolvido por: Everton William Constantino
# Data: 03/06/2025
'''
# Exemplo de criação de uma lista
lista = [1, 2, 3, 4, 5]  # Lista de números

# Acessando elementos da lista
print("Acessando elementos da lista:")
for i in range(len(lista)): # Obtém o tamanho da lista e itera sobre cada índice
    print(f"Elemento na posição {i}: {lista[i]}")  # Imprime cada elemento da lista
print("Acesso aos elementos da lista concluído.\n")

# Adicionando elementos à lista
lista.append(6)  # Adiciona o número 6 ao final da lista
print("Lista após adicionar o número 6:", lista)  # Imprime a lista atualizada

# Removendo elementos da lista
lista.remove(3)  # Remove o número 3 da lista
print("Lista após remover o número 3:", lista)  # Imprime a lista atualizada

# Ordenando a lista
lista.sort()  # Ordena a lista em ordem crescente
print("Lista após ordenação:", lista)  # Imprime a lista ordenada

# Verificando o tamanho da lista
tamanho = len(lista)  # Obtém o tamanho da lista
print("Tamanho da lista:", tamanho)  # Imprime o tamanho da lista

# Verificando se um elemento está na lista
if 4 in lista:  # Verifica se o número 4 está na lista
    print("O número 4 está na lista.")  # Imprime mensagem se o número estiver na lista
else:
    print("O número 4 não está na lista.")
print("Verificação de presença do número 4 concluída.\n")

# Exemplo de iteração sobre uma lista
print("Iterando sobre a lista:")
for numero in lista:
    print(numero)  # Imprime cada número da lista
print("Iteração sobre a lista concluída.\n")

# Exemplo de lista com diferentes tipos de dados
lista_mista = [1, "Python", 3.14, True]  # Lista com diferentes tipos de dados
print("Lista mista:", lista_mista)  # Imprime a lista mista

# Acessando elementos de uma lista mista
print("Acessando elementos da lista mista:")
for item in lista_mista:
    print(item)  # Imprime cada item da lista mista
print("Acesso aos elementos da lista mista concluído.\n")

# Exemplo de fatiamento de lista
fatiamento = lista[1:4]  # Obtém uma sublista dos elementos da posição 1 até a 3
print("Fatiamento da lista (posição 1 a 3):", fatiamento)  # Imprime a sublista

# Exemplo de lista aninhada (lista dentro de uma lista)
lista_aninhada = [[1, 2], [3, 4], [5, 6]]  # Lista contendo outras listas
print("Lista aninhada:", lista_aninhada)  # Imprime a lista aninhada

# Acessando elementos de uma lista aninhada
print("Acessando elementos da lista aninhada:")
for sublista in lista_aninhada:
    for numero in sublista:
        print(numero)  # Imprime cada número de cada sublista
print("Acesso aos elementos da lista aninhada concluído.\n")

# Exemplo de lista com compreensão de lista
lista_compreensao = [x**2 for x in range(1, 6)]  # Cria uma lista com os quadrados dos números de 1 a 5
print("Lista com compreensão de lista (quadrados de 1 a 5):", lista_compreensao)  # Imprime a lista criada

# Exemplo de uso de métodos de lista
print("Usando métodos de lista:")

# Verificando se a lista está vazia
if not lista:  # Verifica se a lista está vazia
    print("A lista está vazia.")
else:
    print("A lista não está vazia.")

# Limpando a lista
lista.clear()  # Limpa todos os elementos da lista
print("Lista após limpeza:", lista)  # Imprime a lista após limpeza

# Exemplo de concatenação de listas
lista1 = [1, 2, 3]  # Primeira lista
lista2 = [4, 5, 6]  # Segunda lista
lista_concatenada = lista1 + lista2  # Concatena as duas listas
print("Lista concatenada:", lista_concatenada)  # Imprime a lista concatenada

# Exemplo de repetição de lista
lista_repetida = lista1 * 3  # Repete a lista 3 vezes
print("Lista repetida:", lista_repetida)  # Imprime a lista repetida
