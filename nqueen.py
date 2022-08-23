N = int(input("Enter the number of queens :"))

board = [[0]*N for i in range(N)]

def attack(i, j):
    for k in range(0,N):
        if board[i][k]=='Q' or board[k][j]=='Q':
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]=='Q':
                    return True
    return False

def nqueen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (board[i][j]!='Q'):
                board[i][j] = 'Q'
                if nqueen(n-1)==True:
                    return True
                board[i][j] = 0
    return False

nqueen(N)
for i in board:
    print()
    for j in i:
        print(j,end=' ')

print()

for i in board:
    print()
    i.reverse()
    for j in i :
        print(j,end=' ')
