import random as r

# first question : simple throw
def throw_dice () : 
    return r.randint(1,6)

# second question : throw n times
def throw_dice_times(n) : 
    throws = []
    for time in range(n) : 
        throw = throw_dice()
        throws.append(throw)
    return throws

# third question : count how many 6 did we got in n number of throws
def count_six(throws) : 
    return throws.count(6)



# fourth question : 
def random_exp () : 
    throws = 0

    while True : 
        throw = throw_dice()
        if throw == 6 : 
            throws+=1
            break
    
    print('on a obtenu un 6 après ' + str(throws) + ' tentatives')




def main () : 
    running = True

    while(running) : 

        question = 0
        while question not in [1,2,3] : 
            print("\nPour un simple lancer, choisir 1.\nPour multiple lancer, choisir 2.\nPour Une expérience aléatoire, choisir 3.\n")
            try : 
                question = int(input())
                if  question not in [1,2,3] : 
                    raise Exception('invalid choice')
            except : 
                print('Choix invalide\n')
                question = 0
        

        if question == 1 : 
            print("\n")
            print(throw_dice())
        elif question == 2 : 
            try :
                times = int(input('\nCombien de fois voulez-vous lancer le dé ? '))
            except : 
                times = 1

            throws = throw_dice_times(times)
            print(throws)

            print("\nnombre de fois où on obtient le nombre 6 : ",count_six(throws))
        
        else : 
            random_exp()

        print('\nRéesayer ? [O/N]')
        x = input()
        running = x in ['o','O']




main()