from collections import deque

def get_neighbours(i, j, max_dim):
    
    neighbours = [[(i-1, j-1), (i-1, j), (i-1, j+1)], 
                  [(i, j-1), (i, j+1)], 
                  [(i+1, j-1), (i+1, j), (i+1, j+1)]]

    if i == 0:
        neighbours.pop(0)
    elif i == max_dim - 1:
        neighbours.pop(2)

    if j == 0:
        for row in neighbours:
            row.pop(0)
    elif j == max_dim - 1:
        for row in neighbours:
            row.pop(-1)

    return neighbours

def populate_queue(queue, neighbours, arr, unexplored):

    for row in neighbours:
        for i, j in row:
            if not unexplored.get(i):
                continue
            elif not unexplored[i].get(j):
                continue


            unexplored[i].pop(j)
            if not list(unexplored[i].keys()):
                unexplored.pop(i)

            if arr[i][j] == 0:
                queue.appendleft((i, j))

    return queue, unexplored
    

def pond_sizes(arr):

    unexplored = {}
    for i in range(len(arr)):
        unexplored[i] = {}
        for j in range(len(arr[i])):
            unexplored[i][j] = True

    pond_sizes = []
    while len(list(unexplored.keys())):
        row = list(unexplored.keys())[0]
        col = list(unexplored[row].keys())[0]
        unexplored[row].pop(col)
        if not list(unexplored[row].keys()):
            unexplored.pop(row)
        if arr[row][col] != 0:
            continue

        pond_size = 1
        neighbours = get_neighbours(row, col, len(arr[0]))
        queue, unexplored = populate_queue(deque(), neighbours, arr, unexplored)
 
        while len(queue):
            pond_size += 1
            node = queue.pop()
            new_neighbours = get_neighbours(node[0], node[1], len(arr[0]))
            queue, unexplored = populate_queue(queue, new_neighbours, arr, unexplored)

        pond_sizes.append(pond_size)

    return pond_sizes


def test_case(arr, solution, test_func):

    output = test_func(arr)
    if sorted(output) == sorted(solution):
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]], [2, 4, 1], pond_sizes)
