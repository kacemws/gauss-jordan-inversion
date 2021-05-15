

class backpack_object:
 
    def __init__(self, weight, utility):
        self.weight = weight
        self.utility = utility
 
    def __repr__(self):
        return '{' + str(self.weight) + ', ' + str(self.utility) + '}'

backpack_objects = [
    backpack_object(6,12),
    backpack_object(3,8),
    backpack_object(9,20),
    backpack_object(5,9),
    backpack_object(3,6),
    backpack_object(7,16),
]

max_weight = 17


### 1st question
def sorting (backpack_objects) : 
    backpack_objects.sort(key=lambda x:(x.utility/x.weight), reverse=True)


### 2nd question
def initial_solution(backback_objects) : 
    decision_vars = []
    left_weight = max_weight

    for object in backback_objects : 
        if object.weight <= left_weight : 
            decision_vars.append(1)
            left_weight = left_weight - object.weight
        else :
            decision_vars.append(0)
    return decision_vars, left_weight

sorting(backpack_objects)
decision_vars, z = initial_solution(backpack_objects)

print(decision_vars)
z = max_weight - z
print(z)
