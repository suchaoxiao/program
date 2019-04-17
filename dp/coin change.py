import sys


def coin_change(arr,n):
    coin=[1,2,5]
    dp=[]
    dp[1]=1
    dp[2]=1
    dp[5]=1
    for i in range(n):
        for j in range(len(coin)):
            dp[n]=min(dp[i-coin[j]])+1
    return dp[n]


if __name__=="__main__":
    arr=list(map(int,sys.stdin.readline().strip().split()))
    n=int(sys.stdin.readline().strip().split())
    num=coin_change(arr,n)
    print(num)