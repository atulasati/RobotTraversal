def robot_traversal():
    while True:
        top_right_cord = input('Please Enter top-right coordinates of the rectangular plan : ')
        if top_right_cord and len(top_right_cord.split()) == 2:
            if top_right_cord.split(" ")[0].isdigit() and top_right_cord.split(" ")[0].isdigit():
                m = int(top_right_cord.split(" ")[0])
                n = int(top_right_cord.split(" ")[1])
                break
            print("\n\tinvalid input")

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
    
    while True:
        moves = ""
        movement = input('Please Enter Series of movement without spaces: \nexample: MLMMLMRM \n')
        for i in range(len(movement)):    
            move = movement[i].upper()
            if move.isalpha():
                moves += move
            else:
                print('Please enter valid series of strings. example: MMLRML')
        break

    if direction == 'N':
        last_move = 'y'
    elif direction == 'E':
        last_move = 'x'
    elif direction == 'S':
        last_move = 'y'
    else:
        last_move = 'x'

    path = []

    for i in range(len(movement)):    
        move = movement[i]
        path.append((x,y))
        # If move is left or right, then change direction   
        if move == 'R' and last_move == 'x':
            last_move = 'y'
            if direction == 'E':
                direction = 'S'
            else:
                direction = 'N'
            
        elif move == 'R' and last_move == 'y':
            last_move = 'x'
            if direction == 'N':
                direction = 'E'
            else:
                direction = 'W'

        elif move == 'L' and last_move == 'y':
            last_move = 'x'
            if direction == 'N':
                direction = 'W'
            else:
                direction = 'E'
            
        elif move == 'L' and last_move == 'x':
            last_move = 'y'
            if direction == 'E':
                direction = 'N'
            else:
                direction = 'S'
            
        elif move == 'M':
            if last_move == 'x' and direction=='E': x += 1
                
            elif last_move == 'x' and direction=='W': x -= 1
            
            elif last_move == 'y' and direction=='N': y += 1

            elif last_move == 'y' and direction=='S': y -= 1
                
            elif x > m or y > n:
                print('Out of Plane! Please give another series of movement')
                break
        
        for i in path:
            if (x, y) == i:
                print(f'The ROBOT already travelled the same coordinate: {i}')
                return int(x), int(y), direction

    print(int(x), int(y), direction)
    
if __name__ == '__main__':
    robot_traversal()