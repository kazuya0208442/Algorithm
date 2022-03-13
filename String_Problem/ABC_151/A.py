import sys
import string

lines = []
for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))

C = lines[0]
# alphabet = list(string.ascii_lowercase)
alphabet = [chr(v) for v in range(ord('a'), ord('z') + 1)]


next_index = ord(C) + 1 - ord('a')

print(alphabet[next_index])
