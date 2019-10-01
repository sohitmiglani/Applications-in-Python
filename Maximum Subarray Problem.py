# This is a representation of solving the Max-Sub Array problem through 4 different techniques. 
# A subarray is essentially a part of the subarray that has the maximum sum. 
# It is usually helpful in optimizing investments by looking at trade patterns. 
# It's not a greedy algorithm so it accomodates 'negative edges'. 

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_subarray_bruteforce(A):
	max=A[0]
	for i in range(len(A)):			#length of sum
		for j in range(len(A)-i):	#for loop
			subMax=0
			for k in range(i):		#calculate sum
				subMax+=A[j+k]
			if subMax>max: max=subMax
	return max

def incremental_max_subarray(A,mA):
	max_withend=A[0]
	for x in A[1:]:
		max_withend=max(x,max_withend+x)
	return max(max_withend,mA)

def recursive_mx_subarray(A):
    if len(A) == 1:
        return A[0], A[0]
    prev_mx_subarray, prev_mx_endarray = recursive_mx_subarray(A[:-1])
    mx_endarray=max(prev_mx_endarray + A[-1], A[-1])
    mx_subarray=max(mx_endarray,prev_mx_subarray)
    return mx_subarray, mx_endarray
    
def mx_subarray(A):
    (x,_) = recursive_mx_subarray(A)
    return x

print max_subarray_bruteforce([2,-4,8,-8,-2,-2])
print max_subarray([2,-4,8,-8,-2,-2,7])
print incremental_max_subarray([2,-4,8,-8,-2,-2,7,9],max_subarray([2,-4,8,-8,-2,-2,7]))
print mx_subarray([2,-4,8,-8,-2,-2,7])
