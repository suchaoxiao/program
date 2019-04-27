import sys

def aver_age(w,y,x,n):
    while n:
        average = ((y+1)*w*(1-x)+21*w*x)/w
        y=average
        n-=1
    if average>int(average):
        return int(average)+1
    return int(average)

if __name__=='__main__':
    arr=list(map(str,sys.stdin.readline().strip().split()))
    w=int(arr[0])
    y=int(arr[1])
    x=float(arr[2])
    n=int(arr[3])

    out=aver_age(w,y,x,n)
    print(out)
