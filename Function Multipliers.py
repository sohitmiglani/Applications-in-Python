# The first function demonstrates a function multiplier that essentially customizes a function with a veriable 'm' and runs it 'n' times. 
# Such functions are helpful to understand how to customize and reiterate over functions, especially functions with randomized answers. 
# An example of a function has been given.  This example function creates a list of m random integers between -1000 and 10000. 

def function_multiplier(function,m,n):
    list = []
    list.append(function(m))
    for i in range(1,n):
        list.append(function((2*i)*m))
    return list 

from random import randint

def rand_list(m):
    lis =[]
    for _ in xrange(m):
        lis.append(randint(-1000,1000))
    return lis

function_multiplier(rand_list,1,4)
