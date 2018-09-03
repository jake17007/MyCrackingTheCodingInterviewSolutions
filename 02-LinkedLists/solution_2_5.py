class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def display(self):
        curr = self
        s = ''
        while curr:
            s += str(curr.val) + ' -> '
            curr = curr.next
        s += 'None'
        return s

    def append_to_end(self, val):
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        return self


def equal_lls(a, b):
    if a is None and b is None:
        return True
    elif a is None:
        return False
    elif b is None:
        return False
    a = a.display()
    b = b.display()
    if a == b:
        return True
    return False


def sum_ll(a, b):
    if a is None:
        return b
    if b is None:
        return a
    curr = None
    head = curr
    carry = 0
    while a or b:
        # Calcuate current digit
        if a and b:
            curr_val = a.val + b.val + carry
            a = a.next
            b = b.next
        elif a:
            curr_val = a.val + carry
            a = a.next
        else:
            curr_val = b.val + carry
            b = b.next

        # Calculate carry digit
        if curr_val > 9:
            curr_val -= 10
            carry = 1
        else:
            carry = 0

        # Save and update nodes
        curr = Node(curr_val)
        if not head:
            head = curr
            tail = curr
        else:
            tail.next = curr
            tail = curr
        curr = curr.next

    if carry:
        tail.next = Node(carry)

    return head


def test_sum_ll():
    tests = [(None, None, None),
             (None, Node(1), Node(1)),
             (Node(1), None, Node(1)),
             (Node(1), Node(1), Node(2)),
             (Node(1), Node(1).append_to_end(2), Node(2).append_to_end(2)),
             (Node(1).append_to_end(2), Node(1), Node(2).append_to_end(2)),
             (Node(1).append_to_end(2).append_to_end(3), Node(1),
              Node(2).append_to_end(2).append_to_end(3)),
             (Node(9), Node(9), Node(8).append_to_end(1)),
             (Node(9).append_to_end(1), Node(9), Node(8).append_to_end(2)),
             (Node(5).append_to_end(9).append_to_end(2),
              Node(7).append_to_end(1).append_to_end(6).append_to_end(9),
              Node(2).append_to_end(1).append_to_end(9).append_to_end(9))]
    for i, test in enumerate(tests):
        result = sum_ll(test[0], test[1])
        assert equal_lls(result, test[2]), 'Test {} failed.'.format(i + 1)
