class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def append_to_tail(self, val):
        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)


def find_kth_to_last(head, k):
    trail = head
    i = 1
    while i < k:
        head = head.next
        i += 1
        if head is None:
            return 'error'
    while head.next is not None:
        head = head.next
        trail = trail.next
    return trail.val

def main():
    x = Node(1)
    assert find_kth_to_last(x, 1) == 1, 'Test 1 Failed'

    x = Node(1)
    x.append_to_tail(2)
    assert find_kth_to_last(x, 3) == 'error', 'Test 2 Failed'

    x = Node(1)
    x.append_to_tail(2)
    assert find_kth_to_last(x, 2) == 1, 'Test 3 Failed'

    x = Node(1)
    x.append_to_tail(2)
    assert find_kth_to_last(x, 1) == 2, 'Test 4 Failed'

if __name__ == '__main__':
    main();
