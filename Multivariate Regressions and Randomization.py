# This algorithm creates a random multivariate regression of the variation of the students IQ with SAT and GPA Scores. 
# It constructs the IQ of students by constructing a linear equation, IQ = GPA + SAT/600 + random error. 

# The logic behind choosing the coefficients of GPA and SAT is to bring them to the same level of range. 
# If their range differs, then one will tend to dominate over the other. 

# We run independant regressions of IQ over SAT and GPA to check how their variation differs. 
# These variations will tend to be similar if the range of GPA and SAT/600 match (which they do). 
# On changing the coefficients, one coefficient will dominate over the other. 

# This helps us understand how coefficients affect the multivariate regression, and how randomization plays it's part. 

import numpy as np
import random
import matplotlib.pyplot as plt

errors = np.random.normal(0,1,200)

def create_random_pop(scale):  # This creates a random population by chooding random numbers and adding them to the list. 
    set_1 = []
    a = 0 
    while a < 200:
        b = scale*random.random() #This line outputs one random number from 1 to 100. 
        set_1.append(b)  # we add it to the thresholds set. We do this 500 times. 
        a +=1
    return set_1

# Brute force method of linear regression

GPA = create_random_pop(4) 
SAT = create_random_pop(2400)

b = 0 
IQ = []

while b<200: 
    IQ.append((GPA[b]) + (SAT[b])/600 + (errors[b]))
    b = b + 1

m, b = np.polyfit(GPA, IQ, 1)
m2,b2 = np.polyfit(SAT, IQ, 1)
IQ_fitted_GPA = []
IQ_fitted_SAT = []

c = 0
while c<200: 
    IQ_fitted_GPA.append(m*GPA[c] + b)
    IQ_fitted_SAT.append(m2*SAT[c] + b2)
    c = c + 1

    
plt.scatter(GPA, IQ, s=2)
plt.plot(GPA,IQ_fitted_GPA, '-')
plt.xlabel("GPA of Students")
plt.ylabel("IQ of Students")
plt.title("Variation of IQ with the GPA of Students")
plt.show()

plt.scatter(SAT, IQ, s=2)
plt.plot(SAT,IQ_fitted_SAT, '-')
plt.xlabel("SAT Scores of Students")
plt.ylabel("IQ of Students")
plt.title("Variation of IQ with the SAT Scores of Students")
plt.show()

