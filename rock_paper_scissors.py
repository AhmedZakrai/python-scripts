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
  elif select == 'p' :
     select = 'PAPER'
  elif select == 's' :
     select = 'SCISSORS'
  elif select == 'q' :
     sys.exit()
  else :
     print ('pleas !!! ')
     continue
  print (f'{select} versus...')
  choes= random.randint(1,3)

  if  choes == 1 : 
    print ('ROCK\nYou win!')
    win += 1
  elif choes == 2 :
     print ('SCISSORS\nSory you losse!')
     los += 1
  elif choes == 3 :
    print ('PAPER\nIt is a tie!')
    tie += 1

