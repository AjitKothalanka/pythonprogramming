a=list(map(int,input('Enter the vertices seperated by spaces:').split()))
b=a.copy()
n=len(a)
print('Weights are Integers and give "999" for Infinity')
adj_mat=[]
for i in a:
    s=[]
    for j in b:
        l=[i,j]
        print('Current edge :',l)
        m=int(input('Enter distance between these nodes:'))
        l=[]
        s.append(m)
    adj_mat.append(s)

print('The Adjacency matrix is :')
for i in range(n):
    print(adj_mat[i])

for r in range(n):
    for p in range(n):
        for q in range(n):
            adj_mat[p][q]=min(adj_mat[p][q],adj_mat[p][r]+adj_mat[r][q])

print('The All Pair Shortest Distance solution is:')
for i in range(n):
    print(adj_mat[i])

