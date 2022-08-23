def find(i):
	while parent[i] != i:
		i=parent[i]
	return i
def union(i, j):
	a=find(i)
	b=find(j)
	parent[a]=b
def kruskalMST(G):
	mincost=0 
	for i in range(V):
		parent[i]=i
	edge_count=0
	while edge_count<V-1:
		min=INF
		a=-1
		b=-1
		for i in range(V):
			for j in range(V):
				if find(i) != find(j) and G[i][j]<min:
					min=G[i][j]
					a=i
					b=j
		union(a, b)
		print('Edge {} : ({}, {}) Cost:{}'.format(edge_count, a+1, b+1, min))
		edge_count += 1
		mincost += min

	print("Minimum cost= {}".format(mincost))

INF=999
print('Enter "999" as input for INF')
V = int(input('Enter number of nodes :'))
parent=[i for i in range(V)]
G=[]
for i in range(V):
    sublist=list(map(int,input('Enter data row-wise:').split()))
    G.append(sublist)
    sublist=[]
kruskalMST(G)
