import time

class Node:
    def __init__(self, puzzle, parent, depth, heuristic):
        self.puzzle = puzzle
        self.parent = parent
        self.depth = depth
        self.heuristic = heuristic

class Position:
    def __init__(self, character, row, column):
        self.character = character
        self.row = row
        self.column = column

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
        #print(new_puzzle)
        return new_puzzle
    else:
        return None

def move_down(puzzle, row, column):
    new_puzzle = [x[:] for x in puzzle]
    if row != len(puzzle)-1:
        new_puzzle[row][column], new_puzzle[row+1][column] = new_puzzle[row+1][column], new_puzzle[row][column]
        #print(new_puzzle)
        return new_puzzle
    else:
        return None

def move_left(puzzle, row, column):
    new_puzzle = [x[:] for x in puzzle]
    if column != 0:
        new_puzzle[row][column], new_puzzle[row][column-1] = new_puzzle[row][column-1], new_puzzle[row][column]
        #print(new_puzzle)
        return new_puzzle
    else:
        return None

def move_right(puzzle, row, column):
    new_puzzle = [x[:] for x in puzzle]
    if column != len(puzzle[0])-1:
        new_puzzle[row][column], new_puzzle[row][column+1] = new_puzzle[row][column+1], new_puzzle[row][column]
        #print(new_puzzle)
        return new_puzzle
    else:
        return None

def findChildNodes(parent_node):
    puzzle = parent_node.puzzle
    #print(puzzle)
    rows = len(puzzle)
    columns = len(puzzle[0])
    child_nodes = []

    for row in range(rows):
        for column in range(columns):
            #print("Puzzle", puzzle[row][column])
            child_node = create_node(move_up(puzzle, row, column), parent_node, parent_node.depth+1, 0)
            child_nodes.append(child_node)
            child_node = create_node(move_down(puzzle, row, column), parent_node, parent_node.depth + 1, 0)
            child_nodes.append(child_node)
            child_node = create_node(move_left(puzzle, row, column), parent_node, parent_node.depth + 1, 0)
            child_nodes.append(child_node)
            child_node = create_node(move_right(puzzle, row, column), parent_node, parent_node.depth + 1, 0)
            child_nodes.append(child_node)

    child_nodes = [node for node in child_nodes if node.puzzle is not None]
    #print("Total", len(child_nodes), "possibilities")
    return child_nodes


def create_node(puzzle, parent, depth, cost):
    return Node(puzzle, parent, depth, cost)


def dfs(start, goal):
    openList = []
    closeList = []
    puzzle_dict = []

    start_node = create_node(start,None,0,0)
    openList.append(start_node)

    puzzle_str = "".join(element for sub in start_node.puzzle for element in sub)
    puzzle_dict.append(puzzle_str)

    # timing
    start_time = time.time()

    while len(openList) > 0:
        #print("OpenList", len(openList))
        #print("CloseList", len(closeList))
        elapsed_time = time.time() - start_time
        if elapsed_time < 60:
            # get left most node
            current_node = openList.pop()
            closeList.append(current_node)

            # check if find goal puzzle
            if current_node.puzzle == goal:
                print("Find solution")
                print(current_node.puzzle)
                path = []
                temp = current_node
                print(temp.depth)
                while True:
                    current_str = convertMatrixToString(temp.puzzle)
                    path.insert(0, current_str)
                    if temp.depth <= 0:
                        break
                    temp = temp.parent

                print(path)
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                return path
            else:
                child_nodes = findChildNodes(current_node)
                for node in child_nodes:
                    puzzle_str = "".join(element for sub in node.puzzle for element in sub)
                    # check if it's in closeList & openList
                    if puzzle_str in puzzle_dict:
                        #print("in")
                        continue
                    else:
                        puzzle_dict.append(puzzle_str)
                        print(puzzle_str)
                        openList.append(node)
        else:
            print("No solution")
            return 'No solution'



