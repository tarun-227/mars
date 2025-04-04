def file_to_matrix(file_path):#function to read the file and make a matrix
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            matrix.append(list(map(int, line.strip().split())))
    return matrix


def convert_to_coordinates(matrix):#function to convert directions to x, y coordinates and make arena

    coordinates = []
    x_values, y_values = [], []

    for obs in matrix:
        north, east, south, west = obs
        x = east - west  # x-coordinate
        y = north - south  # y-coordinate
        coordinates.append((x, y))
        x_values.append(x)
        y_values.append(y)

    #finding min and max to decide the size of the arena
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    #size of arena
    width = max_x - min_x + 1
    height = max_y - min_y + 1


    arena = []
    #setting all slots as 1
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(1)
        arena.append(row)

    # putting 0 if obstacle exists there
    for x, y in coordinates:
        arena[y - min_y][x - min_x] = 0  # Adjust for offset

    return arena



file_path = input("Enter the full path of the text file: ")


arena_matrix = convert_to_coordinates(file_to_matrix(file_path))
for row in arena_matrix:
    print(row)
