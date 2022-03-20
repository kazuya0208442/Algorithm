# [1,0]
# [0,-1]
# [-1,0]
# [0,1]
# [1,0]
# [0,-1]
# [-1,0]
# [0,1]

import sys

def main(lines):
    N = int(lines[0])
    T = list(lines[1])
    position = [0, 0]
    direction = [1, 0]
    to_index = 0

    for string in T:
        if string == 'S':
            for v in direction:
                if v != 0:
                    position[to_index] += v
        else:
            if direction[0] == 1:
                direction = [0, -1]
                to_index = 1
            elif direction[0] == -1:
                direction = [0, 1]
                to_index = 1
            else:
                if direction[1] == 1:
                    direction = [1, 0]
                    to_index = 0
                else:
                    direction = [-1, 0]
                    to_index = 0
    
    print(*position)










if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)