# This algorithm is a representation of the hiring problem wherein a company is trying to optimize it's HR resources by hiring an assistant intelligently. 
# It needs to hire the best candidate (which comes in a randomly ordered list of candidates) while optimizing over hiring costs. 
# It also graphs the variation of funds spent in hiring candidates, as compared to the number of candidates. 

import numpy as np
import random
import matplotlib.pyplot as plt

def hiring_problem(n):
    hires = 0
    best= 0
    candidates = np.random.uniform(0,1,size=n)
    for i in range(0,n):
        if candidates[i]>best:
            hires+= 1
            best = candidates[i]
    return hires 

def hiring_problem_graph(max_n):
    hire_averages = []
    for i in range(1,max_n+1):
        hires = []
        for b in range(1000):
            hires.append(hiring_problem(i))
        hire_averages.append(np.mean(hires))
    
    x=range(1,max_n+1) #generates x-axis
    plt.plot(x, hire_averages) # Plots all the averages 
    plt.title("Average number of hires Vs. Number of candidates")
    plt.xlabel("Number of candidates")
    plt.ylabel("Number of Hires")
    plt.show()
