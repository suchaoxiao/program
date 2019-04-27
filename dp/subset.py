import sys


def subset_v1(arr,n):
    if n==0:
        return True
    if len(arr)==1:
        return arr[0]==n
    if n-arr[-1]<0:
        return subset_v1(arr[:-1],n)
    return subset_v1(arr[:-1],n-arr[-1]) or subset_v1(arr[:-1],n)

def subset_v2(arr,n):
    arr_set=set()
    for i,v in enumerate(arr):
        if n-v in arr_set:
            return True
        arr_set.add(v)


if __name__=='__main__':
    arr=list(map(int,sys.stdin.readline().strip().split()))
    n=int(sys.stdin.readline().strip())
    out=subset_v1(arr,n)
    print(out)
    out2=subset_v2(arr,n)
    print(out2)