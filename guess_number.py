# Guess the Number Game 

import random , sys
print ('=================================================')
number_guess = random.randint(1,20)
print ('I am thinking of anumber between 1 and 20.')
print ('If you want colesd enter "exit" !')
cont = 0
while True:
	number_ent = input('Take a guess.\n>')
	cont += 1
	if int(number_ent) == number_guess :
		print (f'Good job ! You got it in {cont} guesses !')
		break
	elif int(number_ent) > number_guess :
		print ('Your guess is too high.')
	elif int(number_ent) < number_guess :
		print ('Your guess is too low.')
	elif number_ent == 'exit' :
		sys.exit()
	else : 
		continue
























