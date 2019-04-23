import sys


def max_area(arr):
    mini_area=max(arr[:])
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            area=min(arr[i:j])*(j-i)
            if area>mini_area:
                mini_area=area
    return mini_area

'''
分治法：最大矩形面积只可能有三种情况：
1. 取决于高度最小的柱子，此时面积等于高度乘总长度；
2. 最大面积出现在高度最小的柱子左边；
3. 最大面积出现在高度最小的柱子右边；
'''
def large_area(arr):
    l=len(arr)
    idx=arr.index(min(arr))
    val1=arr[idx]*l
    if idx!=0:
        val2=largestarea(arr[0:idx])
    else:
        val2=0
    if idx!=l-1:
        val3=largestarea(arr[idx+1:l])
    else:
        val3=0
    return max(val1,val2,val3)



def largestarea(a):
    l = len(a)
    idx = a.index(min(a))

    value1 = a[idx] * l

    if idx != 0:
        value2 = largestarea(a[0:idx])
    else:
        value2 = 0
    if idx != l - 1:
        value3 = largestarea(a[idx + 1:l])
    else:
        value3 = 0
    return max(value1, value2, value3)

if __name__=='__main__':
    n=int(sys.stdin.readline().strip())
    arr=list(map(int,sys.stdin.readline().strip().split()))
    out=max_area(arr)
    out_1=largestarea(arr)
    print(out_1)
    print(out)