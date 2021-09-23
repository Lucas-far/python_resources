

"""
Objetivo:
    arredondar um dado flutuante para o seu valor inteiro mais próximo

Objetivo 2:
    diminuir casas decimais de uma classe flutuante

Observação:
    1. se a porção decimal for acima de .4, arredonda-se para o valor inteiro seguinte
    2. se a porção decimal for abaixo de .4, arredonda-se para o valor inteiro anterior
    3. há um parâmetro 2, sendo ele usado no objetivo 2
"""

# @float

def scan(classe, dado):
    try:
        print(classe, round(dado))
    except TypeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))

scan('booleano', True)
scan('complexo', 7.7654j)
scan('dicionário', {'c': 'v'})
scan('flutuante', 7.7654)
scan('inteiro', 7)
scan('lista', ['l'])
scan('nenhum', None)
scan('range', range(1, 4))
scan('conjunto', {'cj'})
scan('string', 's')
scan('tupla', ('t',))

print([1], round(17.4))
print([2], round(17.7))
print([3], round(17.4321, 1))
print([4], round(17.4321, 2))
