import sys
from typing import List

def main(lines: List):
    N = int(lines[0])
    numbers = [v for v in range(1, 2*N + 2)]

    for _ in range(N + 1):
        # print(numbers[0], flush=True)
        # sys.stdout.write(str(numbers[0]))
        # sys.stdout.flush()
        # sys.stdout.write("\n")
        # sys.stdout.flush()

        print("\r{0}".format(numbers[0]), end='')
        print("\u001B[2A", end="")
        sys.stdout.write("\n")

        numbers.remove(numbers[0])
        num = int(input())

        if num == 0:
            exit()
        numbers.remove(num)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)