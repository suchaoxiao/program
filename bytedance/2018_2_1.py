import sys

n = int(sys.stdin.readline().strip())
q = list(map(int,sys.stdin.readline().strip().split()))
like_dict = {}
for i in range(len(q)):
    if q[i] not in like_dict:
        like_dict[q[i]] = [i + 1]
    else:
        like_dict[q[i]].append(i + 1)
m = int(sys.stdin.readline().strip())
data_list = list()
output = list()
for i in range(m):
    query = list(map(int,sys.stdin.readline().strip().split()))
    data_list.append(query)
for data in data_list:
    num = 0
    min = data[0]
    max=data[1]
    if data[2] in like_dict:
        for i in like_dict[data[2]]:
            if i<=max and i>=min:
                num+=1
    output.append(num)
for i in output:
    print (i)
