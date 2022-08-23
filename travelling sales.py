answer = []
def tsp(graph, v, currPos, n, count, cost):
    if (count == n and graph[currPos][0]):
        answer.append(cost + graph[currPos][0])
        return
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i])
            v[i] = False
v=int(input("Enter total number of vertices :"))
n=v
graph=[]
for i in range(v):
    sublist=list(map(int,input('Enter data row-wise:').split()))
    graph.append(sublist)
    sublist=[]

v = [False for i in range(n)]
v[0] = True
tsp(graph, v, 0, n, 1, 0)
print('The answer is :' ,min(answer))
