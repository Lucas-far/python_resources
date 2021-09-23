

def mtd_vertical_sequence(the_game):
    """"""

    line1, line2, line3, line4, line5 = 0, 0, 0, 0, 0
    line1_numbers = [1, 6, 11, 16, 21]
    line2_numbers = [2, 7, 12, 17, 22]
    line3_numbers = [3, 8, 13, 18, 23]
    line4_numbers = [4, 9, 14, 19, 24]
    line5_numbers = [5, 10, 15, 20, 25]

    for number in the_game:
        if number in line1_numbers:
            line1 += 1
        elif number in line2_numbers:
            line2 += 1
        elif number in line3_numbers:
            line3 += 1
        elif number in line4_numbers:
            line4 += 1
        elif number in line5_numbers:
            line5 += 1

    result = [line1, line2, line3, line4, line5]
    return result


if __name__ == '__main__':
    from metodos_bdd.lotofacil_database import ten_last_games
    from lotofacil_sample_game import _

    ten_last_games_horizontal_sequence = [
        mtd_vertical_sequence(the_game=ten_last_games[0]),
        mtd_vertical_sequence(the_game=ten_last_games[1]),
        mtd_vertical_sequence(the_game=ten_last_games[2]),
        mtd_vertical_sequence(the_game=ten_last_games[3]),
        mtd_vertical_sequence(the_game=ten_last_games[4]),
        mtd_vertical_sequence(the_game=ten_last_games[5]),
        mtd_vertical_sequence(the_game=ten_last_games[6]),
        mtd_vertical_sequence(the_game=ten_last_games[7]),
        mtd_vertical_sequence(the_game=ten_last_games[8]),
        mtd_vertical_sequence(the_game=ten_last_games[9]),
    ]
    print(ten_last_games_horizontal_sequence)

    # ----- Análise de um jogo aleatório para saber se sua sequência horizontal está entre as dos 10 últimos jogos -----
    var = mtd_vertical_sequence(the_game=_)
    print(var)
    print(var in ten_last_games_horizontal_sequence)
