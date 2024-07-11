def game(number):
    n = int(str(number)[0]) - int(str(number)[1])
    return n if n > 0 else -1 * n

