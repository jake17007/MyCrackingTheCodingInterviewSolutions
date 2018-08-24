class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def append_to_tail(self, val):
        curr = self
        while curr.next != None:
            curr = curr.next
        curr.next = Node(val)


def equal_lls(a, b):
    while a.next != None or b.next != None:
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
    while curr != None:
        s += str(curr.val) + ' -> '
        curr = curr.next
    s += 'None'
    print(s)


def partition(head, n):
    curr = head
    if curr == None:
        return None

    r_head = None
    r_tail = None
    l_head = None
    l_rail = None

    while curr != None:
        next = curr.next
        if curr.val >= n:
            if not r_head:
                r_head = curr
                r_tail = curr
            else:
                r_tail.next = curr
                curr.next = None
                r_tail = curr
        else:
            if l_head == None:
                l_head = curr
                l_tail = curr
            else:
                l_tail.next = curr
                curr.next = None
                l_tail = curr
        curr = next

    if l_head:
        l_tail.next = r_head
        return l_head
    return r_head


def main():

    print('\nTest 1')
    x = None
    y = partition(x, 1)
    assert y == None, 'Test 1 failed.'

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
    y = partition(x, 1)
    z = Node(0)
    z.append_to_tail(1)
    print(y)
    #display(y)
    #display(z)
    assert equal_lls(y, z), 'Test 6 failed.'


if __name__ == '__main__':
    main()
