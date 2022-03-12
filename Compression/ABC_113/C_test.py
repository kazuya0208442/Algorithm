import sys

def main(lines):
    N, M = map(int, lines[0].split())
    prefecture = [[] for _ in range(N+1)]
    state_num = 1
    prefecture_year_relationship = [0] * (M+1)

    for row in lines[1:]:
        P, Y = map(int, row.split())
        prefecture[P].append([state_num, Y])
        state_num += 1
    
    for num in range(N+1):
        if len(prefecture[num]) == 0:
            continue
        prefecture[num].sort(key=lambda x: x[1])
        years = set()
        
        for state_num, year in prefecture[num]:
            years.add(year)
        
        relationship = {v:i+1 for i, v in enumerate(sorted(list(years)))}

        for state_num, year in prefecture[num]:
            prefecture_year = ('0'*5 + str(num))[-6:] + ('0'*5 + str(relationship[year]))[-6:]
            prefecture_year_relationship[state_num] = prefecture_year
    
    for i in range(1, M+1):
        print(prefecture_year_relationship[i])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)