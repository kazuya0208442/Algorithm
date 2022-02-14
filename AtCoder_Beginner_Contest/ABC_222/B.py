

def main():
    N, P = map(int, input().split())
    score_list = list(map(int, input().split()))
    drop_num = 0

    for i in range(N):
        if score_list[i] < P:
            drop_num += 1
    
    print(drop_num)

main()