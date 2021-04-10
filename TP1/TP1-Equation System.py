import numpy as np
import copy




old_coefs = [[2,1,4],[3,2,1],[1,3,3]]
old_results = [16,10,16]

coefs = copy.deepcopy(old_coefs)
results = copy.deepcopy(old_results)


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

def iteration_GJ_solutions (A,Res, r, s): 
    pivot = A[r][s]
    Res[r] = Res[r] / pivot
    for j in range(0,len(A[0])) : 
        A[r][j] = A[r][j] / pivot
    for i in range(0, len(A)) : 
        if i != r : 
            Ais = A[i][s]
            Res[i] = Res[i] - Ais * Res[r]
            for j in range(0,len(A[0])) : 
                A[i][j] = A[i][j] - Ais * A[r][j]
    return A,Res

for i in range(0, len(coefs)) : 
    for j in range(0,len(coefs[0])) : 
        if coefs[i][j] != 0 :
            r = i
            s = j
            coefs, results = iteration_GJ_solutions(coefs,results, r, s)
            break


print(coefs)
print(results)
print('************')


