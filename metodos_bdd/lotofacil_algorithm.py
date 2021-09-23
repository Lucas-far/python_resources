

from datetime import datetime

from metodos_bdd.lotofacil_database import (ten_last_games_prime_numbers,
                                            ten_last_games_horizontal_sequences,
                                            ten_last_games_vertical_sequences)

from metodos_bdd.lotofacil_database import dtb
from metodos_bdd.painter_random import mtd_painter_random

from metodos_bdd.lotofacil_create_game import mtd_lotofacil_create_game
from metodos_bdd.lotofacil_horizontal_sequence import mtd_horizontal_sequence
from metodos_bdd.lotofacil_vertical_sequence import mtd_vertical_sequence
from metodos_bdd.lotofacil_check_void_bigger_than_3 import mtd_lotofacil_check_void_bigger_than_3
from metodos_bdd.lotofacil_check_if_sequence_too_large import mtd_check_if_sequence_too_large
from metodos_bdd.lotofacil_set_prime_numbers_amount import mtd_lotofacil_set_prime_numbers_amount
from metodos_bdd.lotofacil_find_prime_numbers import mtd_lotofacil_find_prime_numbers
from metodos_bdd.lotofacil_check_game_overall_score import mtd_lotofacil_check_game_overall_score

number_of_games = int(input('Quantos jogos?\n-> '))
attempts = 0
counter = 0
algorithm_start = datetime.now()
progress_frame = f'------- Tentativas: {attempts} | Jogos registrados: {counter}/{number_of_games} -------'

while counter < number_of_games:

    game_created = mtd_lotofacil_create_game(length=15)
    game_created = list(game_created)

    game_created_horizontal_sequence = mtd_horizontal_sequence(the_game=game_created)                  # list
    game_created_vertical_sequence = mtd_vertical_sequence(the_game=game_created)                      # list
    game_created_voids = mtd_lotofacil_check_void_bigger_than_3(the_game=game_created)                 # bool: True
    game_created_sequence_in_a_row = mtd_check_if_sequence_too_large(the_game=game_created)            # bool: True
    game_created_prime_numbers_amount = mtd_lotofacil_set_prime_numbers_amount(the_game=game_created)  # bool: True
    game_created_prime_numbers = mtd_lotofacil_find_prime_numbers(the_game=game_created)

    game_created_overall_score = mtd_lotofacil_check_game_overall_score(the_game=game_created, games_compared=dtb)

    print(f"""
    Sequência de 15 números que representa um jogo dessa loteria
    {mtd_painter_random(label=str(game_created))}""")

    print(f"""
    Lista contendo 5 inteiros representando a quantidade de cada número nas partes horizontais do volante 
    {mtd_painter_random(label=str(game_created_horizontal_sequence))}""")

    print(f"""
    Lista contendo 5 inteiros representando a quantidade de cada número nas partes verticais do volante 
    {mtd_painter_random(label=str(game_created_vertical_sequence))}""")

    print(f"""
    Cálculo de índices, por exemplo, i[1] - i[0]...i[2] - i[1] e assim suscetivamente
    Os cálculos são inseridos em um lista, que será percorrida e verificada
    Se o jogo possuir um vácuo normal (até 3):  retorno é True
    Se o jogo possuir um vácuo normal (+ de 3): retorno é False
    {mtd_painter_random(label=str(game_created_voids))}""")

    print(f"""
    Se a sequência de números seguidos for igual ou maior que 7: retorna True
    Se a sequência de números seguidos menor que 7:              retorna False
    {mtd_painter_random(label=str(game_created_sequence_in_a_row))}""")

    print(f"""
    Se a quantidade de números primos no jogo for entre 6 para 8:      retorno é True 
    Se a quantidade de números primos no jogo for entre 1 para 5 ou 9: retorno é False 
    {mtd_painter_random(label=str(game_created_prime_numbers))}""")

    if game_created_voids:
        if game_created_sequence_in_a_row:
            if game_created_prime_numbers_amount:

                if game_created_horizontal_sequence not in ten_last_games_horizontal_sequences:
                    if game_created_vertical_sequence not in ten_last_games_vertical_sequences:
                        if game_created_prime_numbers not in ten_last_games_prime_numbers:

                            if 0 not in game_created_horizontal_sequence:
                                if 0 not in game_created_vertical_sequence:

                                    counter += 1
                                    print(game_created_overall_score)
                                    with open('games_storage.txt', 'a') as doc:
                                        doc.write('\n')
                                        doc.write(str('    Seq. horizontal: '))
                                        doc.write(str(game_created_horizontal_sequence))
                                        doc.write('\n')
                                        doc.write(str('    Seq. vertical: '))
                                        doc.write(str(game_created_vertical_sequence))
                                        doc.write('\n')
                                        doc.write(str(game_created_overall_score))
                                        doc.write('\n')

    else:
        attempts += 1
        print(progress_frame)
