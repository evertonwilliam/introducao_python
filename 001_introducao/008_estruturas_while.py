'''
Estruturas de repetição são fundamentais na programação, permitindo que um bloco de código seja executado várias vezes com base em uma condição.
# Neste exemplo, vamos explorar a estrutura de repetição `while`, que executa um bloco de código enquanto uma condição for verdadeira.
# Exemplo de uso do while para contar de 1 a 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1  # Incrementa o contador em 1 a cada iteração

desenvolvido por: Everton William Constantino
# Data: 03/06/2025
'''

# Exemplo de uso do while para contar de 1 a 10
contador = 1    # Inicializa o contador em 1
while contador <= 10:
    print(contador)
    contador += 1  # Incrementa o contador em 1 a cada iteração
print("Contagem de 1 a 10 concluída.\n")

# Exemplo de uso do while para contar de 10 a 1
contador = 10 # Inicializa o contador em 10
while contador >= 1:
    print(contador)
    contador -= 1  # Decrementa o contador em 1 a cada iteração
print("Contagem de 10 a 1 concluída.\n")


# Exemplo de uso do while para contar de 1 a 10, mas pulando os números pares
contador = 1 # Inicializa o contador em 1
while contador <= 10:
    if contador % 2 == 0:  # Verifica se o número é par
        contador += 1
        continue  # Pula para a próxima iteração se for par
    print(contador)
    contador += 1  # Incrementa o contador em 1 a cada iteração
print("Contagem de 1 a 10, pulando números pares, concluída.\n")