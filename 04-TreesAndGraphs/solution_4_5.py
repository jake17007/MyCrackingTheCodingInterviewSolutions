from copy import deepcopy
import math
import pytest

from BSTNode import BSTNode


def validate_bst_h(root, lo, hi):
    if not root:
        return True
    valid = root.val > lo and root.val <= hi
    return (valid and validate_bst_h(root.left, lo, root.val)
            and validate_bst_h(root.right, root.val, hi))


def validate_bst(root):
    return validate_bst_h(root, -math.inf, math.inf)


# Test cases

test1 = None

test2 = BSTNode(1)

test3 = BSTNode(1)
test3.left = BSTNode(1)

test4 = BSTNode(1)
test4.right = BSTNode(2)

test5 = BSTNode(1)
test5.left = BSTNode(2)

test6 = BSTNode(1)
test6.right = BSTNode(1)

test7 = BSTNode(1)
test7.left = BSTNode(1)
test7.right = BSTNode(2)

test8 = BSTNode(1)
test8.left = BSTNode(2)
test8.right = BSTNode(2)

test9 = BSTNode(1)
test9.left = BSTNode(1)
test9.right = BSTNode(1)

test10 = BSTNode(10)
test10.left = BSTNode(7)
test10.right = BSTNode(20)
test10.left.left = BSTNode(3)
test10.left.left.left = BSTNode(1)
test10.left.right = BSTNode(8)
test10.left.right.left = BSTNode(7.5)
test10.left.right.right = BSTNode(9)
test10.right = BSTNode(20)
test10.right.right = BSTNode(29)

test11 = deepcopy(test10)
test11.right.left = BSTNode(9)

TESTS = [
    (test1, True),
    (test2, True),
    (test3, True),
    (test4, True),
    (test5, False),
    (test6, False),
    (test7, True),
    (test8, False),
    (test9, False),
    (test10, True),
    (test11, False)
]


@pytest.mark.parametrize('input', TESTS)
def test_validate_bst(input):
    assert validate_bst(input[0]) == input[1]
