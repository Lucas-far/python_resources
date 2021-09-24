

# Procedimentos não mandatórios que recomenda-se saber (após instalar o GIT)
def obs():
    """
    git config --global user.name "seu_user"      git config user.name (verificar)
    git config --global user.email "seu_email"    git config user.email (verificar)
    git config --list                             verificar outros comandos GIT
    """


# Este procedimento necessita uma chave ssh criada e vinculada a sua conta Github [ criar_chave_ssh_windows.py ]
def parte_1():
    """
    Ir ao Github e criar um repositório virtual

    ------------------------------ CASO O REPOSITÓRIO LOCAL SEJA EXISTENTE (COM ARQUIVOS) ------------------------------
    Criar o repositório ignorando os arquivos de configuração [ README.MD ] [ .gitignore ] [ LICENSE ]
    Copiar o link SSH que aparece após a criação do repositório

    git init
    git remote add origin link_ssh
    git add .
    git commit -m 'first commit'
    git branch -M main
    git push -u origin main

    ---------------------------------------- CASO O REPOSITÓRIO LOCAL SEJA NOVO ----------------------------------------
    Criar o repositório adicionando os arquivos de configuração [ README.MD ] [ .gitignore ] [ LICENSE ]
    git init

    git add .
        • No Windows, o ambiente virtual pelo pycharm já vêm configurado e ativado, então cria-se um arquivo qualquer
          substituindo o . pelo nome do arquivo.formato

        • No Ubuntu, como o ambiente virtual não é criado e ativado naturalmente, a criação de um arquivo devia ser ele
            -> python3 -m venv .venv
            -> source .venv/bin/activate

    git commit -m "first commit"
    git branch -M main
    git remote add origin link_ssh
    git push -u origin main
    """
