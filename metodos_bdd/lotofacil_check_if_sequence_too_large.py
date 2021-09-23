

def mtd_check_if_sequence_too_large(the_game, first_index: int = 0, second_index: int = 1):
    """
    Check if a lotofacil game has a followed sequence larger than or equals to 7 numbers
    The typed parameters are supposed to be kept the way they are, in order to have the correct subtraction in the loop
    There are three examples as commentaries below showing how the methods works
    If the return has a string with 6 y (yyyyyy), it means the values form a sequence with at least 7 numbers in a row
    This (yyyyyy) based on Lotofacil, can be any long sequence between 1 to 25 (ex: 5, 6, 7, 8, 9, 10, 11)
    """
    box = []
    box2 = []
    while second_index < len(the_game):
        box.append((the_game[second_index] - the_game[first_index]) - 1)
        first_index += 1
        second_index += 1

    # EXAMPLE: box = [0, 0, 0, 0, 0, 0, 2, 1, 3, 0, 1, 1, 2, 0]

    for integer in box:
        if integer == 0:
            box2.append('y')
        else:
            box2.append('n')

    # ------------------------------------ EXAMPLE OF RESULT POST USE OF SYNTAX FOR ------------------------------------
    # box2 = ['y', 'y', 'y', 'y', 'y', 'y', 'n', 'n', 'n', 'y', 'n', 'n', 'n', 'y']

    box2_str = "".join(box2)  # ex: 'yyyyyynnnynnny'

    large_sequence_7 = 'yyyyyy'
    large_sequence_8 = 'yyyyyyy'
    large_sequence_9 = 'yyyyyyyy'

    if large_sequence_7 in box2_str or large_sequence_8 in box2_str or large_sequence_9 in box2_str:
        # print(box2_str)
        return False  # if the game sequence has at least 7 numbers in a row
    # print(box2_str)
    return True       # if the game sequence has less than 7 numbers in a row (acceptable)


if __name__ == '__main__':
    argument_6_in_a_row = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 17, 18, 19]  # must be true
    argument_7_in_a_row = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 20]   # must be false
    argument_8_in_a_row = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]    # must be false
    argument_9_in_a_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]     # must be false

    var = mtd_check_if_sequence_too_large(the_game=argument_6_in_a_row)
    var2 = mtd_check_if_sequence_too_large(the_game=argument_7_in_a_row)
    var3 = mtd_check_if_sequence_too_large(the_game=argument_8_in_a_row)
    var4 = mtd_check_if_sequence_too_large(the_game=argument_9_in_a_row)

    print(var, var2, var3, var4)
    # print(var)
    # print(var2)
    # print('yyyyyy' in var)
    # print('yyyyyy' in var2)
