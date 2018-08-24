class SetOfStacks:

    def __init__(self, limit):
        self.limit = limit
        self.stacks = []

    def push(self, val):
        if self.stacks == []:
            self.stacks.append([val])
        else:
            last = self.stacks[-1]
            if len(last) >= self.limit:
                self.stacks.append([val])
            else:
                last.append(val)

    def pop(self):
        if self.stacks == []:
            return 'error'
        to_return = self.stacks[-1].pop()
        if self.stacks[-1] == []:
            self.stacks.pop()
        return to_return

def main():

    # Test push
    sos = SetOfStacks(2)
    sos.push(1)
    print(sos.stacks)
    assert sos.stacks == [[1]], 'Push test 1 failed.'

    sos = SetOfStacks(2)
    sos.push(1)
    sos.push(2)
    print(sos.stacks)
    assert sos.stacks == [[1, 2]], 'Push test 2 failed.'

    sos = SetOfStacks(2)
    sos.push(1)
    sos.push(2)
    sos.push(3)
    print(sos.stacks)
    assert sos.stacks == [[1, 2],[3]], 'Push test 3 failed.'

    #Test pop
    sos = SetOfStacks(2)
    result = sos.pop()
    print(result)
    assert result == 'error', 'Pop test 1a failed.'
    assert sos.stacks == [], 'Pop test 1b failed.'

    sos = SetOfStacks(2)
    sos.push(1)
    result = sos.pop()
    print(result)
    assert result == 1, 'Pop test 2a failed.'
    assert sos.stacks == [], 'Pop test 2b failed.'

    sos = SetOfStacks(2)
    sos.push(1)
    sos.push(2)
    result = sos.pop()
    print(result)
    assert result == 2, 'Pop test 3a failed.'
    assert sos.stacks == [[1]], 'Pop test 3b failed.'

    sos = SetOfStacks(2)
    sos.push(1)
    sos.push(2)
    sos.push(3)
    result = sos.pop()
    print(result)
    assert result == 3, 'Pop test 4a failed.'
    assert sos.stacks == [[1, 2]], 'Pop test 4b failed.'


if __name__ == '__main__':
    main()
