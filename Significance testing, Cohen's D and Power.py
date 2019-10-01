# This algorithm performs significant testing by using Z-Scores and the area under the curve of the null hypothesis distribution. 
# It also calculates the power and the Cohen's-D for that particular test.

import scipy.stats as st

def significance(alpha, mean1, mean2, sd1, sd2, size1, size2):
    diff_in_means = mean2 - mean1 # We calculate the difference in means 
    
    print "The difference in means is " + str(diff_in_means)
    
    standard_error = ((sd1**2)/size1 + (sd2**2)/size2)**0.5
    print "The Standard error is " + str(standard_error)
       
    # We calculate the Z-Score for the difference in the means. 
    # I have mentioned "0" here as well because it is the null hypothesis. 
    # The null hypothesis is difference in means = 0, so it lies at the centre
    z_score = ( diff_in_means) / standard_error
    
    # This function gives me the area from the other(left) side of the graph to the point 
    area = st.norm.cdf(z_score)
   
    if area>0.5:# If it lies on right side, then we must subtract it from total area to get p-value
        p_value = 1 - area 
    else:          # Otherwise, it is itself the p-value
        p_value = area
    
    print "The p-value for the difference in the means is " + str(p_value)
    if p_value <alpha:   # Now, if p-value is less than alpha, then the result is significant. 
        print "There is a statistically significant difference"
    
    if p_value >alpha:   # If p-value is greater than alpha, the result is not significant. 
        print "The difference in the means is not statistically significant."
     
    pooled_standard_deviation = (((size1-1)*(sd1**2) + (size2-1)*(sd2**2))/(size1 + size2 - 2))**0.5
    #Calculating Cohen's D through the formula. 
    cohen_d = diff_in_means/pooled_standard_deviation
    
    print "The Effect Size or Cohen's d is " + str(cohen_d)
    
    if abs(cohen_d) <0.2:
        print "The results are not very practically significant."
    elif abs(cohen_d) > 0.2 and abs(cohen_d) <= 0.5:
        print "The results are somewhat practically significant."
    elif abs(cohen_d) > 0.5 and abs(cohen_d) <= 0.8:
        print "The results are quite practically significant."
    elif abs(cohen_d) > 0.8:
        print "The results are very practically significant."
    
    upper_bound = 0 + standard_error*1.96   # Calculating upper bound of Confidence interval
    #Calculating The Z-Score of the upper bound relative to the alternative distribution. 
    relative_z_score = (upper_bound - diff_in_means)/standard_error
    #Calculating it's area from the left tail. 
    area = st.norm.cdf(relative_z_score)
    #Power is the area from the right tail, so we subtract it from total area
    power = 1 - area
    print "The power of the experiment is " + str(power*100) + " %"
    print "Thus, there is a " + str(power*100) + " % chance that we'll reject the null hypothesis correctly and accept the alternative hypothesis correctly."

