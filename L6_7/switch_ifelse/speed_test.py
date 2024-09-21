
def test_if_else(x):

    if x == 10:
        return 'A'
    elif x == 9:
        return 'B'
    elif x == 8:
        return 'C'
    elif x == 7:
        return 'D'
    elif x == 6:
        return 'E'
    elif x == 5:
        return 'F'
    elif x == 4:
        return 'G'
    elif x == 3:
        return 'G'
    elif x == 2:
        return 'I'
    elif x == 1:
        return 'J'
    elif x == 0:
        return 'K'
    else:
        return 'ERROR'


def test_match(x):
    match x:
        case 10:
            return 'A'
        case 9:
            return 'B'
        case 8:
            return 'C'
        case 7:
            return 'D'
        case 6:
            return 'E'
        case 5:
            return 'F'
        case 4:
            return 'G'
        case 3:
            return 'G'
        case 2:
            return 'I'
        case 1:
            return 'J'
        case 0:
            return 'K'
        case _:
            return 'ERROR'


def test():
    print('MATCH')
    for i in range(100000000):
        # test_if_else(i % 10)
        test_match(i % 10)


test()
