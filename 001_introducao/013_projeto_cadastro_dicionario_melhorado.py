'''
PROGRAMA: DICIONÁRIOS EM PYTHON
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO: CÓDIGO MELHORADO PARA CADASTRO DE PESSOAS COM DICIONÁRIOS
INCLUIDO MELHORIAS NA PESQUISA, EXCLUSÃO E LISTAGEM DE PESSOAS ALÉM DE TRATAMENTO DE ERROS E FUNCIONALIDADES DE LIMPEZA E PAUSA
AGORA O PROGRAMA É MAIS ROBUSTO E FÁCIL DE USAR, COM MENOS PROBLEMAS DE ENTRADA INVÁLIDA E MELHOR USABILIDADE
UTILIZADO DEFINIÇÃO DE FUNÇÕES PARA LIMPAR A TELA E PAUSAR A EXECUÇÃO

Desenvolvido por: Everton William Constantino
Data: 03/06/2025
'''

import os

# Definindo as variáveis
pessoa      = {}            # dicionário de pessoa
pessoas     = []            # lista de dicionários de pessoas
auto_id     = 0             # ID da pessoa cadastrada
execucao    = True          # controle do loop principal

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("Pressione ENTER para continuar...")

while execucao:
    limpar()

    print("#" * 30)
    print('**** MENU DE OPÇÕES ****')
    print("#" * 30)
    print("# 1. CADASTRO")
    print("# 2. PESQUISAR")
    print("# 3. EXCLUIR")
    print("# 4. LISTAR")
    print('# 5. SAIR')
    print("#" * 30)

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("⚠️ Entrada inválida! Digite um número entre 1 e 5.")
        pausar()
        continue

    if opcao == 1:
        limpar()
        print("******** Cadastrar *********")
        pessoa['nome'] = input("Primeiro Nome: ")
        pessoa['segundo_nome'] = input("Segundo Nome: ")
        pessoa['sobrenome'] = input("Sobrenome: ")
        pessoa['idade'] = input("Idade: ")
        pessoa['auto_id'] = auto_id
        auto_id += 1
        pessoas.append(pessoa.copy())  # adiciona cópia do dicionário
        pessoa.clear()
        print("✅ Pessoa cadastrada com sucesso!")
        pausar()

    elif opcao == 2:
        limpar()
        print("******** Pesquisar Por Nome *********")
        nome = input("Digite o nome a ser pesquisado: ")
        encontrados = [p for p in pessoas if p.get("nome") == nome] # lista de pessoas com o nome pesquisado

        if encontrados:
            for p in encontrados:
                print(f"Código: {p['auto_id']}")
                print(f"Nome: {p['nome']} {p['segundo_nome']} {p['sobrenome']}")
                print(f"Idade: {p['idade']}")
                print("=" * 20)
        else:
            print("⚠️ Nenhuma pessoa encontrada com esse nome.")
        pausar()

    elif opcao == 3:
        limpar()
        print("************** Excluir **************")
        nome = input("Digite o nome a ser pesquisado para exclusão: ")
        encontrados = [p for p in pessoas if p.get("nome") == nome] # lista de pessoas com o nome pesquisado

        if encontrados:
            for p in encontrados:
                print(f"Código: {p['auto_id']}")
                print(f"Nome: {p['nome']} {p['segundo_nome']} {p['sobrenome']}")
                print(f"Idade: {p['idade']}")
                print("=" * 20)

            try:
                id_excluir = int(input("Digite o código da pessoa que deseja excluir: "))
                index = next((i for i, p in enumerate(pessoas) if p["auto_id"] == id_excluir), None)
                if index is not None:
                    confirmacao = input("Deseja excluir o cadastro acima? (S/N): ").strip().upper()
                    if confirmacao == "S":
                        del pessoas[index]
                        print("✅ Cadastro excluído com sucesso.")
                    else:
                        print("❌ Exclusão cancelada.")
                else:
                    print("⚠️ Código não encontrado.")
            except ValueError:
                print("⚠️ Código inválido.")
        else:
            print("⚠️ Nenhum cadastro encontrado com esse nome.")
        pausar()

    elif opcao == 4:
        limpar()
        print("******** Lista de Pessoas Cadastradas ********")
        if pessoas:
            for p in pessoas:
                print(f"Código: {p['auto_id']}")
                print(f"Nome: {p['nome']} {p['segundo_nome']} {p['sobrenome']}")
                print(f"Idade: {p['idade']}")
                print("=" * 20)
        else:
            print("⚠️ Nenhuma pessoa cadastrada.")
        pausar()

    elif opcao == 5:
        limpar()
        print("👋 Encerrando o programa... Até logo!")
        execucao = False

    else:
        print("⚠️ Opção inválida! Digite um número entre 1 e 5.")
        pausar()