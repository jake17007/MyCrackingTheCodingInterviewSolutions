def has_all_unique(the_str):
    seen_chars = {}
    for i in range(len(the_str)):
        if the_str[i] in seen_chars:
            return False
        else:
            seen_chars[the_str[i]] = 1
    return True


def test_has_all_unique():
    tests = [('', True),
             ('A', True),
             ('AA', False),
             ('ABA', False),
             ('AB', True)]
    for i, test in enumerate(tests, start=1):
        assert has_all_unique(test[0]) == test[1], 'Test {} failed.'.format(i)
