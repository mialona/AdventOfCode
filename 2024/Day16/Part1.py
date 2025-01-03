from warnings import warn
import heapq

class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

def return_path(current_node):
    path = []
    current = current_node
    print(current.g)
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze, start, end, allow_diagonal_movement = False):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node = Node(Node(None, (start[0], start[1] - 1)), start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
          # if we hit this point return the path such as it is
          # it will not contain the destination
          warn("giving up on pathfinding too many iterations")
          return return_path(current_node)

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []

        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != '.' and maze[node_position[0]][node_position[1]] != 'S' and maze[node_position[0]][node_position[1]] != 'E':
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            if current_node.position[0] == child.position[0] - 1 and current_node.parent.position[0] != current_node.position[0] - 1:
                child.g = current_node.g + 1001;
            else:
                if current_node.position[0] == child.position[0] + 1 and current_node.parent.position[0] != current_node.position[0] + 1:
                    child.g = current_node.g + 1001;
                else:
                    if current_node.position[1] == child.position[1] + 1 and current_node.parent.position[1] != current_node.position[1] + 1:
                        child.g = current_node.g + 1001;
                    else:
                        if current_node.position[1] == child.position[1] - 1 and current_node.parent.position[1] != current_node.position[1] - 1:
                            child.g = current_node.g + 1001;
                        else:
                            child.g = current_node.g + 1;
            child.h = 0.001*((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None

def printMap(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            print(map[i][j], end='');
        print();
    print();

##with open('test1.txt', 'r') as file:
with open('input.gnumeric', 'r') as file:
    i = 0;
    map = [];
    start = None;
    end = None;
    lines = file.readlines();
    while i < len(lines):
        line = lines[i].strip();
        if len(line) > 0:
            if line.find('S') > -1:
                start = (i,line.find('S'));
            if line.find('E') > -1:
                end = (i,line.find('E'));
            map.append(list(line));
        i = i + 1;

    path = astar(map, start, end)
    path2 = [(139, 1), (139, 2), (139, 3), (139, 4), (139, 5), (139, 6), (139, 7), (138, 7), (137, 7), (136, 7), (135, 7), (134, 7), (133, 7), (132, 7), (131, 7), (131, 8), (131, 9), (131, 10), (131, 11), (131, 12), (131, 13), (130, 13), (129, 13), (128, 13), (127, 13), (126, 13), (125, 13), (125, 14), (125, 15), (126, 15), (127, 15), (127, 16), (127, 17), (128, 17), (129, 17), (129, 18), (129, 19), (129, 20), (129, 21), (130, 21), (131, 21), (131, 22), (131, 23), (131, 24), (131, 25), (131, 26), (131, 27), (131, 28), (131, 29), (131, 30), (131, 31), (131, 32), (131, 33), (131, 34), (131, 35), (131, 36), (131, 37), (131, 38), (131, 39), (131, 40), (131, 41), (132, 41), (133, 41), (133, 42), (133, 43), (133, 44), (133, 45), (133, 46), (133, 47), (133, 48), (133, 49), (133, 50), (133, 51), (133, 52), (133, 53), (134, 53), (135, 53), (136, 53), (137, 53), (137, 54), (137, 55), (138, 55), (139, 55), (139, 56), (139, 57), (139, 58), (139, 59), (139, 60), (139, 61), (138, 61), (137, 61), (137, 62), (137, 63), (136, 63), (135, 63), (135, 64), (135, 65), (134, 65), (133, 65), (133, 64), (133, 63), (132, 63), (131, 63), (131, 64), (131, 65), (131, 66), (131, 67), (132, 67), (133, 67), (134, 67), (135, 67), (135, 68), (135, 69), (135, 70), (135, 71), (135, 72), (135, 73), (134, 73), (133, 73), (133, 74), (133, 75), (134, 75), (135, 75), (135, 76), (135, 77), (135, 78), (135, 79), (135, 80), (135, 81), (135, 82), (135, 83), (135, 84), (135, 85), (135, 86), (135, 87), (134, 87), (133, 87), (133, 88), (133, 89), (133, 90), (133, 91), (133, 92), (133, 93), (134, 93), (135, 93), (135, 94), (135, 95), (134, 95), (133, 95), (132, 95), (131, 95), (130, 95), (129, 95), (128, 95), (127, 95), (126, 95), (125, 95), (124, 95), (123, 95), (122, 95), (121, 95), (120, 95), (119, 95), (118, 95), (117, 95), (116, 95), (115, 95), (114, 95), (113, 95), (113, 96), (113, 97), (113, 98), (113, 99), (112, 99), (111, 99), (111, 100), (111, 101), (111, 102), (111, 103), (110, 103), (109, 103), (109, 104), (109, 105), (110, 105), (111, 105), (111, 106), (111, 107), (110, 107), (109, 107), (109, 108), (109, 109), (108, 109), (107, 109), (107, 110), (107, 111), (107, 112), (107, 113), (108, 113), (109, 113), (110, 113), (111, 113), (111, 114), (111, 115), (112, 115), (113, 115), (113, 116), (113, 117), (113, 118), (113, 119), (113, 120), (113, 121), (114, 121), (115, 121), (116, 121), (117, 121), (117, 122), (117, 123), (117, 124), (117, 125), (116, 125), (115, 125), (114, 125), (113, 125), (113, 126), (113, 127), (112, 127), (111, 127), (110, 127), (109, 127), (108, 127), (107, 127), (107, 126), (107, 125), (106, 125), (105, 125), (105, 126), (105, 127), (105, 128), (105, 129), (104, 129), (103, 129), (102, 129), (101, 129), (101, 130), (101, 131), (100, 131), (99, 131), (98, 131), (97, 131), (96, 131), (95, 131), (94, 131), (93, 131), (92, 131), (91, 131), (90, 131), (89, 131), (88, 131), (87, 131), (86, 131), (85, 131), (84, 131), (83, 131), (83, 132), (83, 133), (82, 133), (81, 133), (81, 134), (81, 135), (80, 135), (79, 135), (78, 135), (77, 135), (76, 135), (75, 135), (74, 135), (73, 135), (72, 135), (71, 135), (71, 136), (71, 137), (70, 137), (69, 137), (68, 137), (67, 137), (66, 137), (65, 137), (64, 137), (63, 137), (62, 137), (61, 137), (60, 137), (59, 137), (58, 137), (57, 137), (56, 137), (55, 137), (54, 137), (53, 137), (52, 137), (51, 137), (51, 136), (51, 135), (51, 134), (51, 133), (50, 133), (49, 133), (48, 133), (47, 133), (46, 133), (45, 133), (44, 133), (43, 133), (42, 133), (41, 133), (40, 133), (39, 133), (38, 133), (37, 133), (36, 133), (35, 133), (34, 133), (33, 133), (32, 133), (31, 133), (31, 132), (31, 131), (30, 131), (29, 131), (28, 131), (27, 131), (27, 130), (27, 129), (26, 129), (25, 129), (25, 128), (25, 127), (25, 126), (25, 125), (25, 124), (25, 123), (26, 123), (27, 123), (27, 122), (27, 121), (27, 120), (27, 119), (26, 119), (25, 119), (24, 119), (23, 119), (23, 118), (23, 117), (22, 117), (21, 117), (21, 116), (21, 115), (21, 114), (21, 113), (20, 113), (19, 113), (19, 112), (19, 111), (18, 111), (17, 111), (16, 111), (15, 111), (15, 110), (15, 109), (14, 109), (13, 109), (12, 109), (11, 109), (10, 109), (9, 109), (9, 110), (9, 111), (8, 111), (7, 111), (7, 112), (7, 113), (7, 114), (7, 115), (7, 116), (7, 117), (7, 118), (7, 119), (7, 120), (7, 121), (6, 121), (5, 121), (5, 122), (5, 123), (4, 123), (3, 123), (3, 124), (3, 125), (3, 126), (3, 127), (3, 128), (3, 129), (2, 129), (1, 129), (1, 130), (1, 131), (1, 132), (1, 133), (1, 134), (1, 135), (2, 135), (3, 135), (3, 136), (3, 137), (2, 137), (1, 137), (1, 138), (1, 139)]
    print(len(path) - 1);
    for i in range(len(path2) - 1):
        if map[path2[i][0]][path2[i][1]] == '.':
            map[path2[i][0]][path2[i][1]] = 'X';
    for i in range(len(path) - 1):
        if map[path[i][0]][path[i][1]] == '.':
            map[path[i][0]][path[i][1]] = 'O';
    printMap(map)