# This is the algorithm for building and working with heaps, which is a tree-based data structure. 
# It allows us to build a heap from a given list, extract certain element, add and remove them. 


def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)

def heap_extract_max(list):
    build_max_heap(list)
    max = list[0]
    list = list[1:]
    build_max_heap(list)
    return max, list

def max_heap_push(list,x):
    list.append(x)
    build_max_heap(list)
    return list

def max_heap_pop(list):
    list.remove(min(list))
    build_max_heap(list)
    return list
