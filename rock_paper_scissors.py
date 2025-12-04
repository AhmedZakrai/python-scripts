## ROCK, PAPER and SCISSORS Game
import random , sys

print (f'# ' * 31 , '\n' ,' ' * 19 ,'*' * 23  )
print (' ' * 21 ,'ROCK, PAPER, SCISSORS')
win , los , tie = 0 , 0 , 0

while True :
  print (f'{win} Wins, {los} Losses, {tie} Ties')
  print ('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
  select = input ('>')
  if select == 'r' :
     select = 'ROCK'
     u = 1
  elif select == 'p' :
     select = 'PAPER'
     u = 2
  elif select == 's' :
     select = 'SCISSORS'
     u = 3
  elif select == 'q' :
     sys.exit()
  else :
     print ('pleas !!! ')
     continue
  print (f'{select} versus...')
  choes= random.randint(1,3)

  if  choes == 1 : 
    print ('ROCK\nYou win!')
  elif choes == 2 :
     print ('SCISSORS\nSory you losse!')
  elif choes == 3 :
    print ('PAPER\nIt is a tie!')
   
  if choes == u : 
    tie += 1
  elif chose == 2 and u == 1 :
    los += 1
  elif chose == 3 and u == 1 :
    win += 1
  elif chose == 1 and u == 2 :
    win += 1
  elif chose == 3 and u == 2 :
    los += 1
  elif chose == 1 and u == 3 :
    los += 1
  elif chose == 2 and u == 3 :
    win += 1
  

