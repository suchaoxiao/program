# -*- coding: utf-8 -*-
import sys
'''
找出最长的连续公共子串
'''
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

# 相比于最长公共子序列，只不过是转移方程不同
# dpij仍然表示前缀i和前缀j的最长连续公共子串长度

dp = [[0 for j in range(len(s2))] for i in range(len(s1))]
def get_dp(i, j):
    if i < 0 or j < 0:
        return 0
    return dp[i][j]


for i in range(len(s1)):
    for j in range(len(s2)):
        # 如果字符相同，那么在前面已经重复的个数上加1
        if s1[i] == s2[j]:
            dp[i][j] = get_dp(i - 1, j - 1) + 1
        else:
            dp[i][j] = 0

m = 0
#查寻最大子序列长度
for row in dp:
    cur_m = max(row)
    if cur_m > m:
        m = cur_m
print(m)