import sys

def maxsubarr_1(nums):
    if not nums:
        return 0
    dp=[[0 for _ in range(2)] for _ in range(2)]
    dp[0][1],dp[0][0],res=nums[0],nums[0],nums[0]
    for i in range(1,len(nums)):
        x,y=i%2,(i-1)%2
        dp[x][0]=max(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])
        dp[x][1]=min(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])
        res=max(res,dp[x][0])
    return res


def maxsubarr(nums):
    if  nums is None:
        return 0
    res,curmax,curmin=nums[0],nums[0],nums[0]
    for i in range(1,len(nums)):
        num=nums[i]
        curmax,curmin=curmax*num,curmin*num
        curmin,curmax= min(curmax,curmin,num),max(curmax,curmin,num)
        res=curmax if curmax>res else res
    return res

if __name__=='__main__':
    arr=list(map(int,sys.stdin.readline().strip().split()))
    max_1=maxsubarr(arr)
    print(max_1)
    max_2=maxsubarr_1(arr)
    print(max_2)