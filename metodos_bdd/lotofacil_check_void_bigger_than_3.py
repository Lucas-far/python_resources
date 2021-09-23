

def mtd_lotofacil_check_void_bigger_than_3(the_game, first_index: int = 0, second_index: int = 1):
    """
    Check if a lotofacil game has a void bigger than 3 slots, if integer <= 4 is in the return: True
    The typed parameters are supposed to be kept the way they are, in order to have the correct subtraction in the loop
    """
    voids_not_allowed = (4, 5, 6, 7)
    box = []
    while second_index < len(the_game):
        box.append((the_game[second_index] - the_game[first_index]) - 1)
        first_index += 1
        second_index += 1

    for number in box:
        if number in voids_not_allowed:
            print(box)
            return False  # if the void of the calculus is >= 4, then return false
    print(box)
    return True           # if the game is standard, acceptable


if __name__ == '__main__':

    void_3 = [1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]   # 1 to 5 = 2, 3, 4 = void of 3 = True
    void_4 = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # 5 to 10 = 6, 7, 8, 9 = void of 4 = False

    var = mtd_lotofacil_check_void_bigger_than_3(the_game=void_3)
    var2 = mtd_lotofacil_check_void_bigger_than_3(the_game=void_4)

    print(var)
    print(var2)
