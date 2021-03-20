import time

#goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
goal_state = '123456789'


def convertToMatrix(string, columns):
    # slicing strings
    #temp = [string[idx: idx + rows] for idx in range(0, len(string), rows)]
    # conversion to list of characters
    #res = [list(element) for element in temp]
    # printing result
    #print("The converted Matrix : " + str(res))

    # hint range(x) = 0 to x-1
    state = []
    for i in range(len(string)):
        if i % columns == 0:
            sub = string[i:i + columns]
            row = []
            for j in sub:
                row.append(j)
            print(' '.join(row))
            state.append(row)
    print(state)

start_state = "612783549"
convertToMatrix(start_state, 3)
convertToMatrix(goal_state, 3)


def f():
   start_time = time.time()

   # ... do something ...

   passed_time = time.time() - start_time()

   print(f'Total time (in seconds): {passed_time}')


class Node:
    def __init__(self, state, parent, action, depth, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost

    def dfs(start, goal):
        openList = []
        openList.append(start)

        closeList = []

        depth_limit = 5000

        start_time = time.time()
        while len(openList) > 0:
            elapsed_time = time.time() - start_time
            if (elapsed_time < 60):
                # get a current state node
                node = openList.pop(0)
                if node.state == goal:
                    print(node.state)
                    return "Find solution"
            else:
                return 'No solution'

    def move_up(state):
        x = 0

    def move_down(state):
        x = 0

    def move_left(state):
        x = 0

    def move_right(state):
        x = 0
