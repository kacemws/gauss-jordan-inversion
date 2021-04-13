import numpy as np
import heapq



def column(A, j):
   return [row[j] for row in A]

def transpose(A):
   return [column(A, j) for j in range(len(A[0]))]

def isPivotCol(col):
   return (len([c for c in col if c == 0]) == len(col) - 1) and sum(col) == 1

def variableValueForPivotColumn(tableau, column):
   pivotRow = [i for (i, x) in enumerate(column) if x == 1][0]
   return tableau[pivotRow][-1]

# assume the last m columns of A are the slack variables; the initial basis is
# the set of slack variables
def initialTableau(c, A, b):
   tableau = [row[:] + [x] for row, x in zip(A, b)]
   tableau.append([ci for ci in c] + [0])
   return tableau


def primalSolution(tableau):
   # the pivot columns denote which variables are used
   columns = transpose(tableau)
   indices = [j for j, col in enumerate(columns[:-1]) if isPivotCol(col)]
   return [(colIndex, variableValueForPivotColumn(tableau, columns[colIndex]))
            for colIndex in indices]


def objectiveValue(tableau):
   return -(tableau[-1][-1])


def canImprove(tableau):
   lastRow = tableau[-1]
   return any(x > 0 for x in lastRow[:-1])


# this can be slightly faster
def moreThanOneMin(L):
   if len(L) <= 1:
      return False

   x,y = heapq.nsmallest(2, L, key=lambda x: x[1])
   return x == y


def findPivotIndex(tableau):
   column_choices = [(i,x) for (i,x) in enumerate(tableau[-1][:-1]) if x > 0]
   column = max(column_choices, key=lambda a: a[1])[0]

   # check if unbounded
   if all(row[column] <= 0 for row in tableau):
      raise Exception('Linear program is unbounded.')

   # check for degeneracy: more than one minimizer of the quotient
   quotients = [(i, r[-1] / r[column])
      for i,r in enumerate(tableau[:-1]) if r[column] > 0]

   if moreThanOneMin(quotients):
      raise Exception('Linear program is degenerate.')

   # pick row index minimizing the quotient
   row = min(quotients, key=lambda x: x[1])[0]

   return row, column

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

def simplex(c, A, b):
   tableau = initialTableau(c, A, b)
   print("Initial tableau:")
   for row in tableau:
      print(row)

   while canImprove(tableau):
      i,j = findPivotIndex(tableau)
      print("Next pivot index is=%d,%d \n",i,j)
      tableau = iteration_GJ(tableau,i,j)
      
      print("Tableau after pivot:")
      for row in tableau:
         print(row)
      print()

   return tableau, primalSolution(tableau), objectiveValue(tableau)


if __name__ == "__main__":
    c = [600, 400]
    A = [[1, 2], [1, 1],[3, 1]]
    b = [700, 400, 900]
    ID = np.identity(len(A)).tolist()
    for i in range(0,len(ID)) :
        for j in range(0,len(ID[i])) : 
            A[i].append(ID[i][j])
   # add slack variables by hand   
    for i in range(0, len(b)+1) :
        c.append(0)

    t, s, v = simplex(c, A, b)
    print('***********')
    print(s)
    print(v)