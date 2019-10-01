#This simple algorithm codes for a population distribution and conducts significant testing but with a correction for Type A errors. 
#It uses the concept of Bonferroni corrections to change the confidence interval. 
# It also calculates the correction in the error after the bonferroni adjustment. 

get_ipython().magic(u'matplotlib inline')

import numpy as np
import random
import matplotlib.pyplot as plt

import scipy.stats as st

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

print "First create a (pseudo)-random population distribution."
population_size = int(raw_input("Enter a population size:"))
print "Now choose an approximate shape."
pop_type = 0
while pop_type < 1 or pop_type > 3:
    pop_type = int(raw_input("Enter 1 for uniform, 2 for normal-like, or 3 for skewed:") )                  

if pop_type == 1:    # Working with any type of population. This is the answer to Optional Challenge number 2.  
    population = create_unif_pop(population_size)
elif pop_type == 2:                   
    population = create_norm_pop(population_size)
elif pop_type == 3:                   
    population = create_skew_pop(population_size)

print "Here's what the population distribution looks like."
graph_distribution(population, 'Population Distribution')

print "The population mean is:", np.mean(population)

sample_flag = True

# This function takes in input for the number of tests we want to do. 

x= int(raw_input("Please enter the number of hypothesis tests you want to conduct."))

# This new_alpha is the alpha with the bonferroni correction. Also called alpha_star. 
# The reason new_alpha = 0.0001 for 50 or more tests is because 0.0001 is the least value it should take.
# When alpha_star = 0.0001, every hypothesis having p-value below 0.0001 becomes significant, we don't need to go further.
# Thus, alpha_star can take the lowest value of 0.0001 even though the number of tests >50. 

if x>=50:
    new_alpha = 0.0001 
if x<50:
    new_alpha = 0.05/x              # Taking input of any 'X" also meets the optional challenge number 1. 

# This number "X" is the number of hypothesis tests we'll do. 

population_mean = np.mean(population)   # Calculating the mean from the population distribution

observations = []  # An empty set to collect out point estimates. 
        
a= 0 

# The function will basically generate "X' number of values from the sample population such that they lie in the sample. 
# We'll perform the hypothesis test on each one of them. 

while a<x:     
    y= random.choice(population)
    observations.append(y)
    a += 1
        
standard_deviation = np.std(population)  # Calculating the standard deviation of the population. 
standard_error = standard_deviation/(population_size**0.5)   # Calculating the standard error in the population. 

new_rejections = 0   # This is the amount of null hypothesis rejections while using bonferroni corrected alpha. 
rejections = 0       # This is the amount of null hypothesis rejections while using alpha of 0.05. 

for e in observations:
    
    z_score = (e - population_mean)/standard_deviation   # Calculating Z-Score of each observation
    
    area = st.norm.cdf(z_score)  # Calculating the area from the other tail to the observation
    
    if area>0.5:   # If the observation lies on right side, then we must subtract it from total area to get p-value
        p_value = 1 - area 
    else:          # Otherwise, it is itself the p-value
        p_value = area
    
    if p_value <0.05:  #If it is less than the normal alpha, we will add +1 to rejections to note it down.  
        rejections+=1
        
    if p_value <new_alpha: # If it is less than the new corrected alpha, we will add +1 to the new rejections.
        new_rejections += 1
    
print "With an alpha of 0.05 and " + str(x) + " number of tests, we rejected " + str(rejections) + " number of null hypothesis."
print "While, with a bonferroni corrected alpha of " + str(new_alpha) + ", We rejected " + str(new_rejections) + " number of null hypothesis."

if new_rejections !=0 and rejections !=0:   # If any rejection is not 0, we can calculate the amount of error in the sample. 
    print "So, the amount of error without bonferroni correction is " + str((new_rejections - rejections)*100/new_rejections) + " %"

# This calculates the mathematical error for "X" number of hypothesis test with normal alpha of 0.05. 
print "Mathematically, the amount of Type 1 error without bonferroni correction is " + str((1 - 0.95**(x))*100) + " %"

# This calculates the mathematical error for "X" number of hypothesis test with new alpha of 0.05/X. 
print "Mathematically, the amount of Type 1 error with bonferroni correction is " + str((1 - (1-new_alpha)**(x))*100) +" %"
        


# In[ ]:



