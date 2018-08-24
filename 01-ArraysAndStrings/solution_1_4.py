def is_odd(n):
    if n % 2 == 0:
        return False
    return True


def is_palin_perm(s):
    if s == '':
        return True

    s = s.lower()
    max_char = max([ord(ch) for ch in list(s)])
    counts = [0] * (max_char + 1)
    for ch in list(s):
        counts[ord(ch)] += 1

    num_odd_counts = 0
    for cnt in counts:
        if cnt != 0 and is_odd(cnt):
            num_odd_counts += 1

    if num_odd_counts > 1:
        return False
    return True


def main():

    s = ''
    result = is_palin_perm(s)
    assert result is True, 'Test 1 failed.'

    s = 'a'
    result = is_palin_perm(s)
    assert result is True, 'Test 2 failed.'

    s = 'ab'
    result = is_palin_perm(s)
    assert result is False, 'Test 3 failed.'

    s = 'aa'
    result = is_palin_perm(s)
    assert result is True, 'Test 4 failed.'

    s = 'aba'
    result = is_palin_perm(s)
    assert result is True, 'Test 5 failed.'

    s = 'aabbb'
    result = is_palin_perm(s)
    assert result is True, 'Test 6 failed.'

    s = 'aabb'
    result = is_palin_perm(s)
    assert result is True, 'Test 7 failed.'

    s = 'aa bb'
    result = is_palin_perm(s)
    assert result is True, 'Test 8 failed.'

    s = 'Aa'
    result = is_palin_perm(s)
    assert result is True, 'Test 8 failed.'


if __name__ == '__main__':
    main()
