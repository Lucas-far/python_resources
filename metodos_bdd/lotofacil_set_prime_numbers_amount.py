

def mtd_lotofacil_set_prime_numbers_amount(the_game, the_min: int = 5, the_max: int = 8):
    """"""

    prime_numbers_lotofacil = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    prime_numbers_box = []

    for number in the_game:
        if number in prime_numbers_lotofacil:
            prime_numbers_box.append(number)

    prime_numbers_box_size = len(prime_numbers_box)

    if the_min < prime_numbers_box_size <= the_max:
        return True  # if the amount of prime numbers in the game is between 6 to 8 (acceptable)
    return False     # if the amount of prime numbers in the game is between 1 to 5 or equals 9

    # return prime_numbers_box


# class LotofacilFindPrimeNumbers:
#
#     @property
#     def show_the_game(self):
#         return self.__the_game
#
#     @show_the_game.setter
#     def show_the_game(self, new_value):
#         self.__the_game = new_value
#
#     def __init__(self, the_game: list):
#         self.__the_game = the_game
#
#     def scan_game_for_prime_numbers(self):
#
#         prime_numbers_lotofacil = [2, 3, 5, 7, 11, 13, 17, 19, 23]
#         prime_numbers_box = []
#
#         for number in self.__the_game:
#             if number in prime_numbers_lotofacil:
#                 prime_numbers_box.append(number)
#
#         return prime_numbers_box


if __name__ == '__main__':

    structured = '------------------------------------- PROGRAMAÇÃO ESTRUTURAL -------------------------------------\n'
    oriented = '---------------------------------- PROGRAMAÇÃO ORIENTADA A OBJETOS ----------------------------------\n'

    # --------------------------------------------- PROGRAMAÇÃO ESTRUTURAL ---------------------------------------------
    # [2, 3, 5, 7, 11, 13, 17, 19, 23]
    primes_five = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]   # must be False
    primes_six = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]    # must be True
    primes_seven = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17]  # must be True
    primes_eight = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19]  # must be True
    primes_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23]   # must be False

    var = mtd_lotofacil_set_prime_numbers_amount(the_game=primes_five)
    var2 = mtd_lotofacil_set_prime_numbers_amount(the_game=primes_six)
    var3 = mtd_lotofacil_set_prime_numbers_amount(the_game=primes_seven)
    var4 = mtd_lotofacil_set_prime_numbers_amount(the_game=primes_eight)
    var5 = mtd_lotofacil_set_prime_numbers_amount(the_game=primes_nine)

    print(f'{structured} {var} {var2} {var3} {var4} {var5}')

    # ---------------------------------------- PROGRAMAÇÃO ORIENTADA A OBJETOS ----------------------------------------
    # an_object = LotofacilFindPrimeNumbers(the_game=_)
    # an_object_prime_numbers = an_object.scan_game_for_prime_numbers()
    # print(f'{oriented}{an_object_prime_numbers}')

    # print(an_object.show_the_game)
    # an_object.show_the_game = tuple(range(1, 16))
    # print(an_object.show_the_game)
