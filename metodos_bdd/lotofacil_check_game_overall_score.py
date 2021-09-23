

def mtd_lotofacil_check_game_overall_score(the_game, games_compared):
    """"""

    similarities = []

    i = 0

    while i < len(games_compared):
        # Os jogos são tuplas, mas para saber a interseção é preciso convertê-los para classe [ set() ]
        # O método [ intersection() ] está dentro do construtor [ len() ] para que o retorno seja somente um inteiro
        # O construtor [ str() ] está sendo usado, pois será preciso contar o número de ocorrências abaixo
        similarities.append(str(len(set(the_game).intersection(set(games_compared[i])))))
        i += 1

    # A contagem é feita aqui
    accuracy_6 = similarities.count('6')
    accuracy_7 = similarities.count('7')
    accuracy_8 = similarities.count('8')
    accuracy_9 = similarities.count('9')
    accuracy_10 = similarities.count('10')
    accuracy_11 = similarities.count('11')
    accuracy_12 = similarities.count('12')
    accuracy_13 = similarities.count('13')
    accuracy_14 = similarities.count('14')
    accuracy_15 = similarities.count('15')

    report = f"""
    Jogo analisado: {the_game}
    ----------------------------- Pontuações em comparação com todos os jogos da Lotofácil -----------------------------
    6  pontos || {accuracy_6} vezes
    7  pontos || {accuracy_7} vezes
    8  pontos || {accuracy_8} vezes
    9  pontos || {accuracy_9} vezes
    10 pontos || {accuracy_10} vezes
    11 pontos || {accuracy_11} vezes
    12 pontos || {accuracy_12} vezes
    13 pontos || {accuracy_13} vezes
    14 pontos || {accuracy_14} vezes
    15 pontos || {accuracy_15} vezes"""

    return report
    # codigo = [n, (6, _6), (7, _7), (8, _8), (9, _9), (10, _10), (11, _11), (12, _12), (13, _13), (14, _14), (15, _15)]
    # return codigo


if __name__ == '__main__':
    from metodos_bdd.lotofacil_database import dtb
    target_game = {1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25}
    print(result := mtd_lotofacil_check_game_overall_score(the_game=target_game, games_compared=dtb))
