

def fonte():
    """
    Seção 3: Modelagem de Dados - 22. Exercício Modelagem de Dados

    Empresa: Fabricante de picolé

    ------------------------------------------------- Picolés (dados) -------------------------------------------------
    1. água    2. ao leite

    ---------------------------------------------- Picolés (água) (dados) ----------------------------------------------
    1. sabor    2. ingredientes    3. preço    4. tipo da embalagem

    --------------------------------------------- Picolés (leite) (dados) ---------------------------------------------
    1. sabor    2. ingredientes    3. preço    4. tipo da embalagem

    --------------------------------------------- Pícolé (água) (aditivos) ---------------------------------------------
    1. vitaminas    2. sais minerais

    ----------------------------------------- Pícolé (água) (aditivos) (dados) -----------------------------------------
    1. nome    2. fórmula químca

    -------------------------------------------------- Pícolé (leite) --------------------------------------------------
    1. conservantes

    ------------------------------------------ Pícolé (leite) (conservantes) ------------------------------------------
    1. nome    2. Descrição

    ----------------------------------------------- Pícole (água) (lote) -----------------------------------------------
    1. normal

    ---------------------------------------------- Pícole (leite) (lote) ----------------------------------------------
    1. ao leite

    ----------------------------------------------- Revendedores (dados) -----------------------------------------------
    1. pessoa de contato    2. CNPJ    3. Razão Social

    ----------------------------------------------- Nota fiscal (dados) -----------------------------------------------
    1. data    2. valir    3. número de série    4. descrição
    """


def fonte_2():
    """ Seção 3: Modelagem de Dados - 23. Correção Exercício Modelagem de Dados """


def criar_modelo():
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
    """


def tutorial_procedimentos():
    """
    1. Encontrar as entidades    2. Definir os atributos    3. Definir os relacionamentos

    Entidades
    Picolés           || id, sabor, ingredientes, preço, tipo da embalagem
    Tipos de picolé   || id, nome
    Tipo de embalagem || id, nome
    """