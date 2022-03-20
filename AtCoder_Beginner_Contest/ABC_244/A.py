import sys

def main(lines):
    N = int(lines[0])
    S = lines[1]
    print(S[-1])





if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)