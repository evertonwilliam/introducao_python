'''
Aprendendo Python - dicionários
Dicionários são coleções de dados que armazenam pares de chave-valor.
# Criando um dicionário
dicionario = { 
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}
# Acessando valores
print(dicionario['nome'])  # Saída: João

Desenvolvido por: Everton William Constantino
Data: 03/06/2025
'''
# Criando um dicionário
dicionario = { 
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

# Acessando valores
print(dicionario['nome'])  # Saída: João

# Adicionando um novo par chave-valor
dicionario['profissao'] = 'Engenheiro'

# Imprimindo o dicionário atualizado
print(dicionario)  # Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Verificando se uma chave existe
if 'idade' in dicionario:
    print("A chave 'idade' existe no dicionário.")  # Saída: A chave 'idade' existe no dicionário.  

# Iterando sobre chaves e valores
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# Removendo um par chave-valor
dicionario.pop('cidade')

# Imprimindo o dicionário após remoção
print(dicionario)  # Saída: {'nome': 'João', 'idade': 30, 'profissao': 'Engenheiro'}

# Limpando o dicionário
dicionario.clear()

# Imprimindo o dicionário após limpeza
print(dicionario)  # Saída: {}

# Verificando o tamanho do dicionário
print(len(dicionario))  # Saída: 0

# Dicionários aninhados
dicionario_aninhado = {
    'pessoa1': {
        'nome': 'Ana',
        'idade': 25
    },
    'pessoa2': {
        'nome': 'Carlos',
        'idade': 28
    }
}

# Acessando valores em dicionários aninhados
print(dicionario_aninhado['pessoa1']['nome'])  # Saída: Ana

# Adicionando um novo dicionário aninhado
dicionario_aninhado['pessoa3'] = {
    'nome': 'Mariana',
    'idade': 22
}

# Imprimindo o dicionário aninhado atualizado
print(dicionario_aninhado)

# Verificando se uma chave existe em um dicionário aninhado
if 'pessoa2' in dicionario_aninhado:
    print("A chave 'pessoa2' existe no dicionário aninhado.")  # Saída: A chave 'pessoa2' existe no dicionário aninhado.

# Iterando sobre dicionários aninhados
for pessoa, info in dicionario_aninhado.items():
    print(f"{pessoa}: {info['nome']} - {info['idade']} anos")

# Verificando o tamanho de um dicionário aninhado
print(len(dicionario_aninhado))  # Saída: 3

# Limpando o dicionário aninhado
dicionario_aninhado.clear()

# Imprimindo o dicionário aninhado após limpeza
print(dicionario_aninhado)  # Saída: {}

# Verificando o tamanho do dicionário aninhado após limpeza
print(len(dicionario_aninhado))  # Saída: 0

# Dicionários com chaves compostas  
dicionario_com_chaves_compostas = {
    ('nome', 'sobrenome'): 'João Silva',
    ('idade', 'ano_nascimento'): (30, 1993),
    ('cidade', 'estado'): ('São Paulo', 'SP')
}   

# Acessando valores com chaves compostas
print(dicionario_com_chaves_compostas[('nome', 'sobrenome')])  # Saída: João Silva

# Adicionando um novo par chave-valor com chaves compostas
dicionario_com_chaves_compostas[('profissao', 'empresa')] = ('Engenheiro', 'Tech Solutions')    

# Imprimindo o dicionário com chaves compostas atualizado
print(dicionario_com_chaves_compostas)

# Verificando se uma chave composta existe
if ('idade', 'ano_nascimento') in dicionario_com_chaves_compostas:
    print("A chave composta ('idade', 'ano_nascimento') existe no dicionário.")  # Saída: A chave composta ('idade', 'ano_nascimento') existe no dicionário.    

# Iterando sobre chaves compostas e valores
for chave, valor in dicionario_com_chaves_compostas.items():
    print(f"{chave}: {valor}")

# Removendo um par chave-valor com chaves compostas
dicionario_com_chaves_compostas.pop(('cidade', 'estado'))

# Imprimindo o dicionário com chaves compostas após remoção
print(dicionario_com_chaves_compostas)

# Limpando o dicionário com chaves compostas
dicionario_com_chaves_compostas.clear()

# Imprimindo o dicionário com chaves compostas após limpeza
print(dicionario_com_chaves_compostas)  # Saída: {}

# Verificando o tamanho do dicionário com chaves compostas após limpeza
print(len(dicionario_com_chaves_compostas))  # Saída: 0

# Dicionários com valores mutáveis
dicionario_com_valores_mutaveis = {
    'lista': [1, 2, 3],
    'tupla': (4, 5, 6),
    'set': {7, 8, 9}
}

# Acessando valores mutáveis
print(dicionario_com_valores_mutaveis['lista'])  # Saída: [1, 2, 3]

# Modificando um valor mutável
dicionario_com_valores_mutaveis['lista'].append(4)

# Imprimindo o dicionário com valores mutáveis atualizado
print(dicionario_com_valores_mutaveis)  # Saída: {'lista': [1, 2, 3, 4], 'tupla': (4, 5, 6), 'set': {7, 8, 9}}

# Verificando se um valor mutável existe
if 2 in dicionario_com_valores_mutaveis['lista']:
    print("O valor 2 existe na lista.")  # Saída: O valor 2 existe na lista.

# Iterando sobre valores mutáveis
for chave, valor in dicionario_com_valores_mutaveis.items():
    print(f"{chave}: {valor}")

# Removendo um valor mutável    
dicionario_com_valores_mutaveis['set'].remove(8)

# Imprimindo o dicionário com valores mutáveis após remoção
print(dicionario_com_valores_mutaveis)  # Saída: {'lista': [1, 2, 3, 4], 'tupla': (4, 5, 6), 'set': {7, 9}}


