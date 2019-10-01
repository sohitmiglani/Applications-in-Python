# This algorithm is a representation of the Quick Sort algorithm that is a very efficient way to sort lists. 
# It uses a pivot to partition the list so that elements on the left side are smaller than the partition and elements on the right are greater than the partition. 
# It then sorts the rest of the sub lists. 
# By using a quick optimal divide, we can sort lists very efficiently. 

def partition(lis,lower,upper):
    i = lower - 1 
    pivot = lis[upper]
    
    for j in range(lower,upper):
        if lis[j] <= pivot:
            i += 1
            lis[i],lis[j] = lis[j],lis[i]
            
    lis[i+1], lis[upper] = lis[upper],lis[i+1]
    return (i+1)

def quicksort(lis):
    lower = 1 
    upper = len(lis) - 1
    
    if lower < upper: 
        
        index = partition(lis,lower,upper)
        
        quicksort(lis, lower, index - 1 )
        quicksort(lis, index+1, upper)
    
    return lis
