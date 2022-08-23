n=int(input('Enter the total number of nodes:'))
graph={}
for i in range(n):
    keys=(input('Enter value in node:'))
    values=list(map(str,input('Enter the adjacent nodes of:').split()))
    graph[keys]=values
print(graph)


def bfs(graph, start):
    result = []
    queue = [start]
    visited= [start]    

    while queue:
        node = queue.pop(0)
        result.append(node)
        adjacent = graph[node]

        for j in adjacent:
            if j not in visited:
                queue.append(j)
                visited.append(j)
    return result
s=input('Enter start node:')
ans = bfs(graph,s)
print(ans)

    
