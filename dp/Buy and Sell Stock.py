import sys

def max_profit(price):
    if not price:
        return 0
    res=0
    profit=[[0 for i in range(3)] for i in range(len(price))]
    #解释profit第二个维度012的意思0表示没有买入股票的时候，1表示买入1支股票的的状态，2表示之前买了一支股票，仙子啊把他卖了的状态
    profit[0][0],profit[0][1],profit[0][2]=0,-price[0],0
    for i in range(1,len(price)):
        profit[i][0]=profit[i-1][0]  #之前没股票，保持不动
        profit[i][1]=max(profit[i-1][1],profit[i-1][0]-price[i])  #之前没股票买入股票和之前有股票的最大
        profit[i][2]=profit[i-1][1]+price[i] #之前有股票，这一步卖掉
        res=max(res,profit[i][0],profit[i][1],profit[i][2])
    return res


if __name__=="__main__":
    price=list(map(int,sys.stdin.readline().strip().split()))
    max_p=max_profit(price)
    print(max_p)