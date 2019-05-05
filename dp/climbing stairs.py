import sys


def climbing_v1(n):
    if n == 0 or n == 1:
        return 1
    return climbing_v1(n - 1) + climbing_v1(n - 2)


def climbing_v2(n):
    if n == 1 or n == 0:
        return 1
    # men = [0] * (n + 1)
    men = {}  # 创建一个字典用来保存中间数据
    if n not in men:
        men[n] = climbing_v2(n - 1) + climbing_v2(n - 2)
    return men[n]


def climbing_v3(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


def climbing_v4(n):
    dp1, dp2 = 1, 1
    for i in range(2, n + 1):
        dp2, dp1 = dp1 + dp2, dp2
    return dp2


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    out1 = climbing_v1(n)
    out2 = climbing_v2(n)
    out3 = climbing_v3(n)
    out4 = climbing_v4(n)
    print(out1, out2, out3, out4)
