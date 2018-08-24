def insert_charset(st, idx):
    st[idx] = '0'
    idx -= 1
    st[idx] = '2'
    idx -= 1
    st[idx] = '%'
    idx -= 1
    return idx


def urlify(st, true_len):

    st = list(st)

    new_str_idx = len(st) - 1
    old_str_idx = true_len - 1

    while new_str_idx > 0:
        if st[old_str_idx] == ' ':
            new_str_idx = insert_charset(st, new_str_idx)
        else:
            st[new_str_idx] = st[old_str_idx]
            new_str_idx -= 1
        old_str_idx -= 1

    return ''.join(st)


def main():
    x = ''
    print(urlify(x, 0))
    assert urlify(x, 0) == '', 'Test 1 failed.'

    x = 'a'
    print(urlify(x, 1))
    assert urlify(x, 1) == 'a', 'Test 2 failed.'

    x = '   '
    print(urlify(x, 1))
    assert urlify(x, 1) == '%20', 'Test 3 failed.'

    x = 'ab ab  '
    print(urlify(x, 5))
    assert urlify(x, 5) == 'ab%20ab', 'Test 4 failed.'

    x = ' ab ab    '
    print(urlify(x, 6))
    assert urlify(x, 6) == '%20ab%20ab', 'Test 5 failed.'

    x = 'ab ab     '
    print(urlify(x, 6))
    assert urlify(x, 6) == 'ab%20ab%20', 'Test 6 failed.'


if __name__ == '__main__':
    main()
