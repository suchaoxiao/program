'''
P为给定的二维平面整数点集。定义P中某点x，如果x满足P中任意点都不在x的右上方区域内（横纵坐标都大于x），
则称其为为“最大的” “。求出所有”最大的“点的集合。（所有点的横坐标和纵坐标都不重复，坐标轴范围在[0,1e9）内）
如下图：实心点为满足条件的点的集合。请实现代码找到集合P中的所有“最大”点的集合并输出。
https://www.nowcoder.com/test/question/done?tid=23206002&qid=14105
输入描述
第一行输入点集的个数 N， 接下来 N 行，每行两个数字代表点的 X 轴和 Y 轴。
对于 50%的数据,  1 <= N <= 10000;
对于 100%的数据, 1 <= N <= 500000;
输出描述
输出“最大的” 点集合， 按照 X 轴从小到大的方式输出，每行两个数字分别代表点的 X 轴和 Y轴。
例子
输入
5
1 2
5 3
4 6
7 5
9 0
输出
4 6
7 5
9 0
'''
import sys
# n=int(sys.stdin.readline().strip())
# point=[]
# for i in range(n):
#     point.append(list(map(int,sys.stdin.readline().strip().split())))
def print_sort(point):
    point.sort(key=lambda k:k[1],reverse=True)
    res=[]
    res.append(point[0])
    for i in range(1,len(point)):
        if point[i][0]>res[-1][0]:
            res.append(point[i])
        else:
            continue
    res.sort(key=lambda k:k[0])
    for i in res:
        print(i[0],i[1])

if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    point = []
    for i in range(n):
        point.append(list(map(int, sys.stdin.readline().strip().split())))
    print_sort(point)
