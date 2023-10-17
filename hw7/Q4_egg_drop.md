## Q4

### a
f(1,m) = 1, drop one egg at level 0, if it breaks l is 0 else 1 , because l can be 0 or 1 only.
f(0,m) = 0, l can only be 0.  
f(n,1) = n, only 1 egg, have to go from the bottom and test every floor
f(n,0) = infinity

### b  
if break: need f(x, m -1) tries

if no break: need f(n-x, m) tries

### c  
Base case provided in **a**  
at f(n, m), drop egg at **relative** level `x` s.t. we minimize max(f(x, m-1) == f(n-x, m)), let f(n, m) be that value + 1.

### d  
Incrementing n, decrementing m:
```python
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
```
### e  
O(n^2m), outer loop with n iterations, inner loop with m iterations and smaller inner x loop with n iterations. 

### f
O(n*m) for 2d dp table.