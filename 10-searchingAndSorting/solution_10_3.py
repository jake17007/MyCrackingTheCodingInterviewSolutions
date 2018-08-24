def check_if_can_be_in(a, n, lo, hi):
    if a[lo] <= a[hi] and a[lo] <= n:
        return True
    elif a[lo] >= a[hi] and n <= a[hi]:
        return True
    else:
        return False


def find_in_rotated(a, n):
    return find_in_rotated_h(a, n, 0, len(a)-1)


def find_in_rotated_h(a, n, lo, hi):
    if len(a) == 0:
        return None
    mid = (lo + hi) // 2
    if a[mid] == n:
        return mid
    if len(a) == 1:
        return None
    # Check right
    if check_if_can_be_in(a, n, mid+1, hi):
        return find_in_rotated_h(a, n, mid+1, hi)
    else:
        return find_in_rotated_h(a, n, lo, mid-1)


def main():
    a, n = [], 1
    result = find_in_rotated(a, n)
    assert result == None, 'Test 1 failed.'

    a, n = [1], 1
    result = find_in_rotated(a, n)
    assert result == 0, 'Test 2 failed.'

    a, n = [1], 2
    result = find_in_rotated(a, n)
    assert result == None, 'Test 3 failed.'

    a, n = [0, 1], 1
    result = find_in_rotated(a, n)
    assert result == 1, 'Test 4 failed.'

    a, n = [1, 0], 1
    result = find_in_rotated(a, n)
    assert result == 0, 'Test 5 failed.'

    a, n = [0, 1], 2
    result = find_in_rotated(a, n)
    assert result == None, 'Test 6 failed.'

    a, n = [0, 3, 5], 0
    result = find_in_rotated(a, n)
    assert result == 0, 'Test 7 failed.'

    a, n = [0, 3, 5], 5
    result = find_in_rotated(a, n)
    assert result == 2, 'Test 8 failed.'

    a, n = [0, 3, 5], 6
    result = find_in_rotated(a, n)
    assert result == None, 'Test 9 failed.'

    a, n = [5, 3, 0], 0
    result = find_in_rotated(a, n)
    assert result == 2, 'Test 10 failed.'

    a, n = [3, 5, 0], 3
    result = find_in_rotated(a, n)
    assert result == 0, 'Test 11 failed.'

    a, n = [3, 5, 0], 6
    result = find_in_rotated(a, n)
    assert result == None, 'Test 12 failed.'

    a, n = [6, 8, 10, 0, 2, 4], 6
    result = find_in_rotated(a, n)
    assert result == 0, 'Test 13 failed.'

    a, n = [6, 8, 10, 0, 2, 4], 10
    result = find_in_rotated(a, n)
    assert result == 3, 'Test 14 failed.'

    a, n = [6, 8, 10, 0, 4], 0
    result = find_in_rotated(a, n)
    assert result == 3, 'Test 15 failed.'


if __name__ == '__main__':
    main()
