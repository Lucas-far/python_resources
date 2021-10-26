

from metodos_bdd.lotofacil_find_prime_numbers import mtd_lotofacil_find_prime_numbers as primes
from metodos_bdd.lotofacil_horizontal_sequence import mtd_horizontal_sequence as horizontal
from metodos_bdd.lotofacil_vertical_sequence import mtd_vertical_sequence as vertical

dtb = [
    (2,3,4,5,6,8,9,10,11,12,18,19,20,21,25),
    (1,2,5,6,9,10,11,12,13,16,17,18,19,20,21),
    (1,2,3,7,8,12,13,14,15,16,18,20,23,24,25),
    (3,4,7,8,11,12,15,16,17,18,20,22,23,24,25),
    (1,3,4,5,6,7,8,9,10,12,14,15,20,23,24),
    (2,3,4,5,6,7,8,9,10,15,17,19,21,22,25),
    (2,5,6,9,10,11,12,15,16,17,18,20,21,22,23),
    (1,2,5,8,9,11,13,14,15,17,19,20,22,23,24),
    (2,3,5,6,8,9,11,13,15,16,17,19,21,24,25),
    (1,4,5,8,10,11,12,14,16,17,18,19,21,22,25)
]

ten_last_games = [dtb[0], dtb[1], dtb[2], dtb[3], dtb[4], dtb[5], dtb[6], dtb[7], dtb[8], dtb[9]]

ten_last_games_prime_numbers = [
    primes(dtb[0]), primes(dtb[1]), primes(dtb[2]), primes(dtb[3]), primes(dtb[4]), primes(dtb[5]), primes(dtb[6]),
    primes(dtb[7]), primes(dtb[8]), primes(dtb[9])
]

ten_last_games_horizontal_sequences = [
    horizontal(dtb[0]), horizontal(dtb[1]), horizontal(dtb[2]), horizontal(dtb[3]), horizontal(dtb[4]),
    horizontal(dtb[5]), horizontal(dtb[6]), horizontal(dtb[7]), horizontal(dtb[8]), horizontal(dtb[9]),
]

ten_last_games_vertical_sequences = [
    vertical(dtb[0]), vertical(dtb[1]), vertical(dtb[2]), vertical(dtb[3]), vertical(dtb[4]),
    vertical(dtb[5]), vertical(dtb[6]), vertical(dtb[7]), vertical(dtb[8]), vertical(dtb[9]),
]

if __name__ == '__main__':

    dez_ultimos_jogos = '------------------------------------- Dez últimos jogos -------------------------------------'
    dez_ultimos_jogos_n_primos = '------------------------ Dez últimos jogos (números primos) ------------------------'
    dez_ultimos_jogos_seq_horizontal = '----------------- Dez últimos jogos (sequências horizontais) -----------------'
    dez_ultimos_jogos_seq_vertical = '------------------- Dez últimos jogos (sequências verticais) -------------------'

    print([1], dez_ultimos_jogos)
    for game in ten_last_games:
        print(game)
    print('\n')

    print([2], dez_ultimos_jogos_n_primos)
    for game in ten_last_games_prime_numbers:
        print(game)
    print('\n')

    print([3], dez_ultimos_jogos_seq_horizontal)
    for game in ten_last_games_horizontal_sequences:
        print(game)
    print('\n')

    print([4], dez_ultimos_jogos_seq_vertical)
    for game in ten_last_games_vertical_sequences:
        print(game)
    print('\n')

    # print([2], ten_last_games_prime_numbers)
    # print([3], ten_last_games_horizontal_sequences)
    # print([4], ten_last_games_vertical_sequences)

    # number_of_games = len(dtb)
    # module_size = getsizeof(dtb)

    # relatorio = f"""
    # ---------------------------------------------------- RELATÓRIO ----------------------------------------------------
    # Número de jogos no banco de dados da lotofácil: {number_of_games}
    # Tamanho do arquivo: {module_size}
    #
    # ---------- RANK DAS DEZENAS (ORDENADO) ----------
    # 1: {n1}   2: {n2}   3: {n3}   4: {n4}   5: {n5}
    # 6: {n6}   7: {n7}   8: {n8}   9: {n9}   10: {n10}
    # 11: {n11}   12: {n12}   13: {n13}   14: {n14}   15: {n15}
    # 16: {n16}   17: {n17}   18: {n18}   19: {n19}   20: {n20}
    # 21: {n21}   22: {n22}   23: {n23}   24: {n24}   25: {n25}
    #
    # ---------- RANK DAS DEZENAS (DECRESCENTE) ----------
    # {rank_dezenas_decrescente}
    # """