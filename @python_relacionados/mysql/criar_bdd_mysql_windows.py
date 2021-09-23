

# Configuração de um usuário novo através do usuário matriz
def parte_1():
    """
    • mysql -u root -p
    • Inserir a senha configurado na instalação

    • CREATE USER 'nome do usuário novo'@'localhost' IDENTIFIED BY 'senha desejada';
        Se nada tiver sido feito errado, o retorno deve ser [ Query OK, 0 rows affected ]

    • exit
    • mysql -u usuário novo -p
    • Inserir a senha configurado para este usuário novo

    ---------------------------------------------------- PROBLEMAS ----------------------------------------------------
    • Independente de estar logado no usuário 'root' ou no novo, o comando 'GRANT' parece não funcionar
    • O comando configura para que um usuário novo tenha os mesmo privilégios do usuário matriz

        GRANT ALL PRIVILEGES ON *.* TO 'nome do usuário novo' WITH GRANT OPTION;
        FLUSH PRIVILEGES

    ------------------------------------------------- SOLUÇÃO PESSOAL -------------------------------------------------
    • Antes de mais nada, é preciso que um usuário novo já tenha sido criado pelo usuário matriz
    • Entrar no [ MySQL Workbench ], logar na minha conta 'root'
    • Ao logar, há um painel esquerdo [ MANAGEMENT - Users and Privileges ]
    • No painel, aparecem cada um dos usuários já criados, além do 'root'
    • Clicar no nome do usuário a ser alterado e depois clicar na aba [ administrative roles ]
    • Marcar a primeira caixa (que marcará todas as outras) e clicar em [ apply ]
    """


def parte_2():
    """
    • É preciso que um usuário já tenha sido criado pelo usuário matriz, para dar continuidade
    • Abrir o MySQL Workbench
    • Em [ MySQL Connections ], clicar no ícone [ + ]
    • Preencher os campos: [ Connection name ] [ Username ] [ Password ]
    • Clicar em [ Test Connection ] e é esperado que não retorne um erro
    • Clicar em [ OK ]
    • No painel, abaixo de [ MySQL Connections ] deve ter sido criado o usuário existente que você configurou
    • Clicar neste usuário e digitar a senha
    • Na abertura, na parte branca da tela, clique após o número 1 e digite [ CREATE DATABASE nome_do_bdd; ]
    • Clique no ícone do [ raio ] que está logo acima da tela branca, para salvar a criação desse banco de dados
    """


# Integração do bdd MySQL com um projeto que vai usá-lo (parte 1 - Instalação de dependências)
def parte_3():
    """
    • OBS: Antes de fazer os procedimentos, é preciso que um projeto Django tenha sido minimamente configurado
    • pip install mysqlclient PyMySQL (talvez a segunda dependência não precise ser adicionada)
    • pip freeze > requirements.txt
    """


# Configuração do banco de dados em um projeto Django [ NAME = nome do bdd criado na parte 1 ]
def pp_settings():
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nome_do_bdd_criado_pelo_user',
            'USER': 'nome_do_user_que_criou_o_bdd',
            'PASSWORD': 'senha_do_user_que_criou_o_bdd',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    """
