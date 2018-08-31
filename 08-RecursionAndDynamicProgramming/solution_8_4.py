from copy import deepcopy


def generate_ps_h(subsets_acc, my_set):
    if not my_set:
        return subsets_acc
    new_subs = deepcopy(subsets_acc)
    elem = my_set.pop()
    for sub in new_subs:
        sub.add(elem)
    subsets_acc.extend(new_subs)
    return generate_ps_h(subsets_acc, my_set)


def generate_ps(my_set):
    return generate_ps_h([set()], my_set)


def test_generate_ps():
    tests = [(set(), [set()]),
             (set([1]), [set(), set([1])]),
             (set([1, 2]), [set(), set([1]), set([2]), set([1, 2])])]

    for i, test in enumerate(tests):
        print('Test {} running'.format(i+1))
        assert generate_ps(test[0]) == test[1], 'Test {} failed.'.format(i+1)
