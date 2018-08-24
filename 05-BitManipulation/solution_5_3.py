def as_bin_str(n):
    return '{0:b}'.format(n)


def get_bit_at_i(n, i):
    mask = 1 << i
    result = n & mask
    if result > 0:
        return 1
    return 0


def max_len(n):
    max_ = 0
    zero_flipped = False
    curr_len = 0

    for i in range(32):
        if get_bit_at_i(n, i) == 1:
            curr_len += 1
            prev = 1
        elif zero_flipped == False:
            curr_len += 1
            prev = 0
            zero_flipped = True
        elif prev == 0:
            curr_len = 1
        max_ = max(max_, curr_len)

    return max_


def main():

    x = 4
    assert max_len(x) == 2, 'Test 1 failed.'

    x = 2
    assert max_len(x) == 2, 'Test 2 failed.'

    x = 1
    assert max_len(x) == 2, 'Test 3 failed.'

    x = 9
    assert max_len(x) == 2, 'Test 4 failed.'

    x = 5
    assert max_len(x) == 3, 'Test 5 failed.'

    x = 923
    print(max_len(x))
    assert max_len(x) == 5, 'Test 6 failed.'


if __name__ == '__main__':
    main()
