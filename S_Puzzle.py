import time

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
    return state


def f():
   start_time = time.time()

   # ... do something ...

   passed_time = time.time() - start_time()

   print(f'Total time (in seconds): {passed_time}')


def move_up(puzzle, row, column):
    # copy puzzle & delete all elements
    # remark: new_puzzle = puzzle[:], doesn't work in 2d list
    new_puzzle = [x[:] for x in puzzle]
    if row != 0:
        new_puzzle[row][column], new_puzzle[row-1][column] = new_puzzle[row-1][column], new_puzzle[row][column]
        print(new_puzzle)
        return new_puzzle
    else:
        return None

def move_down(puzzle, row, column):
    new_puzzle = [x[:] for x in puzzle]
    if row != len(puzzle)-1:
        new_puzzle[row][column], new_puzzle[row+1][column] = new_puzzle[row+1][column], new_puzzle[row][column]
        print(new_puzzle)
        return new_puzzle
    else:
        return None

def move_left(puzzle, row, column):
    new_puzzle = [x[:] for x in puzzle]
    if column != 0:
        new_puzzle[row][column], new_puzzle[row][column-1] = new_puzzle[row][column-1], new_puzzle[row][column]
        print(new_puzzle)
        return new_puzzle
    else:
        return None

def move_right(puzzle, row, column):
    new_puzzle = [x[:] for x in puzzle]
    if column != len(puzzle[0])-1:
        new_puzzle[row][column], new_puzzle[row][column+1] = new_puzzle[row][column+1], new_puzzle[row][column]
        print(new_puzzle)
        return new_puzzle
    else:
        return None

def findChildNode(parent_node):
    puzzle = parent_node.puzzle
    #print(puzzle)
    rows = len(puzzle)
    columns = len(puzzle[0])
    child_nodes = []

    #for i in puzzle:
        #for j in i:
            #print(j)

    for row in range(rows):
        for column in range(columns):
            print("Puzzle", puzzle[row][column])
            #if row == 1 and column == 1:
            child_node = create_node(move_up(puzzle, row, column), parent_node, parent_node.depth+1, 0)
            child_nodes.append(child_node)
            child_node = create_node(move_down(puzzle, row, column), parent_node, parent_node.depth + 1, 0)
            child_nodes.append(child_node)
            child_node = create_node(move_left(puzzle, row, column), parent_node, parent_node.depth + 1, 0)
            child_nodes.append(child_node)
            child_node = create_node(move_right(puzzle, row, column), parent_node, parent_node.depth + 1, 0)
            child_nodes.append(child_node)


    child_nodes = [node for node in child_nodes if node.puzzle is not None]
    print("Total", len(child_nodes), "possibilities")
    return child_nodes


def create_node(puzzle, parent, depth, cost):
    return Node(puzzle, parent, depth, cost)


class Node:
    def __init__(self, puzzle, parent, depth, cost):
        self.puzzle = puzzle
        self.parent = parent
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
            if elapsed_time < 60:
                # get a current state node
                node = openList.pop(0)
                if node.puzzle == goal:
                    print(node.puzzle)
                    return "Find solution"
            else:
                return 'No solution'



start_state = "612783549"
#goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
goal_state = '123456789'
start_state = "612783549"
goal = convertToMatrix(goal_state, 3)
current_state = convertToMatrix(start_state, 3)
print()

node = create_node(current_state,None,0,0)

move_up(current_state, 1, 1)
print("Find child node")
findChildNode(node)