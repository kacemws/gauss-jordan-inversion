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


def iteration_GJ_UP (A,I, r, s): 
    pivot = A[r][s]
    for j in range(0,len(A[0])) : 
        A[r][j] = A[r][j] / pivot
        I[r][j] = I[r][j] / pivot
    for i in range(0, len(A)) : 
        if i != r : 
            Ais = A[i][s]
            for j in range(0,len(A[0])) : 
                A[i][j] = A[i][j] - Ais * A[r][j]
                I[i][j] = I[i][j] - Ais * I[r][j]
    return A,I

ID = np.identity(len(A)).tolist()
for i in range(0, len(A)) : 
    for j in range(0,len(A[0])) : 
        if A[i][j] != 0 :
            r = i
            s = j
            A,ID= iteration_GJ_UP(A, ID, r, s)
            break


print("matrice : ",A)
print('************')
print("inverse using GJ : ",ID)
print('************')
print("inverse using numpy : ",np.linalg.inv(np.array(old_a)))


