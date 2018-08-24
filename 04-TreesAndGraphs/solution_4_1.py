import queue

class Node:
    def __init__(self, val):
        self.neighbors = []
        self.visited = False
        self.val = val


    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


    def display(self):
        neighbors_str = ''
        for neighbor in self.neighbors:
            neighbors_str += neighbors_str + neighbor.val + ', '
        print('%s: %s' % (self.val, neighbors_str))


def is_route(a, b):
    q = queue.Queue()
    q.put(a)
    while not q.empty():
        c = q.get()
        if c == b:
            return True
        c.visited = True
        for neighbor in c.neighbors:
            if neighbor.visited is False:
                q.put(neighbor)
    return False


def show_is_correct(actual, result):
    if actual == result:
        print('Correct!')
    else:
        print('Wrong!')


def main():

    print('\nTest 1:')
    test_1_a = Node('a')
    test_1_b = Node('b')
    test_1_a.add_neighbor(test_1_b)
    test_1_a.display()
    test_1_b.display()
    show_is_correct(True, is_route(test_1_a, test_1_b))


    print('\nTest 2:')
    test_2_a = Node('a')
    test_2_b = Node('b')
    test_2_a.display()
    test_2_b.display()
    show_is_correct(False, is_route(test_2_a, test_2_b))

    print('\nTest 3:')
    test_3_a = Node('a')
    test_3_b = Node('b')
    test_3_c = Node('c')
    test_3_a.add_neighbor(test_3_c)
    test_3_c.add_neighbor(test_3_b)
    test_3_a.display()
    test_3_b.display()
    test_3_c.display()
    show_is_correct(True, is_route(test_3_a, test_3_b))

    print('\nTest 4:')
    test_4_a = Node('a')
    test_4_b = Node('b')
    test_4_c = Node('c')
    test_4_a.add_neighbor(test_4_c)
    test_4_c.add_neighbor(test_4_a)
    test_4_a.display()
    test_4_b.display()
    test_4_c.display()
    show_is_correct(False, is_route(test_4_a, test_4_b))


if __name__ == '__main__':
    main()
