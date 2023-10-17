N = 100
M = 2

dp = [[None for j in range(M+1)] for i in range(N + 1)]

for m in range(M + 1):
    dp[0][m] = 0
    dp[1][m] = 1

for n in range(2, N + 1):
    dp[n][1] = n
    dp[n][0] = float("INF")

for n in range(2, N + 1):
    for m in range(M, 1, -1):
        drop_at:int = -1
        minimized_worst_case = float("INF")
        for x in range(1, n + 1):#which level to drop
            worst_case_cost = max(dp[x][m-1], dp[n-x][m])
            if  worst_case_cost < minimized_worst_case:
                minimized_worst_case = worst_case_cost
                drop_at = x
        dp[n][m] = minimized_worst_case + 1

print(dp[100][2])