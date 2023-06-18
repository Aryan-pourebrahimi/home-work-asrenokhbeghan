from random import randint
score1=0
score2=0
gamer1=0
gamer2=0
n=0
for i in range(1,8):  
    gamer2=0
    gamer1=0
    guess1=int(input("player1 enter your guess:"))
    guess2=int(input("player2 enter your guess:"))
    print('lets start round',i)
    n=0
    while n<=4:
        while True:
            player1=input('player1 please press enter to roll a dice')
            if player1=='':
                dice1=randint(1,6)
                print(dice1)
                if dice1==6:
                    print('you win another dice')
                    n-=1
                break
        gamer1+=dice1
        n+=1
    n=0
    while n<=4:
        while True:
            player2=input('player2 please press enter to roll a dice')
            if player2=='':
                dice2=randint(1,6)
                print(dice2)
                if dice2==6:
                    print('you win another dice')
                    n-=1
                break   
        gamer2+=dice2
        n+=1
    if guess1 <= gamer1:
        score1+=guess1*5+(gamer1-guess1)
    if guess2 <= gamer2:
        score2+=guess2*5+(gamer2-guess2)
    print('player1 score in this round',gamer1)
    print('player2 score in this round',gamer2)
    print('player1 score until this round',score1)
    print('player2 score until this round',score2)
if score2 > score1:
    print('score player1:',score1,'\n','score player2:',score2)
    print('player2 win','\n','thanks for playing')
if score2 < score1:
    print('score player1:',score1,'\n','score player2:',score2)
    print('player1 win','\n','thanks for playing')    
