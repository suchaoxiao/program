import sys

def coin(n):
    dp=[0 for i in range(n+1)]
    coin_list=[1,5,10,20,50,100]
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        for j in coin_list :
            if i>=j:
                dp[i]+=dp[i-j]
    return dp[n]



if __name__=='__main__':
    # n=int(sys.stdin.readline().strip())
    n=10
    out=coin(n)
    print(out)