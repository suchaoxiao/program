import sys


def max_act(n):
    max=0
    if n==1:
        return 1
    if n==2:
        return 2
    max+=max_act(n-1)+max_act(n-2)
    return max


if __name__=='__main__':
    n=int(sys.stdin.readline().strip())
    out=max_act(n)
    print(out)
