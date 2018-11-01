
# coding: utf-8

# Program to show the Randomized Algorithm technique of a hiring a candidate from a  list of candidates. the program computes the cost of interviewing n candidates and hiring one of them.
# 
# Constraints/Assumptions:
# 1. Hiring a candidate would take 1 unit time
# 2. Each interview would take 1 unit time

# In[12]:


def hire(candidate_list):
    '''
    Function to calculate the hiring cost of a hiring a candidate from a list of candidates using randomized algorithm technique
    input : an integer list of candidates
    output : total cost of interviewing the candidates and hiring one of them
    '''
    #creating and initializing variables to denote hiring cost and interviewing cost. 
    interview_cost = 0
    hiring_cost = 0

    #let us use a dummy candidate 0 and assume that he.she is the best at the start of the hiring process
    best_c = 0
    
    for candidate in candidate_list:
        # increment interviewing cost by 1 each time a new candidate is interviewed
        interview_cost = interview_cost + 1
        
        if candidate > best_c:
            best_c = candidate         #change the best candidate everytime the above condition is satisfied
           
            hiring_cost = hiring_cost + 1   #increment hiring cost by 1 each time we get a candidate who is better than the previous best candidate
            
    total_cost = interview_cost + hiring_cost  #compute the total cost of hiring 1 candidate after interviewing the candidates and choosing amongst them
   
    return total_cost


# In[13]:


import random

n = int(input("Enter the number of candidates you want to hire from "))

#creating a list of candidates where each candidate is idetified by his/her number. list[1] meand candidate 1 and so on
candidate_list = list(range(1, n+1))

#shuffling the candidates to remove the order
random.shuffle(candidate_list)

#call the hire function and get the cost of hiring a candidate from above list
cost = hire(candidate_list)
print("The cost of hiring a candidate is : " ,cost)

