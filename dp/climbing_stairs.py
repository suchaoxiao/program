import sys
'''
leetcode 70 题
'''

def climbing_s(n):
    if n == 0 or n == 1:
        return 1
    return climbing_s(n-1)+climbing_s(n-2)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    sum = climbing_s(n)
    print(sum)
