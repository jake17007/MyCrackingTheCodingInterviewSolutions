class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def move_from_to(self, a, b):
        while a:
            b.append(a.pop())

    def enqueue(self, val):
        self.move_from_to(self.s2, self.s1)
        self.s1.append(val)

    def dequeue(self):
        if not self.s1 and not self.s2:
            return 'Error'
        self.move_from_to(self.s1, self.s2)
        return self.s2.pop()


def test_enqueue():
    mq = MyQueue()
    tests = [([], [], 1, [1], []),
             ([1], [], 2, [1, 2], []),
             ([], [1], 2, [1, 2], [])]
    for i, test in enumerate(tests):
        mq.s1 = test[0]
        mq.s2 = test[1]
        mq.enqueue(test[2])
        assert mq.s1 == test[3], 'Test {}.A failed.'.format(i)
        assert mq.s2 == test[4], 'Test {}.B failed.'.format(i)


def test_dequeue():
    mq = MyQueue()
    tests = [([], [], [], [], 'Error'),
             ([], [1], [], [], 1),
             ([1], [], [], [], 1),
             ([], [2, 1], [], [2], 1),
             ([1, 2], [], [], [2], 1)]
    for i, test in enumerate(tests):
        mq.s1 = test[0]
        mq.s2 = test[1]
        result = mq.dequeue()
        assert mq.s1 == test[2], 'Test {}.A failed.'.format(i)
        assert mq.s2 == test[3], 'Test {}.B failed.'.format(i)
        assert result == test[4], 'Test {}.C failed.'.format(i)
