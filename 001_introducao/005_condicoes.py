'''
Aprendendo sobre condições em Python
# Condições em Python

Desenvolvido por: Everton William Constantino
Data: 03/06/2025

Importante: Este código é um exemplo simples para demonstrar o uso de condicionais em Python.
O if é usado para executar um bloco de código se uma condição for verdadeira.
O else é usado para executar um bloco de código se a condição for falsa.

As condicionais utilizam operadores de comparação, como:
- Igualdade: `==`
- Diferença: `!=`
- Maior que: `>`
- Menor que: `<`
- Maior ou igual a: `>=`
- Menor ou igual a: `<=`
- E lógico: `and`
- Ou lógico: `or`
'''

print('Condicionais em Python')

# Condicional simples
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade')

# Condicional composta
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

# Condicional aninhada
if idade >= 18:
    print('Você é maior de idade')
else:
    if idade >= 16:
        print('Você é menor de idade, mas pode votar')
    else:
        print('Você é menor de idade e não pode votar')

# Condicional com elif
if idade >= 18:
    print('Você é maior de idade')
elif idade >= 16:
    print('Você é menor de idade, mas pode votar')
else:
    print('Você é menor de idade e não pode votar')