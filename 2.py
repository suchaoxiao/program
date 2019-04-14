import sys
def min_cost(alist):
    i = 1
    j = 0
    min_pay = 0
    s = []
    s.append(0)
    while True:
        k=1
        temp=10000000
        while True:
            flag=0
            if k in s:
                flag=1
            if (flag==0) and (alist[k][s[i-1]]<temp):
                j=k
                temp=alist[k][s[i-1]]
            k+=1
            if k>=n:
                break
        s.append(j)
        i+=1
        min_pay+=temp
        if i>=n:
            break
    min_pay+=alist[0][j]
    return min_pay
if __name__=="__main__":
    n=int(sys.stdin.readline().strip())
    alist=[]
    for i in range(n):
        line=sys.stdin.readline().strip()
        values=list(map(int,line.split()))
        alist.append(values)
    cost=min_cost(alist)
    print(cost)

