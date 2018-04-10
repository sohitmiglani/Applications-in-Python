# This is a representation of the insertion sort algorithm that works on the principle of building a final sorted list, by picking elements one by one.
#  We're also timing the algorithm so that we can compare it's time efficiency with other sorting algorithms. 

import time
start = time.clock()
def insertion_sort(list):
    
    for i in range(1,len(list)):
        key = list[i]
        j = i-1 
        while j>=0 and key < list[j]:
            list[j+1] = list[j]
            j -=1 
        list[j+1] = key
    
    
    return list
end = time.clock()
print "Time Taken: " + str(end-start)
lis = range(1,101)[::-1]

insertion_sort(lis)
