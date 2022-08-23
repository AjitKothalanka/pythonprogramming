INF = 999
N = int(input('Enter number of nodes :'))
G=[]
for i in range(N):
    sublist=list(map(int,input('Enter data row-wise:').split()))
    G.append(sublist)
    sublist=[]
selected_node = list(0 for i in range(N))
no_edge = 0
selected_node[0] = True
print("Edge - Weight\n")

while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
