class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def append_to_end(self, val):
        curr = self
        while curr.next != None:
            curr = curr.next
        curr.next = Node(val)

    def display(self):
        curr = self
        st = ''
        while curr != None:
            st += (curr.val + ' -> ')
            curr = curr.next
        st += 'None'
        print(st)
        return st


def delete_mid_node(node):
    node.val = node.next.val
    node.next = node.next.next


def main():

    first = Node('a')
    second = Node('b')
    third = Node('c')
    first.next = second
    second.next = third
    delete_mid_node(second)
    assert first.display() == 'a -> c -> None', 'Test 1 failed.'

    first = Node('a')
    second = Node('b')
    third = Node('c')
    fourth = Node('d')
    first.next = second
    second.next = third
    third.next = fourth
    delete_mid_node(third)
    assert first.display() == 'a -> b -> d -> None', 'Test 2 failed.'


if __name__ == '__main__':
    main()
