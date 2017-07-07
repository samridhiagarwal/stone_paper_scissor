from random import randint
print("Let's Play Stone Paper Scisor")
player = input('stone (s), paper (p) or scissors (s)?')

if(player == 'r'):
  print('*', end=' ')
  
elif(player == 'p'):
  print('###', end=' ')
  
elif(player == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'r'
  print('*')
  
elif(chosen == 2):
  computer = 'p'
  print('###')
  
else:
  computer = 's'
  print('>8')

if(player == computer):
  print('DRAW!')
  
elif(player == 'r' and computer == 's'):
  print('Player wins!')
  
elif(player == 'r' and computer == 'p'):
  print('Computer wins!')
  
elif(player == 'p' and computer == 'r'):
  print('Player wins!')
  
elif(player == 'p' and computer == 's'):
  print('Computer wins!')

elif(player == 's' and computer == 'p'):
  print('Player wins!')
  
elif(player == "s" and computer == 'r'):
  print('Computer wins!')

else:
  print('Huh?')
  
  
