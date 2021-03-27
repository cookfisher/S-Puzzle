import S_Puzzle
import random

def generate_input_matrix(n):
    # choice method can generate unique number, randint can't
    #matrix = np.random.choice(range(1,n*n+1,1), (n,n), replace=False)
    #matrix = np.random.choice(range(1, n * n + 1, 1), n*n, replace=False)
    #matrix = list(range(1, n * n + 1))
    matrix = list(range(1, n * n + 1))
    random_matrix = random.shuffle(matrix)
    #matrix = random.shuffle(list(range(1, n * n + 1)))
    print(random_matrix)

    input_matrix = []
    temp_list = []

    col_counter = 0
    row_counter = 0
    index = 0

    while index < len(matrix):
        if col_counter < n:
            temp_list.append(matrix[index])
            col_counter = col_counter + 1
            index = index + 1

            #print('the row number is ', row_counter + 1)
            #print('the colume number is ', col_counter)
            #print('the temp list is in the row ',temp_list)
        else:
            input_matrix.append(temp_list)
            row_counter = row_counter + 1
            col_counter = 0
            #print('the row number is ', index)
            #print('the input list is in the row ', input_matrix)
            temp_list = []

        if index == n*n:
            input_matrix.append(temp_list)
    print('The generate matrix is :', input_matrix)

    return input_matrix


def generate_goal_matrix(n):
    g_matrix = list(range(1, n*n+1))
    #goal_matrix = np.array(goal_matrix).reshape((n,n))
    #print(goal_matrix)

    goal_matrix = []
    temp_list = []

    col_counter = 0
    row_counter = 0
    index = 0

    while index < len(g_matrix):
        if col_counter < n:
            temp_list.append(g_matrix[index])
            col_counter = col_counter + 1
            index = index + 1

            #print('the row number is ', row_counter + 1)
            #print('the colume number is ', col_counter)
            #print('the temp list is in the row ',temp_list)
        else:
            goal_matrix.append(temp_list)
            row_counter = row_counter + 1
            col_counter = 0
            #print('the row number is ', index)
            #print('the input list is in the row ', input_matrix)
            temp_list = []

        if index == n*n:
            goal_matrix.append(temp_list)
    print('The goal matrix is :', goal_matrix)

    return goal_matrix


n = 4
s = generate_input_matrix(n)
g = generate_goal_matrix(n)
print('The start matrix is', s)
print('The goal matrix is', g)
#start = depth_first.convertToMatrix(s, 4)
#goal = depth_first.convertToMatrix(g, 4)

#AStar(start_puzzle, goal, 1)

output_h1_solution = open("Output_h1_solution.txt", "w")
output_h1_search = open("Output_h1_search.txt", "w")
S_Puzzle.AStar(s, g, 1,output_h1_solution,output_h1_search)
output_h1_solution.close()
output_h1_search.close()
