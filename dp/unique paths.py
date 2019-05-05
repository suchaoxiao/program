import sys


def max_paths_v1(m, n):
    if m == 1 or n == 1:
        return 1
    return max_paths_v1(m - 1, n) + max_paths_v1(m, n - 1)


def max_paths_v2(m, n):
    if m == 1 or n == 1:
        return 1
    mem = {}
    if (m, n) not in mem:
        mem[m, n] = max_paths_v2(m - 1, n) + max_paths_v2(m, n - 1)
    return mem[m, n]


def max_paths_v3(m, n):
    dp = [[1] * (m ) for i in range(n )]

    for i in range(1, n ):
        for j in range(1, m ):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    offset = list(map(int, sys.stdin.readline().strip().split()))
    m, n = offset[:2]
    out = max_paths_v1(m, n)
    out2 = max_paths_v2(m, n)
    out3 = max_paths_v3(m, n)
    print(out, out2, out3)
