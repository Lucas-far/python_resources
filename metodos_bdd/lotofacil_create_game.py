

def mtd_lotofacil_create_game(length: int):
    """"""

    from random import choice

    card = [*range(1, 26)]  # Lotofácil possui 25 dezenas
    the_game = set({})      # Os números serão inseridos dentro desse conjunto vazio, que será incrementado logo abaixo

    while len(the_game) < length:
        the_game.add(choice(card))

    return the_game


class LotofacilCreateGame:

    @property
    def return_length(self) -> int:
        return self.__length

    @return_length.setter
    def return_length(self, new_value):
        self.__length = new_value

    def __init__(self, length: int):
        self.__length = length

    def add_numbers_to_set(self) -> set:
        from random import choice

        card = [*range(1, 26)]
        the_game = set({})

        while len(the_game) < self.__length:
            the_game.add(choice(card))

        return the_game


if __name__ == '__main__':
    structured = '------------------------------------- PROGRAMAÇÃO ESTRUTURAL -------------------------------------\n'
    oriented = '---------------------------------- PROGRAMAÇÃO ORIENTADA A OBJETOS ----------------------------------\n'

    # --------------------------------------------- PROGRAMAÇÃO ESTRUTURAL ---------------------------------------------
    object_main = mtd_lotofacil_create_game(length=15)
    print(f'{structured}{object_main}')

    # ---------------------------------------- PROGRAMAÇÃO ORIENTADA A OBJETOS ----------------------------------------
    an_object = LotofacilCreateGame(length=15)
    an_object_game = an_object.add_numbers_to_set()
    print(f'{oriented}{an_object_game}')
