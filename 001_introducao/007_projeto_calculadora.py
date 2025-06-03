'''
PROJETO: Calculadora Simples
Este projeto consiste em criar uma calculadora simples que realiza operações básicas como adição, subtração, multiplicação e divisão. A calculadora deve ser capaz de receber dois números e a operação desejada, e retornar o resultado da operação.

Desenvolvido por: Everton William Constantino
Data: 03/06/2025

# Importante: Este código é um exemplo simples para demonstrar o uso de funções e condicionais em Python.
'''

#cabecalho do projeto

print('************************************************')
print('************Calculadora Simples*****************')
print('************************************************')

# Solicita ao usuário os números e a operação desejada
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada (+, -, *, /): ')

# Realiza a operação com base na escolha do usuário
if operacao == '+':
    print (numero1 + numero2)
elif operacao == '-':
    print (numero1 - numero2)
elif operacao == '*':
    print (numero1 * numero2)
elif operacao == '/':
    if numero2 != 0:
        print (numero1 / numero2)
    else:
        print ('Erro: Divisão por zero não é permitida.')
else:
    print('Operação inválida. Por favor, escolha entre +, -, *, /.')

# Fim do projeto de calculadora simples