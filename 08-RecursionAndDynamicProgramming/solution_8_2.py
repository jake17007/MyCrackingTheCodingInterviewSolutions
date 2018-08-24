def get_bottom_right(grid):
    return (len(grid)-1, len(grid[0])-1)


def get_top_left(grid):
    return (0, 0)


def get_dir(grid, curr, dir):
    if dir == 'r':
        curr = (curr[0], curr[1]+1)
    if dir == 'd':
        curr = (curr[0]+1, curr[1])
    if dir == 'l':
        curr = (curr[0], curr[1]-1)
    if dir == 'u':
        curr = (curr[0]-1, curr[1])
    if curr[0] > len(grid) - 1 or curr[0] < 0 or curr[1] > len(grid[0]) - 1 or curr[1] < 0:
        return None
    return curr


def is_good(grid, curr):
    return grid[curr[0]][curr[1]] == 0


def mark_cells(grid):
    good_cells = set()
    v = set()
    st = []
    st.append(get_bottom_right(grid))
    while st:
        curr = st.pop()
        v.add(curr)
        if is_good(grid, curr):
            good_cells.add(curr)
            if curr == get_top_left(grid):
                break
            l = get_dir(grid, curr, 'l')
            u = get_dir(grid, curr, 'u')
            if l:
                st.append(l)
            if u:
                st.append(u)
    if get_top_left(grid) not in good_cells:
        return 'ERROR'
    return good_cells


def path_from_marked(grid, good_cells):
    if good_cells == 'ERROR':
        return good_cells
    curr = get_top_left(grid)
    end = get_bottom_right(grid)
    path = [curr]
    while curr != end:
        d = get_dir(grid, curr, 'd')
        if d and d in good_cells:
            path.append(d)
            curr = d
            continue
        r = get_dir(grid, curr, 'r')
        if r and r in good_cells:
            path.append(r)
            curr = r
            continue
    return path


def get_path(grid):
    good_cells = mark_cells(grid)
    path = path_from_marked(grid, good_cells)
    return path


def main():
    x = [[0, 0],
         [1, 0]]
    assert get_path(x) == [(0,0),(0,1),(1,1)], 'Test 1 failed'

    x = [[0, 1],
         [0, 0]]
    assert get_path(x) == [(0,0),(1,0),(1,1)], 'Test 2 failed'

    x = [[0, 1],
         [1, 0]]
    assert get_path(x) == 'ERROR', 'Test 3 failed'

    x = [[0, 1, 0],
         [0, 0, 0],
         [1, 1, 0]]
    assert get_path(x) == [(0,0),(1,0),(1,1),(1,2),(2,2)], 'Test 4 failed'


    x = [[0, 0, 1],
         [1, 0, 1],
         [1, 0, 0]]
    assert get_path(x) == [(0,0),(0,1),(1,1),(2,1),(2,2)], 'Test 5 failed'


if __name__ == '__main__':
    main()
