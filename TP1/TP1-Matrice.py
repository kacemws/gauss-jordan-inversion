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


ID = np.identity(len(A)).tolist()
for i in range(0,len(ID)) :
    for j in range(0,len(ID[i])) : 
        A[i].append(ID[i][j])

for i in range(0, len(A)) : 
        r = i
        s = i
        A= iteration_GJ(A, r, s)

for i in range(0, len(A)) : 
    # A[i] = A[i][]
    A[i] = A[i][-len(old_a):]


print("matrice : ",A)
# print('************')
# print("inverse using GJ : ",ID)
print('************')
print("inverse using numpy : ",np.linalg.inv(np.array(old_a)))


