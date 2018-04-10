# This algorithm is a representation of the worst sort algorithm. 
# It helps us understand how little details and extra operations can make our code very inefficient. 


def median(x1, x2, x3):
    for a in range(7):
        if x1 <= x2 <= x3:
            return x2
     
        (x1, x2, x3) = (x2, x1, x3)
        if a % 2:
            (x1, x2, x3) = (x3, x1, x2)

def worst_sort(list): 
   x = true    # x is true when list is not sorted
   counter = 0 
   while x: # a loop to shuffle the list and then check whether the list is sorted
      b = True  
      new = random.shuffle(a)   # Sampling a list of the same length from the list 
      for i in range(1,len(a)): # Check whether it's sorted or not 
         b = b and new[i] > new [i-1] 
      x = not b 
      counter +=1 
   return new,counter
