class Node():
    next = None

    def __init__(self, val=None):
        self.val = val


    def add(self, val):
        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)


def display(node):
    if node is None:
        print('None')
        return
    curr = node
    while curr is not None:
        print(curr.val)
        curr = curr.next


def remove_duplicates(head):
    if head is None:
        return None
    seen = {head.val}
    curr = head.next
    prev = head
    while curr != None:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen.add(curr.val)
            prev = prev.next
        curr = curr.next
    return head


def main():
    ll_test_1 = Node()
    print('Test 1 (before)')
    display(ll_test_1)
    print('Test 1 (after)')
    ll_test_1 = remove_duplicates(ll_test_1)
    display(ll_test_1)

    ll_test_2 = Node(1)
    ll_test_2.add(2)
    ll_test_2.add(3)
    print('Test 2 (before)')
    display(ll_test_2)
    print('Test 2 (after)')
    ll_test_2 = remove_duplicates(ll_test_2)
    display(ll_test_2)

    ll_test_3 = Node(1)
    ll_test_3.add(1)
    print('Test 3 (before)')
    display(ll_test_3)
    print('Test 3 (after)')
    ll_test_3 = remove_duplicates(ll_test_3)
    display(ll_test_3)

    ll_test_4 = Node(1)
    ll_test_4.add(1)
    ll_test_4.add(1)
    ll_test_4.add(2)
    print('Test 4 (before)')
    display(ll_test_4)
    print('Test 4 (after)')
    ll_test_4 = remove_duplicates(ll_test_4)
    display(ll_test_4)


if __name__ == '__main__':
    main()
