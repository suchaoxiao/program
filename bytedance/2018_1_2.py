'''
给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。
如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
[6] = 6 * 6 = 36;
[2] = 2 * 2 = 4;
[1] = 1 * 1 = 1;
[6,2] = 2 * 8 = 16;
[2,1] = 1 * 3 = 3;
[6, 2, 1] = 1 * 9 = 9;
从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。
区间内的所有数字都在[0, 100]的范围内;
输入描述:
第一行输入数组序列长度n，第二行输入数组序列。
对于 50%的数据,  1 <= n <= 10000;
对于 100%的数据, 1 <= n <= 500000;
输出描述:
输出数组经过计算后的最大值。
输入例子1:
3
6 2 1
输出例子1:
36
'''
import sys
def print_max(arr):
    stack = []
    arr.append(0)
    result = 0
    i = 0
    presum = []
    tempsum = 0
    while i < len(arr):
        if not stack or arr[i] >= stack[-1]:
            presum.append(tempsum)
            tempsum = 0
            stack.append(arr[i])
            i += 1
        else:
            temp = stack.pop()
            tempsum += (temp + presum.pop())
            result = max(tempsum * temp, result)
    print(result)


def print_max_1(arr):
    stack=[]
    presum=[]
    temsum=0
    arr.append(0)
    i=0
    result=0
    while(i<len(arr)):
        if not stack or arr[i]>=stack[-1]:
            stack.append(arr[i])
            presum.append(temsum)
            temsum=0
            i+=1
        else:
            temp=stack.pop(-1)
            temsum+=temp+presum.pop()
            result=max(result,temp*temsum)
    print(result)



if __name__=='__main__':
    n=int(sys.stdin.readline().strip())
    arr=list(map(int,sys.stdin.readline().strip().split()))
    print_max_1(arr)
