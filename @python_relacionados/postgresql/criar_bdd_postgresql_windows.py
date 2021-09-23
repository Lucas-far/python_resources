

# Precisa ser lida, para melhor compreensão
def hierarquia():
    """
    Criação de um usuário -> Criação do servidor do usuário -> Criação do bdd dentro do servidor do usuário
    """


# Configuração da interface gráfica do PostgreSQL (Criação de um usuário) (Criação do servidor do usuário)
def parte_1():
    """
    • Abrir o software [ Pgadmin4 ] (aplicação web)
    • Na abertura, sempre será requisitado a senha da conta matriz configurada na instalação do PostgreSQL
    • Na lateral esquerda há um painel com um dropdown [ Servers ] que dá acesso a dropdowns aninhados

    ------------------------------------------------ Criando um usuário ------------------------------------------------
    • Servers -> PostgreSQL13 (servidor padrão) -> Login/Group Roles -> botão direto -> create -> login/group role

    CONFIGURAÇÃO
    • General     || Name     = nome do usuário novo
    • Definition  || Password = senha do usuário novo
    • Privileges  || Modificar para [ Yes ] as opções [ Can login? ] e [ Superuser? ]
    • [ Save ]

    ----------------------------------------- Criando um usuário (alternativo) -----------------------------------------
    • Essa configuração não é completa como a manual mencionada acima, portanto é menos recomendada
    • psql -U postgres
    • Inserir a senha do usuário matriz
    • CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    • ALTER USER nome do usuário novo WITH SUPERUSER;
    • \q
    • No PgAdmin, atualizar a página (o usuário criado aparecerá na lista de Group Roles)

    -------------------------------- Criando um servidor com as credenciais do usuário --------------------------------
    • Servers -> botão direito -> create -> server
    • A ideia é a de que o servidor seja configurado com as mesmas credenciais do usuário

    CONFIGURAÇÃO
    • General    || Name              = nome do usuário novo + server
    • Connection || Host name/address = localhost
    • Connection || Username          = nome do usuário novo
    • Connection || Password          = senha do usuário novo
    • [ Save ]
    """


# Configuração da interface gráfica do PostgreSQL (Criação do bdd dentro do servidor do usuário)
def parte_2():
    """
    • No PgAdmin, acessar o dropdown [ Servers ] e procurar pelo servidor do usuário criado
    • Botão direito no servidor do usuário -> Create -> Database
    • General || Database = inserir o nome do bdd (recomendação: nome do usuário_dtb_int)
    • [ Save ]
    """


# Integração do bdd PostgreSQL com um projeto que vai usá-lo (parte 1 - Instalação de dependências)
def parte_3():
    """
    • pip install psycopg2-binary
    • pip freeze > requirements.txt
    """


def settings():
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nome_do_bdd_criado_pelo_user',
            'USER': 'nome_do_user_onde_o_bdd_foi_criado',
            'PASSWORD': 'senha_do_user',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    """
