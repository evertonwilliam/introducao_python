'''
Aprendendo sobre variáveis em Python.

Desenvolvido por: Everton William Constantino
Data: 03/06/2025
# '''


# Declaração de variáveis
primeiro_numero = 10  # Variável do tipo inteiro
segundo_numero = 5.5  # Variável do tipo float
mensagem = "Olá, Python!"  # Variável do tipo string 
verdadeiro = True  # Variável do tipo booleano (True ou False)

# Exibindo os valores das variáveis
print("Primeiro número:", primeiro_numero)  # Exibe o valor da variável inteiro
print("Segundo número:", segundo_numero)  # Exibe o valor da variável float
print("Mensagem:", mensagem)  # Exibe o valor da variável string
print("Valor booleano:", verdadeiro)  # Exibe o valor da variável booleano

# Operações com variáveis
soma = primeiro_numero + segundo_numero  # Soma de dois números
subtracao = primeiro_numero - segundo_numero  # Subtração de dois números
multiplicacao = primeiro_numero * segundo_numero  # Multiplicação de dois números
divisao = primeiro_numero / segundo_numero  # Divisão de dois números

# Exibindo os resultados das operações
print("Soma:", soma)  # Exibe o resultado da soma
print("Subtração:", subtracao)  # Exibe o resultado da subtração
print("Multiplicação:", multiplicacao)  # Exibe o resultado da multiplicação
print("Divisão:", divisao)  # Exibe o resultado da divisão

# Exemplo de concatenação de strings
nome = "Everton"  # Variável do tipo string
sobrenome = "Constantino"  # Variável do tipo string
nome_completo = nome + " " + sobrenome  # Concatena as strings

# Exibindo o nome completo
print("Nome completo:", nome_completo)  # Exibe o nome completo

# Exemplo de formatação de strings
idade = 30  # Variável do tipo inteiro
mensagem_formatada = f"{nome_completo} tem {idade} anos."  # Formata a string

# Exibindo a mensagem formatada
print(mensagem_formatada)  # Exibe a mensagem formatada

# mostrando o tipo de cada variável
print("Tipo de primeiro_numero:", type(primeiro_numero))  # Exibe o tipo da variável inteiro
print("Tipo de segundo_numero:", type(segundo_numero))  # Exibe o tipo da variável float
print("Tipo de mensagem:", type(mensagem))  # Exibe o tipo da variável string
print("Tipo de verdadeiro:", type(verdadeiro))  # Exibe o tipo da variável booleano