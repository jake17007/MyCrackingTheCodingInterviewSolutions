def char_counts(s):
    max_ = max([ord(s[i]) for i in range(len(s))])
    counts = [0] * (max_ + 1)
    for i in range(len(s)):
        counts[ord(s[i])] += 1
    return counts


def get_ana_map(ary):
    ana_map = {}
    for i in range(len(ary)):
        s = ary[i]
        char_counts_str = str(char_counts(s))
        if char_counts_str in ana_map:
            ana_map[char_counts_str].add(i)
        else:
            ana_map[char_counts_str] = set([i])
    return ana_map


def order_anas(ary):
    ana_map = get_ana_map(ary)
    new_order = []
    for char_count in ana_map:
        idxs = ana_map[char_count]
        for idx in idxs:
            new_order.append(ary[idx])
    return new_order


def main():
    ary = []
    assert order_anas(ary) == [], 'Test 1 failed'

    ary = ['a']
    assert order_anas(ary) == ['a'], 'Test 2 failed'

    ary = ['a', 'b', 'a']
    assert order_anas(ary) == ['a', 'a', 'b'], 'Test 3 failed'

    ary = ['a', 'a', 'b']
    assert order_anas(ary) == ['a', 'a', 'b'], 'Test 4 failed'

    ary = ['a', 'ab', 'ba', 'a']
    assert order_anas(ary) == ['a', 'a', 'ab', 'ba'], 'Test 5 failed'


if __name__ == '__main__':
    main()
