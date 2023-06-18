from random import randint
while True:
    computer=randint(1,10000)
    score=100
    while True:
        try:
            player=int(input('enter your guess:'))
            if player > computer:
                print('try lower ;)')
                score-=1
                continue
            elif player < computer:
                score-=1
                print('try upper ;)')
                continue
            elif player==computer:
                print('thats correct :)')
                break
        except:
            continue
    print('your score is',score)
    player=input('if you want exit type end else press enything else')
    if player=='end':
        break
print('thank you for playing :)')
        
