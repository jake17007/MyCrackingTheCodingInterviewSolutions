import math

import pytest


def sort_stack(s):
    len_s = 0
    s2 = []

    # Get length
    while s:
        s2.append(s.pop())
        len_s += 1

    # Sort
    num_sorted = 0
    while num_sorted < len_s:
        max_ = -math.inf
        num_checked = 0
        while s2 and num_checked < (len_s - num_sorted):
            curr = s2.pop()
            to_add = min(max_, curr)
            max_ = max(max_, curr)
            if num_checked > 0:
                s.append(to_add)
            num_checked += 1
        s2.append(max_)
        num_sorted += 1
        while s:
            s2.append(s.pop())

    print(s2)
    return s2


tests = [
    ([], []),
    ([1], [1]),
    ([2, 1], [2, 1]),
    ([1, 2], [2, 1]),
    ([-10, -10, 1, 6, 2, 6, 4], [6, 6, 4, 2, 1, -10, -10])
]


@pytest.mark.parametrize('input', tests)
def test_sort_stack(input):
    assert sort_stack(input[0]) == input[1]
