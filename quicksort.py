def QuickSort(a,l,h):
    if h-l > 1:
        p=partition(a,l,h)
        QuickSort(a,l,p)
        QuickSort(a,p+1,h)
def Interchange(a,i,j):
    a[i],a[j]=a[j],a[i]
def partition(a,l,h):
    m=a[l]
    i=l+1
    j=h-1
    while True:
        while (i <= j and a[i] <= m):
            i=i+1
        while (i <= j and a[j] >= m):
            j=j-1
        if i <= j:
            Interchange(a,i,j)
        else:
            Interchange(a,l,j)
            return j
a=list(map(int,input("Enter list:").split()))
QuickSort(a,0,len(a))
print('Sorted list: ',a)
