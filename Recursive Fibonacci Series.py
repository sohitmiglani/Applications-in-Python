# This is a recursive function to calculate the value of a particular element in the Fibonacci Series. 
# It is the most basic way of implementing Fibonacci series, and takes a lot of time to implement. 
# More time efficient ways of implementing Fibonacci series is through dynamic programming. 

import time
def fib(n): 
    if n <= 0: 
        return 0 
    if n == 1: 
        return 1
    else:
        return fib(n-1) + fib(n-2)

start = time.clock()
fib(100)
end = time.clock()
print str(end - start)
