def find_magic_index(a):
    i = 0
    while i < len(a) and a[i] != i:
        i += 1
    if i == len(a):
        return None
    return i


def find_magic_index_rec(a):
    return find_magic_index_rec_h(a, 0, len(a)-1)


def find_magic_index_rec_h(a, left_idx, right_idx):
    if right_idx < left_idx:
        return None
    mid = (left_idx + right_idx) // 2
    if a[mid] == mid:
        return a[mid]

    # Search left
    left = find_magic_index_rec_h(a, left_idx, min(a[mid], mid-1))
    if left:
        return left

    # Search right
    right = find_magic_index_rec_h(a, max(a[mid], mid+1), right_idx)
    return right


def main():
    x = []
    y = find_magic_index(x)
    assert y is None, 'Test 1 failed.'
    y = find_magic_index_rec(x)
    assert y is None, 'Test 1 failed.'

    x = [0]
    y = find_magic_index(x)
    assert y == 0, 'Test 2 failed.'
    y = find_magic_index_rec(x)
    assert y == 0, 'Test 2 failed.'

    x = [-1, 1]
    y = find_magic_index(x)
    assert y == 1, 'Test 3 failed.'
    y = find_magic_index_rec(x)
    assert y == 1, 'Test 3 failed.'

    x = [1]
    y = find_magic_index(x)
    assert y is None, 'Test 4 failed.'
    y = find_magic_index_rec(x)
    assert y is None, 'Test 4 failed.'

    x = [-1, 2]
    y = find_magic_index(x)
    assert y is None, 'Test 5 failed.'
    y = find_magic_index_rec(x)
    assert y is None, 'Test 5 failed.'

    x = [-1, -1, 0, 3]
    y = find_magic_index(x)
    assert y == 3, 'Test 6 failed.'
    y = find_magic_index_rec(x)
    assert y == 3, 'Test 6 failed.'

    x = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    y = find_magic_index_rec(x)
    assert y == 2, 'Test 7 failed.'


if __name__ == '__main__':
    main()
