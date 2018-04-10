# This is a representation of a recursive merge sort algorithm that works on the principle of divide and conquer. 
# It recursively divdes lists into sub lists that can be sorted easily. 
# It then merges the sorted stand-alone sublists together. 

def merge_sort(arr,L,R):
    
    n1 = len(L)
    n2 = len(R) 
        
    i = 0     
    j = 0     
    k = 0     
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def final_merge(lis):
    n = len(lis)
    if n<2:
        return
        
    cut = int(len(lis)/2)
    
    L = []
    R = []
    
    for i in range(0,cut):
        L.append(lis[i])
    for j in range(cut,len(lis)):
        R.append(lis[j])
    
    print L 
    print R
    final_merge(L)
    final_merge(R)
    merge_sort(lis,L,R)
    return lis
