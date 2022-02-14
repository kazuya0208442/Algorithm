import time
k, s, t = map(int, input().split())
DP = [0] * 51
DP[1] = "ABC"

# DP[i] = "A" + DP[i-1] + "B" + DP[i-1] + "C"

for i in range(2, k+1):
    start = time.time()
    DP[i] = "A" + DP[i-1] + "B" + DP[i-1] + "C"
    end = time.time()
    print(end - start)





# 1 3
# 2 3*2+3
# 3 9*2+3
# 4 21*2+3
# 5 45*2+3
# 6 93*2+3
# An = 2An-1 + 3
# Sn = 
