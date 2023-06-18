from random import randint
while True:
     gamer1=1
     gamer2=1
     print('player1 is a')
     print('player2 is b')
     while True:
          for i in range(0,10):
               for j in range(i*10+1,(i+1)*10+1):
                    if gamer1==j and gamer2==j:
                         j='ab'
                    elif gamer1==j:
                         j='a'
                    elif gamer2==j:
                         j='b'
                    print('{:^3}'.format(j),end=" ")
               print()
          if gamer1==100:
              print('player1 win')
              break
          if gamer2==100:
              print('player2 win')
              break
          while True:
              player1=input('player1 press enter to roll a dice')
              if player1=='':
                  break
         
          dice1=randint(1,6)
          print('dice1 is',dice1)
          while True:
              player2=input('player2 press enter to roll a dice')
              if player2=='':
                  break
          dice2=randint(1,6)
          print('dice2 is',dice2)
          i=gamer1 + dice1
          j=gamer2 + dice2
          if i >100:
              gamer1-=dice1
          if j >100:
              gamer2-=dice2
          
          gamer1+=dice1
          gamer2+=dice2
          if gamer1==4:
              gamer1=14
              print('player1 ladder ;)')
          if gamer1==9:
              gamer1=31
              print('player1 ladder ;)')
          if gamer1==20:
              gamer1=38
              print('player1 ladder ;)')
          if gamer1==28:
              gamer1=84
              print('player1 ladder ;)')
          if gamer1==40:
              gamer1=59
              print('player1 ladder ;)')
          if gamer1==51:
              gamer1=67
              print('player1 ladder ;)')
          if gamer1==63:
              gamer1=81
              print('player1 ladder ;)')
          if gamer1==71:
              gamer1=91
              print('player1 ladder ;)')
          if gamer2==4:
              gamer2=14
              print('player2 ladder ;)')
          if gamer2==9:
              gamer2=31
              print('player2 ladder ;)')
          if gamer2==20:
              gamer2=38
              print('player2 ladder ;)')
          if gamer2==28:
              gamer2=84
              print('player2 ladder ;)')
          if gamer2==40:
              gamer2=59
              print('player2 ladder ;)')
          if gamer2==51:
              gamer2=67
              print('player2 ladder ;)')
          if gamer2==63:
              gamer2=81
              print('player2 ladder ;)')
          if gamer2==71:
              gamer2=91
              print('player2 ladder ;)')
          if gamer1==17:
              gamer1=7
              print('playe1 snake :(')
          if gamer1==54:
              gamer1=34
              print('playe1 snake :(')
          if gamer1==87:
              gamer1=24
              print('playe1 snake :(')
          if gamer1==62:
              gamer1=19
              print('playe1 snake :(')
          if gamer1==64:
              gamer1=60
              print('playe1 snake :(')
          if gamer1==93:
              gamer1=73
              print('playe1 snake :(')
          if gamer1==95:
              print('playe1 snake :(')
              gamer1=75
          if gamer1==99:
              print('playe1 snake :(')
              gamer1=78
          if gamer2==17:
              gamer2=7
              print('playe2 snake :(')
          if gamer2==54:
              gamer2=34
              print('playe2 snake :(')
          if gamer2==87:
              gamer2=24
              print('playe2 snake :(')
          if gamer2==62:
              gamer2=19
              print('playe2 snake :(')
          if gamer2==64:
              gamer2=60
              print('playe2 snake :(')
          if gamer2==93:
              gamer2=73
              print('playe2 snake :(')
          if gamer2==95:
              print('playe2 snake :(')
              gamer2=75
          if gamer2==99:
              print('playe2 snake :(')
              gamer2=78     
          print('player1 score:',gamer1)
          print('player2 score:',gamer2)
     print('thank you for playing:)')
     print('if you want play again press enter else press enthing else')
     gamer1=input()
     if gamer1=='':
          continue
     else:
          break
































