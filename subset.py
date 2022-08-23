def exist(l, n, req) :
   if (req == 0) :
      return True
   if (n == 0 and req != 0) :
      return False
   if (l[n - 1] > req) :
      return exist(l, n - 1, req);
   return exist(l, n-1, req) or exist(l, n-1, req-l[n-1])

def subsetsum(s,a,rem):
    x[a]=1
    if s+l[a]==req:
        z=[]
        for i in range (0,a+1):
            if x[i]==1:
                z.append(l[i])
        print(z)     
    elif s+l[a]+l[a+1]<=req :
        subsetsum(s+l[a],a+1,rem-l[a])
    if s+rem-l[a]>=req and s+l[a+1]<=req :
        x[a]=0
        subsetsum(s,a+1,rem-l[a])


l = list(map(int,input('Enter the list :').split()))
l.sort()
total=sum(l)
req = int(input("Enter required sum :"))
n = len(l)
if (exist(l, n, req) == True) :
   print("Found a subset with given sum.")
   x=[0]*(n+1)
   subsetsum(0,0,total)
else :
   print("No subset with given sum.")
