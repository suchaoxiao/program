import sys

def twosum(arr,target):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]==target-arr[i]:
                return [i, j]
def twosum_1(arr,target):
    hash_map={}
    for i,x in enumerate(arr):
        if target-x in hash_map:
            return [i,hash_map[target-x]]
        hash_map[x]=i



if __name__=="__main__":
    arr=list(map(int,sys.stdin.readline().strip().split()))
    target=int(sys.stdin.readline().strip())
    index=twosum_1(arr,target)
    print(index)