def iterativeDeepening(start, goal):
    openList = []
    closeList = []
    depth_limit = 1
    puzzle_dict = []

    start_node = create_node(start,None,0,0)
    openList.append(start_node)

    puzzle_str = "".join(element for sub in start_node.puzzle for element in sub)
    puzzle_dict.append(puzzle_str)

    # timing
    start_time = time.time()

    while len(openList) > 0:
        #print("OpenList", len(openList))
        #print("CloseList", len(closeList))
        elapsed_time = time.time() - start_time
        if elapsed_time < 60:
            # get left most node
            current_node = openList.pop()
            closeList.append(current_node)

            # check if find goal puzzle
            if current_node.puzzle == goal:
                print("Find solution")
                print(current_node.puzzle)
                path = []
                temp = current_node
                print(temp.depth)
                while True:
                    current_str = convertMatrixToString(temp.puzzle)
                    path.insert(0, current_str)
                    if temp.depth <= 0:
                        break
                    temp = temp.parent

                print(path)
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                return path
            else:
                if current_node.depth < depth_limit:
                    print("Depth = ", current_node.depth)
                    child_nodes = findChildNodes(current_node)
                    for node in child_nodes:
                        puzzle_str = "".join(element for sub in node.puzzle for element in sub)
                        # check if it's in closeList & openList
                        if puzzle_str in puzzle_dict:
                            #print("in")
                            continue
                        else:
                            puzzle_dict.append(puzzle_str)
                            print(puzzle_str)
                            openList.append(node)

                if len(openList) == 0:
                    print("No solution, run out of states")
                    return 'No solution'
        else:
            print("No solution")
            return 'No solution'


def AStar(start, goal, heuristic):
    openList = []
    closeList = []
    puzzle_list = []

    start_node = create_node(start,None,0,0)
    openList.append(start_node)

    puzzle_str = "".join(element for sub in start_node.puzzle for element in sub)
    puzzle_list.append(puzzle_str)

    # timing
    start_time = time.time()

    while len(openList) > 0:
        #print("OpenList", len(openList))
        #print("CloseList", len(closeList))
        elapsed_time = time.time() - start_time
        if elapsed_time < 60:
            # get left most node
            if heuristic == 1:
                index = heuristic1(openList, goal)
            elif heuristic == 2:
                index = heuristic2(openList)
            else:
                current_node = openList.pop()
            current_node = openList.pop(index)
            closeList.append(current_node)

            # check if find goal puzzle
            if current_node.puzzle == goal:
                print("Find solution")
                print(current_node.puzzle)
                path = []
                temp = current_node
                print("Depth", temp.depth)
                while True:
                    current_str = convertMatrixToString(temp.puzzle)
                    path.insert(0, current_str)
                    if temp.depth <= 0:
                        break
                    temp = temp.parent

                print("Path", path)
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                return path
            else:
                child_nodes = findChildNodes(current_node)
                for node in child_nodes:
                    puzzle_str = "".join(element for sub in node.puzzle for element in sub)
                    # check if it's in closeList & openList
                    if puzzle_str in puzzle_list:
                        #print("in")
                        continue
                    else:
                        puzzle_list.append(puzzle_str)
                        print(puzzle_str)
                        openList.append(node)
        else:
            print("No solution")
            return 'No solution'


def matrixToPosition(puzzle):
    poslist = []
    rows = len(puzzle)
    columns = len(puzzle[0])

    for row in range(rows):
        for column in range(columns):
            character = puzzle[row][column]
            temp = Position(character, row, column)
            poslist.append(temp)

    return poslist


def convertMatrixToString(puzzle):
    puzzle_str = "".join(element for sub in puzzle for element in sub)
    return puzzle_str


# using manhattan distance
def heuristic1(openlist, goal):
    goal_poslist = matrixToPosition(goal)
    index = 0
    min_estimation = 10000
    for node in openlist:
        puzzle = node.puzzle
        puzzle_poslist = matrixToPosition(puzzle)
        total_estimation=0

        for pos_t in puzzle_poslist:
            char_p = pos_t.character
            row_p = pos_t.row
            column_p = pos_t.column
            for pos_g in goal_poslist:
                if pos_g.character == char_p:
                    row_g = pos_g.row
                    column_g = pos_g.column
                    estimation = abs(row_g-row_p)+abs(column_g-column_p)
                    total_estimation += estimation

        if total_estimation < min_estimation:
            min_estimation = total_estimation
            index = openlist.index(node)

    return index


# using sum of permutation inversions
def heuristic2(openlist):
    index = 0
    min_sum = 10000

    for node in openlist:
        puzzle = node.puzzle
        puzzle_poslist = matrixToPosition(puzzle)
        sum = 0

        for element_current in puzzle_poslist:
            char_current = element_current.character
            for element_next in puzzle_poslist:
                char_next = element_next.character
                if puzzle_poslist.index(element_next) > puzzle_poslist.index(element_current) and char_current > char_next:
                    sum += 1

        if min_sum > sum:
            min_sum = sum
            index = openlist.index(node)

    return index


#start_state = "2314"
#goal_state = "1234"
start_state = "612783549"
goal_state = '123456789'

goal = convertToMatrix(goal_state, 3)
start_puzzle = convertToMatrix(start_state, 3)
print()

#dfs(start_puzzle, goal)
iterativeDeepening(start_puzzle, goal)
#AStar(start_puzzle, goal, 1)
#AStar(start_puzzle, goal, 2)