import sys
data=[]

while True:
    line=list(map(int,sys.stdin.readline().strip().split()))
    if not line:
        break
    else:
        data.append(line)
min=0
index_2=[]
# index_1=[]
while True:
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j]==2:
                index_2.append([i,j])
            # if data[i][j]==1:
            #     index_1.append([i,j])
    count = 0
    for k in index_2:

        if k[0]!=len(data)-1:
            if data[k[0]+1][k[1]]==1:
                data[k[0] + 1][k[1]] = 2
                count+=1
        if k[1] != len(data[0]) - 1:
            if data[k[0]][k[1]+1]==1:
                data[k[0]][k[1] + 1] = 2
                count += 1
        if k[0] != 0:
            if data[k[0]-1][k[1]]==1:
                data[k[0] - 1][k[1]] = 2
                count += 1
        if k[1] != 0:
            if  data[k[0]][k[1]-1]==1:
                data[k[0]][k[1] - 1] = 2
                count += 1
    if count==0:
        break

    min=min+1
l=0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 1:
            l+=1
if l==0:
    print(min)
else:
    print(-1)








    # 1_index=data[i].index(1)
    # 0_index=data[i].index(0)

