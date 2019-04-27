import sys


def max_area(arr):
    n=len(arr)
    idx=arr.index(min(arr))
    val1=arr[idx]*n
    if idx!=0:
        val2=max_area(arr[0:idx])
    else:
        val2=0
    if idx!=n-1:
        val3=max_area(arr[idx+1:])
    else:
        val3=0
    return max(val1,val2,val3)


if __name__=='__main__':
    arr=list(map(int,sys.stdin.readline().strip().split()))
    n=int(sys.stdin.readline().strip())
    out=max_area(arr)
    print(out)