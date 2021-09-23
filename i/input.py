

"""
Objetivo:
    entrada de texto para coletar dados externos de um usuário para ser exibido em algum algoritmo

Objetivo 2:
    entrada de texto para coletar dados externos de um usuário para ser salvo em algum documento

Observação:
    1. O valor é passado no parâmetro do método, podendo ser string literal ou em variável
    2. O input pode receber cast para variar a classe padrão (string),
"""

from os import chdir

# Exemplos comuns de conversão
"int(input()), str(input()), float(input()), list(input()), tuple(input())"

# Formas de usar input mais atuais
# print(nome := input('(1) Qual o seu nome?\n-> '))                         # input declarado e com par literal
# print(pergunta := '(2) Qual o seu nome?\n-> ', nome2 := input(pergunta))  # input declarado e com par declarado
# input('(3) Qual o seu nome?\n-> ')                                        # input literal e com par literal
# input(f"(4) {(pergunta := 'Qual o seu nome?')}\n-> ")                     # input literal e com par declarado

"Para usar inputs com perguntas curtas, é melhor usar:"  # input declarado e com par literal

# Formas de mostrar dados de um input
v, v2 = 'Python', 'Django'
print([1], '%s' % v)
print([2], '%s %s' % (v, v2))
print([3], '{}'.format(v))
print([4], '{} {}'.format(v, v2))
print([5], f'{v}')
print([6], f'{v} {v2}')

# Minha forma de usar input (contexto de string)
input_name: str = ''
def coletar_dados() -> None:
    """"""
    global input_name
    input_text = \
        f"""
        Qual o seu nome? 
        1. Clique na seta abaixo
        2. Digite seu nome (letras maiúscula após cada palavra)
        3. Aperte ENTER
        -> """
    n = [str(x) for x in range(1, 10)]
    index = 0
    while True:
        input_name = input(input_text)
        while index < len(input_name):
            if input_name[index] in n:
                print('Dado impróprio')
                coletar_dados()
                index = 0
                break
            else:
                index += 1
        break
coletar_dados()
