import numpy as np
import copy



old_a = [[2,-1,0],[-1,2,-1],[0,-1,2]]
# old_b = [[1,2],[3,1]]

A = copy.deepcopy(old_a)
# B = copy.deepcopy(old_b)

def iteration_GJ (A, r, s): 
    pivot = A[r][s]
    for j in range(0,len(A[0])) : 
        A[r][j] = A[r][j] / pivot
    for i in range(0, len(A)) : 
        if i != r : 
            Ais = A[i][s]
            for j in range(0,len(A[0])) : 
                A[i][j] = A[i][j] - Ais * A[r][j]
    return A

           
for i in range(0, len(A)) : 
    for j in range(0,len(A[0])) : 
        if A[i][j] != 0 :
            r = i
            s = j
            A = iteration_GJ(A, r, s)
            break


print(A)
print('************')
print(np.linalg.inv(np.array(old_a)))


