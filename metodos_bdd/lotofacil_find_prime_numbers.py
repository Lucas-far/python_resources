

def mtd_lotofacil_find_prime_numbers(the_game):
    """"""

    prime_numbers_lotofacil = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    prime_numbers_box = []

    for number in the_game:
        if number in prime_numbers_lotofacil:
            prime_numbers_box.append(number)

    return prime_numbers_box


if __name__ == '__main__':
    argument = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23]
    var = mtd_lotofacil_find_prime_numbers(the_game=argument)
    print(var)
