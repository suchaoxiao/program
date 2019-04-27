import sys

def fib_v1(n): #递归解法
    if n==0 or n==1:
        return 1
    return fib_v1(n-1)+fib_v1(n-2)
def fib_v2(n):
    dp=[1]*(n+1)
    for i in range(2,n+1):
        dp[i]=dp[i-2]+dp[i-1]
    return dp[-1]


if __name__=='__main__':
    n=int(sys.stdin.readline().strip())
    out=fib_v1(n)
    print('v1: '+str(out))
    out2=fib_v2(n)
    print('v2: '+str(out))
