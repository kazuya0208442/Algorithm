import sys

def main(lines):
    start = lines[0].split()
    goal = lines[1].split()
    odd_parity = [[start[0], start[2], start[1]], [start[1], start[0], start[2]], [start[2], start[1], start[0]]]

    if goal in odd_parity:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)