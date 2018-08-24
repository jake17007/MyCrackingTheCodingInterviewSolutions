def put_in_map(map, x):
    prev = map.get(x)
    if prev:
        map[x] = prev + 1
    else:
        map[x] = 1


def check_out_map(map, y):
    prev = map.get(y)
    if not prev:
        return False
    if prev < 1:
        return False
    map[y] = prev - 1
    return True


def check_if_perm(a, b):
    if len(a) != len(b):
        return False

    map = {}
    for i in range(len(a)):
        put_in_map(map, a[i])

    for j in range(len(b)):
        result = check_out_map(map, b[j])
        if result is False:
            return result

    return result


def main():
    pass


if __name__ == '__main__':

    a = 'a'
    b = 'a'
    assert check_if_perm(a, b) is True, 'Test 1 Failed'

    a = 'a'
    b = 'b'
    assert check_if_perm(a, b) is False, 'Test 2 Failed'

    a = 'a'
    b = 'aa'
    assert check_if_perm(a, b) is False, 'Test 3 Failed'

    a = 'aa'
    b = 'aa'
    assert check_if_perm(a, b) is True, 'Test 4 Failed'

    a = 'ab'
    b = 'aa'
    assert check_if_perm(a, b) is False, 'Test 5 Failed'

    a = 'ab'
    b = 'ba'
    assert check_if_perm(a, b) is True, 'Test 6 Failed'

    a = 'abcdefggholli'
    b = 'llihafggecdbo'
    assert check_if_perm(a, b) is True, 'Test 7 Failed'
