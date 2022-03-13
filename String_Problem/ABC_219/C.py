# 与えられた名前を、新しい文字列の中では何番目なのかを求めて、それを基の文字列に当てはめて、出来上がった文字列を普通にsortすればいい。

import sys
import string

def main(lines):
    X = list(lines[0])
    N = int(lines[1])
    names = [[name, i] for i, name in enumerate(lines[2:])]
    # alphabet = list(string.ascii_lowercase)
    alphabet = [chr(v) for v in range(ord('a'), ord('z') + 1)]

    for i in range(N):
        name, index_num = names[i]
        name = list(name)
        for j in range(len(name)):
            X_index = X.index(name[j])
            name[j] = alphabet[X_index]
        name = ''.join(name)
        names[i].append(name)
    
    names.sort(key=lambda x: x[2])

    for name, index, changed_name in names:
        print(name)
        
    print(names)
    















if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)