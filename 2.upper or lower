from random import randint
while True:
    win=0
    computer1 = randint(1,9)
    computer3=0
    print(computer1)
    while True:
        gamer=input("guess the next number is upper or lower(for exit print end)")
        while True:
            computer2=randint(1,9)
            if computer2 != computer1:
                break
        if gamer=='upper' or gamer=='lower':  
            if computer2 < computer1 and gamer=='lower':
                print('correct')
                print(computer2)    
                win+=1
                computer1=computer2
                continue
            elif computer2 > computer1 and gamer=='upper':
                print('correct')
                print(computer2)
                win+=1
                computer1=computer2
                continue
            else:
                print('wrong')
                print('the number is',computer2)
                break
        else:
            print('type lower/upper')
            continue
    print('your score is',win)
    gamer=input('thanks for playing(if you want play again press enter else press enething else)')
    if gamer=='':
        continue
    else:
        break
