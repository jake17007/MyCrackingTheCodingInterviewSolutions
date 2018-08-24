def print_bin(flt):
    s = '.'
    i = 1
    while i <= 32:
        curr = 1 / (2 ** i)
        if flt - curr >= 0:
            flt -= curr
            s += '1'
        else:
            s += '0'
        i += 1
    if flt == 0:
        print(s)
    else:
        print('ERROR')


def main():
    print('.01')
    print_bin(.25)
    print('\n')

    print('.011')
    print_bin(.75)
    print('\n')

    print('All zeros except last one')
    print_bin(1 / 2 ** 32)
    print('\n')

    print('ERROR')
    print_bin(1 / 2 ** 33)
    print('\n')

    print('ERROR')
    print_bin(.99999999999999)
    print('\n')

if __name__ == '__main__':
    main()
