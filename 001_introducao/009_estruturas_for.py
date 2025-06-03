'''
Estrutura de repetição for
# Estruturas de repetição são fundamentais na programação, permitindo que um bloco de código seja executado várias vezes com base em uma condição.
# Neste exemplo, vamos explorar a estrutura de repetição `for`, que itera sobre uma sequência (como uma lista, tupla ou string) e executa um bloco de código para cada item da sequência.
# Exemplo de uso do for para iterar sobre uma lista

Desenvolvido por: Everton William Constantino
# Data: 03/06/2025
'''
# Exemplo de uso do for para iterar sobre uma lista
lista = [1, 2, 3, 4, 5]  # Lista de números
for numero in lista:
    print(numero)  # Imprime cada número da lista
print("Iteração sobre a lista concluída.\n")

# Exemplo de uso do for para iterar sobre uma string
string = "Python"  # String de exemplo
for letra in string:
    print(letra)  # Imprime cada letra da string
print("Iteração sobre a string concluída.\n")

# Exemplo de uso do for para iterar sobre um range
for i in range(1, 11):  # Itera de 1 a 10
    print(i)  # Imprime cada número do range
print("Iteração sobre o range concluída.\n")