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


def heuristic1(openlist,goal):
    goal_poslist = matrixToPosition(goal)
    index = 0
    min_estimation = 10000
    for node in openlist:
        #puzzle = node.puzzle
        puzzle_poslist = matrixToPosition(node)
        total_estimation = 0

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

        if total_estimation<min_estimation:
            min_estimation = total_estimation
            index = openlist.index(node)

    return index

def heuristic2(openlist):
    index = 0
    min_sum = 10000

    for node in openlist:
        #puzzle = node.puzzle
        puzzle_poslist = matrixToPosition(node)
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


#start_state = "612783549"
start_state1 = "2314"
start_state2 = "2134"
start_state3 = "2143"
start_state4 = "4321"

#goal_state = '123456789'
goal_state = "1234"

goal = convertToMatrix(goal_state, 2)
start_puzzle1 = convertToMatrix(start_state1, 2)
start_puzzle2 = convertToMatrix(start_state2, 2)
start_puzzle3 = convertToMatrix(start_state3, 2)
start_puzzle4 = convertToMatrix(start_state4, 2)

openlist = []
openlist.append(start_puzzle2)
openlist.append(start_puzzle1)
openlist.append(start_puzzle3)
openlist.append(start_puzzle4)

# print(heuristic1(openlist, goal))
print(heuristic2(openlist))
