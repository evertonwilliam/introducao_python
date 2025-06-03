Última versão: <!--version-start--> 1.0.2 <!--version-end-->

# Linguagem Python
Aprendendo Python na prática

# Criação das branchs:

## Criar e mudar para a branch Desenvolvimento:
```terminal
git checkout -b desenvolvimento
```

## Empurrar a nova branch para o github
O -u faz com que essa branch se torne a branch padrão de push e pull localmente.
```terminal
git push -u origin desenvolvimento
```

## Trabalhe normalmente no ambiente de desenvolvimento
Sempre que for trabalhar, confirme que está na branch certa com o comando:
```terminal
git branch
```

## Configure o VSCode para sempre enviar para desenvolvimento
O VSCode usa o Git configurado localmente. Ao executar:
```terminal
git push
```

## Criando alias para efetuar merge no Master
```terminal
git config --global alias.deploy "!git checkout master && git merge desenvolvimento && git push origin master && git checkout desenvolvimento"
```

## Efetuando o Deploy
```terminal
git deploy
```

## Quando quiser subir para produção (master)
```terminal
git checkout main
git merge desenvolvimento
git push origin main
```

# Configurações do Python:
```terminal
pip install -r requirements.txt
pip freeze > requirements.txt
```

# Estrutura
Abaixo segue a explicação da estrutura dos arquivos existentes no diretório.

## Diretório .github
 Arquivo: *atualizar_versao.yml*
- Este arquivo tem a finalidade de efetuar o versionamento automatizado no github

## Diretório 100_files
- Contém os arquivos de imagem dos aplicativos

## Diretório 001_introducao
- Contém os arquivos de estudo introdutório da linguagem Python