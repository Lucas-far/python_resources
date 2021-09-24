

def fonte():
    """ Seção 3: Modelagem de Dados - 22. Exercício Modelagem de Dados """


def fonte_2():
    """ Seção 3: Modelagem de Dados - 23. Correção Exercício Modelagem de Dados """


def aula_22():
    """
    Empresa: Fabricante de picolé

    Picolés (dados)                  1. água              | 2. ao leite        |                    |
    Picolés (água) (dados)           1. sabor             | 2. ingredientes    | 3. preço           | 4. tipo embalagem
    Picolés (leite) (dados)          1. sabor             | 2. ingredientes    | 3. preço           | 4. tipo embalagem
    Pícolé (água) (aditivos)         1. vitaminas         | 2. sais minerais   |                    |
    Pícolé (água) (aditivos) (dados) 1. nome              | 2. fórmula química |                    |
    Pícolé (leite)                   1. conservantes      |                    |                    |
    Pícolé (leite) (conservantes)    1. nome              | 2. Descrição       |                    |
    Pícole (água) (lote)             1. normal            |                    |                    |
    Pícole (leite) (lote)            1. ao leite          |                    |                    |
    Revendedores (dados)             1. pessoa de contato | 2. CNPJ            | 3. Razão Social    |
    Nota fiscal (dados)              1. data              | 2. valir           | 3. número de série | 4. descrição
    """


def criar_modelo_mysql_workbench():
    """
    - Abertura do MySQL Workbench
    - Menu lateral [ item do meio = criar modelos ]
    - Botão de +
    - Duplo clique no item abaixo do texto [ Physical Schemas ]
    - Inserir um nome ao campo [ Name ]
    - Clicar no ícone do [ disquete ]
    - Inserir o nome novamente e [ Salvar ]
    - Fechar a janela que foi aberta
    - Duplo clique em [ Add diagram + ]

    --------------------------------------------------- CRIAR TABELA ---------------------------------------------------
    Na aba [ Diagram ] temos um conjunto de dropdowns
    Escolher o dropdown [ place a new table = T ] e depois clique na tela do diagrama, para que a tabela apareça
    Para cada nova tabela, o procedimento deve ser repetido

    ------------------------------------------------ CONFIGURAR TABELA ------------------------------------------------
    Com a tabela inserida na diagrama, um clique duplo na sua aba abrirá as configurações

    CAMPOS COMUNS A SEREM PREENCHIDOS:
    1. Table name    2. Column name    3. Datatype    4. Caixas de marcar    5. Foreign Keys

    ITEM 4 (LEGENDAS COMUNS)
    1. PK = chave primária    2. NN = campo não nulo    3. AI = auto incremento

    ITEM 5 (DETALHES)
    O item 5 é usado para criar relacionamentos entre tabelas (uma chave primária é usada como referência em outra)
    As opções nesse item são: [ Foreign keys name ] [ Referenced table ] [ Foreign key columns ] [ Referenced columns ]
    No Ubuntu, há uma criação de sintaxe automática o item [ Foreign keys name ]
    Essa sintaxe costuma ser [ fk_nome_da_tabela_int ]
    A aba [ Referenced table ] faz referência à tabela que receberá a chave primária de outra tabela
    A aba [ Foreign key columns ] faz referência ao atributo da tabela que receberá a chave primária
    A aba [ Referenced column ] faz referência a chave primária a ser referência para uma outra tabela
    """


def aula_23():
    """
    -------------------------------- PROCEDIMENTOS PARA A CRIAÇÃO DE UM BANCO DE DADOS --------------------------------
    1. Encontrar as entidades
    2. Definir os atributos
    3. Definir os relacionamentos
    4. Atentar as formas normais

    --------------------------- ORGANIZAÇÃO DAS ENTIDADES, SEUS ATRIBUTOS E RELACIONAMENTOS ---------------------------
    Entidades
    Picolés             || id, id sabor, preço, id tipo da embalagem
    Tipos de picolé     || id, nome
    Tipo de embalagem   || id, nome
    Ingredientes        || id, nome
    Sabor               || id, nome
    Ingredientes picolé || id, id ingrediente, id picolé
    Aditivos            || id, nome, fórmula química
    Conservantes        || id, nome, descrição
    Aditivos picolé     || id, id aditivo, id picolé
    Conservantes picolé || id, id conservante, id picolé
    Lotes               || id, id tipo picolé, quantidade
    Nota fiscal         || id, data, valor, número de série, descrição, id revendedor
    Lotes nota fiscal   || id, id lote, id nota fiscal
    Revendedor          || id, contato, cnpj, razão social
    """


