def main():
    import math
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    fare_list = []

    for i in range(N):
        fir_distance = A[i][0]
        fir_fare = A[i][1]
        add_distance = A[i][2]
        add_fare = A[i][3]

        if X < fir_distance:
            fare_list.append(fir_fare)
        else:
            X_rem = X - fir_distance
            if X_rem % add_distance == 0:
                fare = fir_fare + add_fare * (X_rem // add_distance + 1)
                fare_list.append(fare)
            else:
                fare = fir_fare + add_fare * math.ceil(X_rem / add_distance)
                fare_list.append(fare)

    min_fare = min(fare_list)
    max_fare = max(fare_list)

    return print(min_fare, max_fare)

main()




