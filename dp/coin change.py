import sys


def coin_change(coins,amount):
    dp = [0] + [-1] * amount
    for x in range(amount):
        if dp[x] < 0:
            continue
        for c in coins:
            if x + c > amount:
                continue
            if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                dp[x + c] = dp[x] + 1
    return dp[amount]

def coinChange( coins, amount):
    dp = [0]   #dp表示的是组成当前面值需要最少的基础面值币数
    length = len(coins)
    for i in range(1, amount + 1):
        dp += [9999]    #相当于list 的append（）方法，加入9999这个元素
        for j in range(length):
            if i >= coins[j] and dp[int(i - coins[j])] != 9999:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    if dp[amount] == 9999:
        return -1
    return dp[amount]

if __name__=="__main__":
    arr=list(map(int,sys.stdin.readline().strip().split()))
    n=int(sys.stdin.readline().strip())
    # num=coin_change(arr,n)
    num=coinChange(arr,n)
    print(num)
