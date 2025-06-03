'''
PROGRAMA: DICIONÁRIOS EM PYTHON
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO: APRENDER SOBRE DICIONÁRIOS COM PYTHON

COMANDOS:

'''
import os

# Definindo as variáveis
pessoa      = {}            # dicionário de pessoa
pessoas     = []            # lista de dicionários de pessoas
opcao       = 0             # opção do menu de escolhas
auto_id     = 0             # ID da pessoa cadastrada
execucao    = True          # faz com que o sistema contine executando


while execucao:
    os.system('cls')    # limpando a tela.

    print("#" * 24)
    print('**** MENU DE OPÇÕES ****')
    print("#" * 24)
    print("# 1. CADASTRO")
    print("# 2. PESQUISAR")
    print("# 3. EXCLUIR")
    print("# 4. LISTAR")
    print('# 5. SAIR')
    print("#" * 24)

    opcao = int(input("Digite a opção desejada: "))         # Temos um bug a ser resolvido aqui. Resolva em seu código.

    if opcao == 1:
        os.system('cls')    # limpando a tela.
        print("******** Cadastrar *********")
        pessoa['nome'] = input("Primeiro Nome: ")
        pessoa['segundo_nome'] = input("Segundo Nome: ")
        pessoa['sobrenome'] = input("sobrenome: ")
        pessoa['idade'] = input("idade: ")
        pessoa['auto_id'] = auto_id
        auto_id = auto_id + 1
        pessoas.append(pessoa.copy())                    # adiciona os dados para dentro da lista pessoa
        pessoa.clear()

    elif opcao == 2:
        os.system('cls')                                    # limpando a tela.
        print("******** Pesquisar Por Nome *********")        
        nome = input("Digite o nome a ser pesquisado: ")

        for p in pessoas:
            if p["nome"] == nome:
                print("Codigo: ", p["auto_id"])
                print("Primeiro Nome: ", p['nome'])
                print("Segundo Nome: ", p['segundo_nome'])
                print("Sobrenome: ", p['sobrenome'])
                print("Idade: ", p['idade'])
                print("=" * 10)

        os.system("pause")  # Pausa na tela
        
    elif opcao == 3:
        os.system('cls')    # limpando a tela.
        print("************** Excluir ************** ")
        nome = input("Digite o nome a ser pesquisado: ")
        for p in pessoas:
            if p["nome"] == nome:
                id = int(p["auto_id"])
                print("Código", p["auto_id"])
                print("Primeiro Nome: ", p['nome'])
                print("Segundo Nome: ", p['segundo_nome'])
                print("Sobrenome: ", p['sobrenome'])
                print("Idade: ", p['idade'])
                print("=" * 10)
        
        excluir = input("Deseja excluir o cadastro acima ? S, N: ")
        if excluir == "S":
            del pessoas[id]
        else:
            print("Não foi excluída")
            os.system("pause")

    elif opcao == 4:
        os.system('cls')    # limpando a tela.
        print("***** Listar *******")
        for p in pessoas:
            print("Código", p["auto_id"])
            print("Primeiro Nome: ", p['nome'])
            print("Segundo Nome: ", p['segundo_nome'])
            print("Sobrenome: ", p['sobrenome'])
            print("Idade: ", p['idade'])
            print("=" * 10)
        os.system("pause")

    elif opcao == 5:        
        os.system('cls')
        print("encerrando...")
        execucao = False

    else:
        print("Opção não encontrada")