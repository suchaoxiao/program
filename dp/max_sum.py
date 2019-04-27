import sys

#递归版本，对于递归取最优问题，画出递归树，就可以写出递归方程，然后找边界条件就可以设置判断递归返回的条件
def max_sum_v1(arr):
    if len(arr)<3:
        return max(arr)
    return max(max_sum_v1(arr[:-1]),arr[-1]+max_sum_v1(arr[:-2]))
#动态规划，定义状态，转移方程，边界条件
def max_sum_v2(arr):
    dp=[0]*(len(arr))
    dp[0]=arr[0]
    dp[1]=max(arr[1],arr[0])
    for i in range(2,len(arr)):
        dp[i]=max(dp[i-1],arr[i]+dp[i-2])
    return dp[-1]


if __name__=='__main__':
    arr=list(map(int,sys.stdin.readline().strip().split()))
    out=max_sum_v1(arr)
    print(out)
    out2=max_sum_v2(arr)
    print(out2)