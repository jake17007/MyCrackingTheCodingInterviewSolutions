class BinNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_leaf(root):
    return root.left is None and root.right is None


def is_balanced_h(root, height):
    if root is None:
        return True, 0
    if is_leaf(root):
        return True, 1

    l_is_bal, l_height = is_balanced_h(root.left, 0)
    r_is_bal, r_height = is_balanced_h(root.right, 0)

    dif = abs(l_height - r_height)
    if dif <= 1 and l_is_bal and r_is_bal:
        return True, max(1+l_height, 1+r_height)
    return False, 0


def is_balanced(root):
    return is_balanced_h(root, 0)[0]


def test_is_leaf():
    test1 = BinNode(1)
    assert is_leaf(test1) is True

    test2 = BinNode(1)
    test2.left = BinNode(2)
    assert is_leaf(test2) is False


def test_is_balanced():
    tests = []

    test1 = None
    tests.append((test1, True))

    test2 = BinNode(1)
    tests.append((test2, True))

    test3 = BinNode(1)
    test3.right = BinNode(2)
    tests.append((test3, True))

    test4 = BinNode(1)
    test4.left = BinNode(2)
    tests.append((test4, True))

    test5 = BinNode(1)
    test5.left = BinNode(2)
    test5.right = BinNode(3)
    tests.append((test5, True))

    test6 = BinNode(1)
    test6.left = BinNode(2)
    test6.left.left = BinNode(3)
    tests.append((test6, False))

    test7 = BinNode(1)
    test7.right = BinNode(2)
    test7.right.left = BinNode(3)
    tests.append((test7, False))

    for i, test in enumerate(tests):
        assert is_balanced(test[0]) is test[1]
