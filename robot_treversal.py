def main():
    
m, n = input('Please Enter top-right coordinates of the rectangular plan :\n').split(' ')
x, y, direction = input('Please enter starting position: \n').split(' ')
moves = list(map(str, input('Please Enter Series of movement with spaces: \n').split()))

m = int(m)
n = int(n)
x = float(x)
y = float(y)

x_origin, y_origin = x, y

if direction == 'N':
    y += 0.1
    last_move = 'y'
elif direction == 'E':
    x += 0.1
    last_move = 'x'
elif direction == 'S':
    y -= 0.1
    last_move = 'y'
else:
    x -= 0.1
    last_move = 'x'
        
for i in range(len(moves)):    
    move = moves[i]
    # If move is left or right, then change direction   
    if move == 'R' and last_move == 'x':
        last_move = 'y'
        
    elif move == 'R' and last_move == 'y':
        last_move = 'x'

    elif move == 'L' and last_move == 'y':
        last_move = 'x'
        
    elif move == 'L' and last_move == 'x':
        last_move = 'y'
        
    elif move == 'M':
        if last_move == 'x':
            x += 1
            x_origin += 1
        elif last_move == 'y':
            y += 1
            y_origin += 1
        elif int(x-1) > m or int(y-1) > n:
            print('Out of Plane! Please give another series of movement')
        
print(int(x), int(y), direction)
    
main()