
# coding: utf-8

# In[161]:


def printm(matrix, m, n):
    # function to print a matrix neatly
    print('\n'.join([''.join(['{:4}'.format(i) for i in row]) for row in matrix]))


# In[162]:


def lcs(string1, string2):
    M = len(string1)
    N = len(string2)

    #Build a solution matrix where all entries are initialized to 0. Later this matrix will be filled up.
    #Size of this matrix will be M rows and N columns
    solution_matrix = [[0] * (N + 1) for i in range(M + 1)]

    
    for i in range(M + 1):
        for j in range(N + 1):
            if i == 0 or j == 0:
                solution_matrix[i][j] = 0
            
            #if a character in the 2 strings is same i.e. if a common character is obtained -
            elif string1[i - 1] == string2[j - 1]:
                solution_matrix[i][j] = solution_matrix[i-1][j-1] + 1   #add 1 to the diagonally up value from matrix and insert this value at the position
                
            #if the character is not same
            else:
                #get the values at the left and above this position. Get the max of the 2 and insert it into the matrix
                #left = matrix[i][j-1]   #above = matrix[i-1][j]
                solution_matrix[i][j] = max(solution_matrix[i-1][j], solution_matrix[i][j-1])
        
        print("Iteration: ", i)
        printm(solution_matrix, M, N)
        print()
    
    #Initialize an empty string to store the solution subsequence
    subsequence_length = solution_matrix[M][N]
    solution_subsequence = [""] * (subsequence_length)
    
    #We start building the subsequence backwards, so start from the last row and column
    last_row = M
    last_column = N
    
    #iterate through the 2 strings backwards
    while last_row > 0 and last_column > 0:
        
        #if a character in the 2 strings is same i.e. if a common character is obtained -
        if string1[last_row - 1] == string2[last_column - 1]:
            
            #add the character to the end of the subsequence
            solution_subsequence[subsequence_length - 1] = string1[last_row - 1]
            
            #decrement the row and column to move to previous diagonal position
            last_row = last_row - 1
            last_column = last_column - 1
            
            #decrement the subsequence length to fill the previous position
            subsequence_length = subsequence_length - 1
            
        #if the character is not same, then find the larger of the two and move back in that direction
        elif solution_matrix[last_row - 1][last_column] > solution_matrix[last_row][last_column - 1]:
            #move to previous row
            last_row = last_row - 1
        
        else:
            #move to the previous column
            last_column = last_column - 1
    return solution_matrix[M][N], solution_subsequence


# In[163]:


string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

ans = lcs(string1, string2)
print("Longest common subsequence:", ''.join(ans[1]))
print("Length of the longest common subsequence:", ans[0])

