import copy

dp = [[-1] * 2 for _ in range(100001)]
dp_p = [[-1] * 2 for _ in range(100001)]

def rot(land):
    for i, layer in enumerate(land):
        layer = copy.deepcopy(land[i])
        layer.sort()
        
        n_fir = layer[3]
        n_sec = layer[2]
        n_fir_idx = land[i].index(n_fir)
        n_sec_idx = land[i].index(n_sec)
        if i == 0:
            dp[0][0], dp[0][1] = n_fir, n_sec
            dp_p[0][0], dp_p[0][1] = n_fir_idx, n_sec_idx
            continue

        if n_fir == n_sec:
            n_fir_idx = [l for l, n in enumerate(land[i]) if n == n_fir][0]
            n_sec_idx = [l for l, n in enumerate(land[i]) if n == n_fir][1]

        if dp_p[i-1][0] != n_fir_idx:
            dp[i][0] = dp[i-1][0] + n_fir
            dp_p[i][0] = n_fir_idx
            dp[i][1] = dp[i-1][0] + n_sec
            dp_p[i][1] = n_sec_idx
        else:
            if dp[i-1][0] + n_sec > dp[i-1][1] + n_fir:
                dp[i][0] = dp[i-1][0] + n_sec
                dp_p[i][0] = n_sec_idx
                dp[i][1] = dp[i-1][1] + n_fir
                dp_p[i][1] = n_fir_idx
            else:
                dp[i][1] = dp[i-1][0] + n_sec
                dp_p[i][1] = n_sec_idx
                dp[i][0] = dp[i-1][1] + n_fir
                dp_p[i][0] = n_fir_idx

    return dp[len(land)-1][0]


def solution(land):
    return rot(land)


print(solution([[1,2,5,3], [1,2,5,5], [1,2,5,3], [1,2,3,5]]))
