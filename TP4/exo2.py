import numpy as np
def vecteurStochastique (vector) : 
        if sum(vector) == 1 : 
            return True
        return False

def matriceStochastique(matrice) : 
    for vector in (matrice) : 
        if not vecteurStochastique(vector) : 
            return False
    return True

def matrice_puissance(list, puissance) : 
    matrice = np.matrix(np.array(list))
    return matrice**puissance

matrice_test = [
    [0,0.5,0.5,0], 
    [0.6,0,0.4,0],
    [0,0.2,0.8,0], 
    [0,0,1,0],
]


print(
    matriceStochastique(
        matrice_test
    )
)

print(matrice_puissance(matrice_test,4))
