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

for i in range(0,len(results)) :
    coefs[i].append(results[i])

for i in range(0, len(coefs)) : 
    for j in range(0,len(coefs[0])) : 
        r = i
        s = i
        coefs = iteration_GJ(coefs, r, s)

solutions = []
for i in range(0, len(coefs)) : 
    solutions.append(coefs[i][-1])


print(solutions)
print(results)
print('************')


