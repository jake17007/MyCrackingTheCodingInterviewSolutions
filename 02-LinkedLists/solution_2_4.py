class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def append_to_tail(self, val):
        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)


def equal_lls(a, b):
    while a.next is not None or b.next is not None:
        if a.val != b.val:
            return False
        if (not hasattr(a, 'next')) or (not hasattr(b, 'next')):
            return False
        a = a.next
        b = b.next
    return True


def display(a):
    curr = a
    s = ''
    while curr is not None:
        s += str(curr.val) + ' -> '
        curr = curr.next
    s += 'None'
    print(s)


def partition(head, n):
    curr = head
    if curr is None:
        return None

    r_head = None
    r_tail = None
    l_head = None
    l_tail = None

    while curr is not None:
        next = curr.next
        if curr.val >= n:
            if not r_head:
                curr.next = None
                r_head = curr
                r_tail = r_head
            else:
                curr.next = None
                r_tail.next = curr
                r_tail = r_tail.next
        else:
            if l_head is None:
                curr.next = None
                l_head = curr
                l_tail = l_head
            else:
                curr.next = None
                l_tail.next = curr
                l_tail = l_tail.next
        curr = next

    if l_head:
        l_tail.next = r_head
        return l_head
    return r_head


def main():

    print('\nTest 1')
    x = None
    y = partition(x, 1)
    assert y is None, 'Test 1 failed.'

    print('\nTest 2')
    x = Node(1)
    y = partition(x, 0)
    z = Node(1)
    display(y)
    display(z)
    assert equal_lls(y, z), 'Test 2 failed.'

    print('\nTest 3')
    x = Node(1)
    y = partition(x, 1)
    z = Node(1)
    display(y)
    display(z)
    assert equal_lls(y, z), 'Test 3 failed.'

    print('\nTest 4')
    x = Node(1)
    y = partition(x, 2)
    z = Node(1)
    display(y)
    display(z)
    assert equal_lls(y, z), 'Test 4 failed.'

    print('\nTest 5')
    x = Node(1)
    x.append_to_tail(0)
    y = partition(x, 0)
    z = Node(1)
    z.append_to_tail(0)
    display(y)
    display(z)
    assert equal_lls(y, z), 'Test 5 failed.'

    print('\nTest 6')
    x = Node(1)
    x.append_to_tail(0)
    z = Node(0)
    z.append_to_tail(1)
    y = partition(x, 1)
    display(y)
    display(z)
    assert equal_lls(y, z), 'Test 6 failed.'

    print('\nTest 7')
    x = Node(3)
    x.append_to_tail(5)
    x.append_to_tail(8)
    x.append_to_tail(5)
    x.append_to_tail(10)
    x.append_to_tail(2)
    x.append_to_tail(1)
    y = partition(x, 5)
    z = Node(3)
    z.append_to_tail(2)
    z.append_to_tail(1)
    z.append_to_tail(5)
    z.append_to_tail(8)
    z.append_to_tail(5)
    z.append_to_tail(10)
    display(y)
    display(z)
    assert equal_lls(y, z), 'Test 7 failed.'


if __name__ == '__main__':
    main()
