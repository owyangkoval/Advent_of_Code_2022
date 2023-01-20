# Supply Stacks

def main():
    file = open('Pset5_AoC_input.txt', 'r')

    matrix_list = []
    empty_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    for val in range(100):
        matrix_list.append(empty_list.copy())
    for string in file:
        if not string.strip():
            break
        row_list = list(string[1::4])
        matrix_list.append(row_list)
    matrix_list.pop()

    for string in file:
        split_string = string.strip().split()
        num_boxes = int(split_string[1])
        from_column = int(split_string[3])
        from_column -= 1  # adjust for counting array from 0
        to_column = int(split_string[5])
        to_column -= 1  # adjust for counting array from 0
        supply_stack_moves(num_boxes, from_column, to_column, matrix_list)
        print(num_boxes, from_column, to_column, "num_boxes and columns")
    print_matrix(matrix_list)

def print_matrix(matrix_list):
    for row in matrix_list:
        print(row)

def supply_stack_move(from_column, to_column, matrix_list):
    """ Moves top block from from_column to to_column. """
    from_row = find_from_top_block(from_column, matrix_list)  # find top block of from_column
    to_row = find_to_top_block(to_column, matrix_list)  # find top block of to_column
    if from_row == None:
        return None
    else:
        move_block((from_row, from_column), (to_row, to_column), matrix_list)


def find_from_top_block(column, matrix_list):
    """ Returns row index of top block in column. """
    for row in range(0, len(matrix_list)):
        num_rows = len(matrix_list)-1
        if matrix_list[row][column] != " ":  # retrieves the top of the stack
            return row
        if matrix_list[num_rows][column] == " ":
            return None


def find_to_top_block(column, matrix_list):
    """ Returns row index of top block in column. """
    num_rows = len(matrix_list) - 1
    if matrix_list[num_rows][column] == " ":
        return num_rows
    else:
        for row in range(0, len(matrix_list)):
            if matrix_list[row][column] != " ":  # retrieves the top of the stack
                return row-1


def move_block(from_idx, to_idx, matrix_list):
    """ Moves one block from from_idx to to_idx. """
    from_row = from_idx[0]  # extract value from tuple
    from_column = from_idx[1]  # extract value from tuple
    to_row = to_idx[0]  # extract value from tuple
    to_column = to_idx[1]  # extract value from tuple
    # set to and from indices to new values
    temp_val = matrix_list[from_row][from_column]
    matrix_list[from_row][from_column] = " "
    matrix_list[to_row][to_column] = temp_val


def supply_stack_moves(num_boxes, from_column, to_column, matrix_list):
    """ Moves the top num_boxes boxes from from_column to to_column. """
    rows = 0
    for row in range(0, len(matrix_list)):
        if row != " ":
            rows += 1
    if rows != 0:
        if num_boxes > rows:
            num_boxes = rows
            for num in range(num_boxes):
                supply_stack_move(from_column, to_column, matrix_list)
        if num_boxes < rows:
            for num in range(num_boxes):
                supply_stack_move(from_column, to_column, matrix_list)


if __name__ == '__main__':
    main()