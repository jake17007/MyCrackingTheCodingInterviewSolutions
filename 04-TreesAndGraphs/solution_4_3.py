from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def display(self):
        curr = self
        st = ''
        while curr != None:
            st += curr.val + ' -> '
            curr = curr.next
        st += 'None'
        return st


class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_lod(root):
    q = Queue()
    lod = []
    if root == None:
        return lod
    prev_level = -1
    q.put((root, 0))
    while not q.empty():
        curr = q.get()
        curr_node = Node(curr[0].val)
        if curr[1] != prev_level:  # Either start a new linked list
            lod.append(curr_node)
            prev_level = curr[1]
        else:  # ... or append to the last node in current linked list
            last.next = curr_node
        last = curr_node # update last node regardless

        if curr[0].left:
            q.put((curr[0].left, curr[1] + 1))
        if curr[0].right:
            q.put((curr[0].right, curr[1] + 1))

    return lod


def lod_to_str(lod):
    if not lod:
        return '[]'
    else:
        st = '['
        for li in lod:
            st += str(li.display()) + ', '
        st += ']'
    return st


def main():

    x = None
    result = lod_to_str(create_lod(x))
    print(result)
    assert result == '[]', 'Test 1 failed.'

    x = BTNode('A')
    result = lod_to_str(create_lod(x))
    print(result)
    assert result == '[A -> None, ]', 'Test 2 failed.'

    x = BTNode('A')
    x.left = BTNode('B')
    x.right = BTNode('C')
    result = lod_to_str(create_lod(x))
    print(result)
    assert result == '[A -> None, B -> C -> None, ]', 'Test 3 failed.'

    x = BTNode('A')
    x.left = BTNode('B')
    result = lod_to_str(create_lod(x))
    print(result)
    assert result == '[A -> None, B -> None, ]', 'Test 4 failed.'

    x = BTNode('A')
    x.left = BTNode('C')
    result = lod_to_str(create_lod(x))
    print(result)
    assert result == '[A -> None, C -> None, ]', 'Test 5 failed.'


if __name__ == '__main__':
    main()