# 51:02
def aula_23_procedimentos():
    """
    DETALHE: Atributos não numéricos parecem ser incongruentes como atributos de uma tabela matriz (que parece guardar
             somente atributos numéricos), por isso eles estão sendo segregados em tabelas, contendo atributos numéricos
             como chaves primaria, e o atributo não numérico em si inserido

             Tabela matriz possui variados atributos numéricos (começados com id_) que são referênciados em outras
             tabelas para chamar um atributo não numérico dentro delas

    TABELA                           NOME DO CAMPO          TIPO      CARACTERÍSTICAS
    1.1 picoles                    | id                   | INT     | PK NN AI
    2.1 sabores                    | id                   | INT     | PK NN AI
    2.2 sabores                    | nome                 | VARCHAR | NN
    3.1 tipos_embalagem            | id                   | INT     | PK NN AI
    3.2 tipos_embalagem            | nome                 | VARCHAR | NN
    1.2 picoles                    | preco                | DECIMAL | NN
    1.3 picoles                    | id_sabor             | INT     | NN
    1.4 picoles                    | id_tipo_embalagem    | INT     | NN
    4.1 tipos_picole               | id                   | INT     | PK NN AI
    4.2 tipos_picole               | nome                 | VARCHAR | NN
    1.5 picoles                    | id_tipo_picole       | INT     | NN
    5.1 ingredientes               | id                   | INT     | PK NN AI
    5.2 ingredientes               | nome                 | VARCHAR | NN
    6.1 ingredientes_picole        | id                   | INT     | PK NN AI
    6.2 ingredientes_picole        | id_ingrediente       | INT     | NN
    6.3 ingredientes_picole        | id_picole            | INT     | NN
    7.1 aditivos_nutritivos        | id                   | INT     | PK NN AI
    7.2 aditivos_nutritivos        | nome                 | VARCHAR | NN
    7.3 aditivos_nutritivos        | formula_quimica      | VARCHAR | NN
    ESCRITOS, MAS NÃO CRIADOS
    aditivos_nutritivos_picole | id                   | INT     | PK NN AI
    aditivos_nutritivos_picole | id_aditivo_nutritivo | INT     | NN
    aditivos_nutritivos_picole | id_picole            | INT     | NN

    A partir da tabela        (7) [ picoles ]
    Criar chave estrangeira   (7) [ fk_picoles_1 ]
    Vindo da tabela           (2) [ sabores ]
    Referenciando o atributo  (7) [ id_sabor ] da tabela [ picoles ]
    Pela chave primária       (2) [ id ] da tabela [ sabores ]

    A partir da tabela        (8) [ picoles ]
    Criar chave estrangeira   (8) [ fk_picoles_2 ]
    Vindo da tabela           (4) [tipos_embalagem ]
    Referenciando o atributo  (8) [ id_tipo_embalagem ] da tabela [ picoles ]
    Pela chave primária       (4) [ id ] da tabela [ tipos_embalagem ]

    A partir da tabela       (11) [ picoles ]
    Criar chave estrangeira  (11) [ fk_picoles_3 ]
    Vindo da tabela          (9)  [ tipos_picole ]
    Referenciando o atributo (11) [ id_tipo_picole ] da tabela [ picoles ]
    Pela chave primária      (9)  [ id ] da tabela [ tipos_picole ]

    A partir da tabela       (15) [ ingredientes_picole ]
    Criar chave estrangeira  (15) [ fk_ingredientes_picole_1 ]
    Vindo da tabela          (12) [ ingredientes ]
    Referenciando o atributo (15) [ id_ingrediente ] da tabela [ ingredientes_picole ]
    Pela chave primária      (12) [ id ] da tabela [ ingredientes ]

    A partir da tabela       (16) [ ingredientes_picole ]
    Criar chave estrangeira  (16) [ fk_ingredientes_picole_2 ]
    Vindo da tabela          (1)  [ picoles ]
    Referenciando o atributo (16) [ id_picole ] da tabela [ ingredientes_picole ]
    Pela chave primária      (1)  [ id ] da tabela [ picoles ]
    """
    # A partir da tabela          () []
    # Criar chave estrangeira     []
    # Requisitar da tabela        () []
    # Para referenciar o atributo () []
    # A chave primária            () []
