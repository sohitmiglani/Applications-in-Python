# This basic algorithm is python illustrates how to develop population data and calculate confidence intervals. 
# It uses the upper and lower bounds from the confidence intervals to execute significance testing. 
# It also visualizes both the null and the alternative hypothesis. 

get_ipython().magic(u'matplotlib inline')

import numpy as np
import random
import matplotlib.pyplot as plt

def create_unif_pop(n):
    distrib = 1000 * np.random.random_sample((n, ))
    return distrib

def create_norm_pop(n):
    distrib = 1000 * np.random.normal(0,1,(n, ))
    return distrib

def create_skew_pop(n):
    distrib = 1000 * np.random.noncentral_f(3, 10, 3, (n, ))
    return distrib

def graph_distribution(dist, name):
    plt.hist(dist)
    plt.title(name)
    plt.show()

def sample_procedure(dist):
    sample_size = int(raw_input("Enter the sample size:"))
    sample_repeats = int(raw_input("Enter the number of times to repeat the experiment:"))
    sample_means = []
    list_of_standard_errors = []
    confidence_intervals = []
    
    for _ in range(sample_repeats):
        
        sample = np.random.choice(dist, (sample_size, ))
        this_mean = np.mean(sample)
        sample_means.append(this_mean)
        #Question 2 starts here 
        
         # Noting the standard deviation
        standard_dev = np.std(sample)        
        # Calculating the standard error for one sample
        standard_error = standard_dev/(sample_size**0.5)
        # Noting down the standard error for this sample in a list
        list_of_standard_errors.append(standard_error)  
        
        # Calculating the upper and lower bound of a 95% confidence interval
        upper_bound = this_mean + standard_error*1.96   
        lower_bound = this_mean - standard_error*1.96
        
        # Keeping record of the intervals as lists in list.
        confidence_intervals.append([lower_bound,upper_bound])  
            
    a = 0 # A variable to track total samples whose confidence interval contains the mean
    b = 0 # A variable to track the total samples 
    c = np.mean(population)   # The actual population mean
    
    # For every list in this bigger list of confidence intervals,
    # The mean(c) must lie above lower bound(1st element) and below upper bound.
    for e in confidence_intervals:   
        b += 1
        #  If the condition is satisfied, we note it down. This is answer to Question 2(2nd part)
        if c > e[0] and c < e[1]:
            a += 1              
        
    print "The population mean lies in " + str(a) + " confidence intervals out of total " + str(b) + " confidence intervals." 
    
    #Calculating actual value of standard error.
    k = np.std(population)/(population_size**0.5)  
    
    # Calculating our estimate of standard error.
    l = np.mean(list_of_standard_errors) #Answer to Question 2 (part 1)       
    
    print "The population standard error is " + str(k)
    print "The estimate of standard errors from the samples is " + str(l)
     
    print "The error in our estimate of standard errors is " + str( (k-l)/k*100 ) + " %"
    
    lower_bounds = []
    upper_bounds = []
    
    # For each confidence interval that we recorded, we are now separating the values.
    for e in confidence_intervals:   
        lower_bounds.append(e[0])   # Recording all lower bounds
        upper_bounds.append(e[1])   # Recording all upper bounds
        
        s = max(lower_bounds)      # The maximum of the lower bounds
        t = min(upper_bounds)      #The minimum of the upper bounds 
        
        u = min(lower_bounds)      # The minimum of lower bounds 
        v = max(upper_bounds)      # The maximum of upper bounds 
        
    print "The confidence interval with highest lower bound and lowest upper bound is " + str(s) +  "," + str(t)
    print "The confidence interval with lowest lower bound and highest upper bound is " + str(u) +  "," + str(v)
    
    if c>s and c<t:   
        print "The population mean lies in the confidence interval of highest lower bound and lowest upper bound."
    else: 
        print "The population mean doesn't lie in the confidence interval of highest lower bound and lowest upper bound."

    if c>u and c<v:  
        print "The population mean lies in the confidence interval of lowest lower bound and highest upper bound."
    else: 
        print "The population mean doesn't lie in the confidence interval of lowest lower bound and highest upper bound."
        
    print "Here's what the sample mean distribution looks like."
    
    plt.hist(sample_means)
    plt.title('Sample Means')
    plt.show()
    
    print "The mean of the sample means is:", np.mean(sample_means)
    print "The standard deviation of the sample means is:", np.std(sample_means)
    print ""

print "First create a (pseudo)-random population distribution."
population_size = int(raw_input("Enter a population size:"))
print "Now choose an approximate shape."
pop_type = 0
while pop_type < 1 or pop_type > 3:
    pop_type = int(raw_input("Enter 1 for uniform, 2 for normal-like, or 3 for skewed:") )                  

if pop_type == 1:
    population = create_unif_pop(population_size)
    
elif pop_type == 2:                   
    population = create_norm_pop(population_size)
    
elif pop_type == 3:                   
    population = create_skew_pop(population_size)
    
print "Here's what the population distribution looks like."
graph_distribution(population, 'Population Distribution')

print "The population mean is:", np.mean(population) ## look this up

print "For the second step, enter the size of the samples to draw --with replacement-- from the population distribution, and how many times to repeat this procedure in order to create a distribution of sample means."

sample_flag = True

while sample_flag:
    sample_procedure(population)
    print "Perform sampling procedure again? Note that if no, then the population distribution will be lost."
    decision = raw_input("Type y or n:")
    if decision == 'n':
        sample_flag = False
    else:
        print "Doing procedure again."
        

