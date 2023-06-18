from random import choice
score=0
while True:
    while True:
        computer=choice(('head','tail'))
        while True:
            player=input('enter head/tail for exit type end')
            if player=='tail' or player=='head' or player=='end':
                break
            else:
                print('please type tail or head')
        if player==computer:
            print('correct')
            score+=1
        else:
            print('wrong')
            print(computer)
        if player=='end':
            break
    print('your score is',score)
    score=0
    player=input('if you dont want play again press end else enter somthing else')
    if player=='end':
        print('thank you for play')
        break

    
