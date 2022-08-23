def MergeSort(a, start, end):
    if end - start>1:
        mid=(start+end)//2
        MergeSort(a, start, mid)
        MergeSort(a, mid, end)
        Merge(a, start, mid, end)

def Merge(a, start, mid, end):
    left=a[start:mid]
    right=a[mid:end]
    k=start
    i=0
    j=0
    while (start+i<mid and mid+j<end):
        if (left[i] <= right[j]):
            a[k]=left[i]
            i=i+1
        else:
            a[k]=right[j]
            j=j+1
        k=k+1
    if start+i<mid:
        while k<end:
            a[k]=left[i]
            i=i+1
            k=k+1
    else:
        while k<end:
            a[k]=right[j]
            j=j+1
            k=k+1
 
a=input('Enter the list of numbers: ').split()
a=[int(x) for x in a]
MergeSort(a, 0, len(a))
print('Sorted list: ', end='')
print(a)         
