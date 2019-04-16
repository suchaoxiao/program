import sys


def longestincreaseseq(arr):
    # pass
    if not arr:
        return 0
    dp=[1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return dp[-1]

def output_maxarr(arr):
    if not arr:
        return []

    max_arr=[]
    max_arr.append(arr[0])
    for i in range(len(arr)):
        if max_arr[-1]<arr[i]:
            max_arr.append(arr[i])
        else:
            max_arr[-1]=arr[i]
    return max_arr


if __name__=="__main__":
    arr=list(map(int,sys.stdin.readline().strip().split()))
    num=longestincreaseseq(arr)
    print(num)
    s=output_maxarr(arr)
    for i in range (len(s)):
        print(s[i])
