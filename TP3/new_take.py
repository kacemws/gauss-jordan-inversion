import copy
from print_helper import print2D




inferior_borne = 0
decision_vars = []

### the backpack object
class backpack_object:
    def __init__(self, weight, utility):
        self.weight = weight
        self.utility = utility
 
    def __repr__(self):
        return '{' + str(self.weight) + ', ' + str(self.utility) + '}'

### 4
class node : 
    # the fixed vars are the one provided by the previous node
    # the decision vars are the one computed in this node
    # left is the left kid
    # right is the right kid
    def __init__(self,fixed_vars):
        self.fixed_vars = fixed_vars
        self.decision_vars = []
        self.z = None
        self.left = None
        self.right = None
    
    ### 3-a 
    def evaluate(self) :
        decision_vars = []
        left_weight = max_weight
        z = 0

        for i in range(len(backpack_objects)): 
            try : 
                if self.fixed_vars[i] == 1 : 
                    if backpack_objects[i].weight > left_weight : 
                        return
                    left_weight -= backpack_objects[i].weight
                    z +=  backpack_objects[i].utility
                decision_vars.append(self.fixed_vars[i])
            except :
                break            


        for object in backpack_objects[len(self.fixed_vars):] : 
            if object.weight <= left_weight : 
                decision_vars.append(1)
                left_weight -= object.weight
                z +=  object.utility
            
            else :
                decision_vars.append(0)
        self.decision_vars = decision_vars
        self.z = z

    ### 3b
    def separate(self) : 
        
        # if there are still more decision variables, go deeper
        if len(self.fixed_vars) != len(self.decision_vars) : 
            
            # the fixed vars to provide to the children nodes, 
            left_vars  = copy.deepcopy(self.fixed_vars)
            right_vars = copy.deepcopy(self.fixed_vars)

            left_vars.append(1)
            right_vars.append(0)

            # the left and right descendant nodes
            self.left = node(left_vars)
            self.right = node(right_vars)
        else : 
            pass
        
    def execute(self) : 
        self.evaluate()
        if self.z is None : 
            return
        if self.z >= inferior_borne : 
            update_borne(self.z, self.decision_vars)
            
        self.separate()
        if self.left is not None : 
            self.left.execute()
        if self.right is not None : 
            self.right.execute()
        
    def __repr__(self):
        left_part = ""
        right_part = ""
        if self.left is not None : 
            left_part = self.left
        if self.right is not None : 
            right_part = self.right

        return '\n{' + str(self.z) + ', ' + str(self.decision_vars) + '}\n left : '+str(left_part)+'\n right : '+str(right_part)


### 1
def sorting (backpack_objects) : 
    backpack_objects.sort(key=lambda x:(x.utility/x.weight), reverse=True)

### 2 
def initial_solution(backback_objects) : 
    decision_vars = []
    left_weight = max_weight
    z = 0

    for object in backback_objects : 
        if object.weight <= left_weight : 
            decision_vars.append(1)
            left_weight = left_weight - object.weight
            z += object.utility
        else :
            decision_vars.append(left_weight / object.weight)
            z+= object.utility * (left_weight / object.weight)
            left_weight = 0
        # fi blasst mandir append 0, rani ndir append te3 dek float, kima 1/2 f cahier te3ek
    return decision_vars, z




def update_borne(z, vars) : 
    global inferior_borne
    global decision_vars

    inferior_borne = z
    
    decision_vars = vars

def filter_fixed(value):
    return value == 1


backpack_objects = []

max_weight = 0


def main():

    ### params : 
    global decision_vars
    global z 
    global backpack_objects 
    global max_weight 

    typing = True

    while typing : 
        # size = input("\nSaisir le nombre d'objets : ") 
        try : 
            # size = int(size)
            # for i in range(size) : 
            #     weight = int(input(f"\nSaisir le poids de l'objet {i+1} : ")) 

            #     utility = int(input(f"\nSaisir l'utilit?? de l'objet {i+1} : ")) 

            #     backpack_objects.append(backpack_object(weight,utility))
            
            # print(backpack_objects)



            # max_weight = int(input("\nSaisir le poids maximale : "))



            backpack_objects = [
                backpack_object(3,15),
                backpack_object(4,18),
                backpack_object(1,3),
                backpack_object(3,7),
                backpack_object(1,2),
                backpack_object(1,1),
            ]
            max_weight = 5



            sorting(backpack_objects)
            decision_vars,z = initial_solution(backpack_objects)

            print(decision_vars,z)

            update_borne(z,decision_vars)

            root_node = node([None,None,None,None,None,None])

            ### 5
            root_node.execute()

            print('\nthe solution for P is : ', inferior_borne)
            print("\nwith the decisions vars as : ", decision_vars)

            # # print(root_node)
            # print2D(root_node)
            typing =False
        except : 
            print("\nVeuillez saisir un nombre entier\n")
            pass


main()