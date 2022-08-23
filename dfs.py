n=int(input('Enter the total number of nodes:'))
graph={}
for i in range(n):
    keys=(input('Enter value in node:'))
    values=list(map(str,input('Enter the adjacent nodes of:').split()))
    graph[keys]=values
print(graph)

visited=[]

def dfs(graph,node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)
s=input('Enter start node:')
dfs(graph,s)
print(visited)
