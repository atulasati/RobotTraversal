import re

AXIS_MAP = {"N": 'y', 'E': 'x', 'S': 'y', 'W':'x'}
SWAP_LAST_MOVE = {'x': 'y', 'y': 'x'}
DIRECTION_MAP = {
    ('R', 'x', 'E'): 'S', 
    ('R', 'x', 'W'): 'N', 
    ('R', 'y', 'N'): 'E', 
    ('R', 'y', 'S'): 'W',
    ('L', 'x', 'W'): 'S', 
    ('L', 'x', 'E'): 'N', 
    ('L', 'y', 'N'): 'W', 
    ('L', 'y', 'S'): 'E',
}

MOVES_MAP = {
    ('x', 'W'): -1, 
    ('x', 'E'): 1, 
    ('y', 'N'): 1, 
    ('y', 'S'): -1,
}

def get_top_right_cord():
    while True:
        top_right_cord = input('Please Enter top-right coordinates of the rectangular plan : ')
        if top_right_cord and len(top_right_cord.split()) == 2:
            if top_right_cord.split(" ")[0].isdigit() and top_right_cord.split(" ")[0].isdigit():
                m = int(top_right_cord.split(" ")[0])
                n = int(top_right_cord.split(" ")[1])
                break
            print("\n\tinvalid input")
    return m, n

def get_x_y_and_direction(m, n):
    while True:
        starting_position = input('Please enter starting position: \nexample: 2 0 E \n')
        if starting_position and len(starting_position.split()) == 3:
            if starting_position.split(" ")[0].isdigit() and starting_position.split(" ")[1].isdigit() and starting_position.split(" ")[2].isalpha():
                x = int(starting_position.split(" ")[0])
                y = int(starting_position.split(" ")[1])
                direction = starting_position.split(" ")[2].upper()
                if x >= 0 and m >= x and y >= 0 and n >= y:
                    break
                print('Please enter valid starting position!')
    return x, y, direction

def get_move_series():
    while True:
        moves = input('Please Enter Series of movement without spaces: \nexample: MLMMLMRM \n').strip()
        if bool(re.match('^[A-Z]+$', moves)):
            break
        print('Please enter valid series of strings. example: MMLRML')
    return moves

def robot_traversal():
    m, n = get_top_right_cord()
    x, y, direction = get_x_y_and_direction(m, n)
    moves = get_move_series()
    traversed_path = []

    last_move = AXIS_MAP[direction]
    for move in moves:
        if move in ["L", "R"]:
            direction = DIRECTION_MAP[(move, last_move, direction)]
            last_move = AXIS_MAP[direction]
        else:
            if last_move == 'x':
                x += MOVES_MAP[(last_move, direction)]
            if last_move == 'y':
                y += MOVES_MAP[(last_move, direction)]
        
        if x<0 or y< 0 or x > m or y > n:
            print('\nOut of Plane! Please give another series of movement')
            break
        
        if move == "M" and (x,y) in traversed_path:
            print(f'The ROBOT already travelled the same coordinate: {x,y}')
            return
        
        traversed_path.append((x,y))

    return f"{x} {y} {direction}"

if __name__ == '__main__':
    res = robot_traversal()
    print(res)