def ways_up_steps(n):
    if n in [0, 1, 2]:
        return n
    if n == 3:
        return 4

    a, b, c = 1, 2, 4
    for i in range(4, n + 1):
        d = a + b + c
        a = b
        b = c
        c = d

    return d


def main():
    test_cases = range(8)
    answers = [0, 1, 2, 4, 7, 13, 24, 44]
    for test_case in test_cases:
        assert ways_up_steps(test_case) == answers[test_case], \
            'Test case: {} failed'.format(test_case)
    print('All tests passed.')

if __name__ == '__main__':
    main()
