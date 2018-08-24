def merge(a, b):

    # shift a by len(b)
    i = len(a) - 1
    j = len(a) - len(b) - 1
    while j >= 0:
        a[i] = a[j]
        i -= 1
        j -= 1

    # merge
    i = len(b)
    j = 0
    curr = 0
    while i < len(a) and j < len(b):
        if b[j] <= a[i]:
            a[curr] = b[j]
            j += 1
        else:
            a[curr] = a[i]
            i += 1
        curr += 1

    # merge rest
    while curr < len(a):
        if i >= len(a):
            a[curr] = b[j]
            j += 1
        else:
            a[curr] = a[i]
            i +=1
        curr += 1

    return a

def main():
    a = []
    b = []

    assert merge(a, b) == [], 'Test 1 failed'

    a = [1]
    b = []
    assert merge(a, b) == [1], 'Test 2 failed'

    a = [None]
    b = [1]
    assert merge(a, b) == [1], 'Test 3 failed'

    a = [1, None]
    b = [2]
    assert merge(a, b) == [1, 2], 'Test 4 failed'

    a = [2, None]
    b = [1]
    assert merge(a, b) == [1, 2], 'Test 5 failed'

    a = [-10, -6, 1, 1, 9, 9, 9, None, None, None, None]
    b = [-6, 1, 2, 100]
    assert merge(a, b) == [-10, -6, -6, 1, 1, 1, 2, 9, 9, 9, 100], 'Test 5 failed'


if __name__ == '__main__':
    main()
