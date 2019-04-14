import sys

def minimumtotal(triangle):
    # pass
    if not triangle:
        return 0
    res=[triangle[-1]]  #二维数组解法
    res=triangle[-1]   #一维数组解法
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            res[j]=min(res[j],res[j+1])+triangle[i][j]  #一维数组解法
            # res[-1][j]=min(res[-1][j],res[-1][j+1])+triangle[i][j] #二维数组解法
    # return res[0][0]  #二维数组解法
    return res[0]   #一维数组解法

if __name__=='__main__':
    n=int(sys.stdin.readline().strip())
    triangle=[]
    for i in range(n):
        line=list(map(int,sys.stdin.readline().strip().split()))
        triangle.append(line)
    minimum=minimumtotal(triangle)
    print(minimum)