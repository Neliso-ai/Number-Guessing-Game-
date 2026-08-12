import random

name = "____number guessing game____".upper()
print(name)
secret_num = random.randint(1,100)

attempts = 10
print(f"You only have {attempts} attempts ")
	
while attempts != 0:	
	try:
		guess = int(input("Guess the number from 1 to 100: "))
		if guess < 1 or guess > 100:
		  print("Please only enter numbers between 1 and 100 !!".upper())
		  continue
		attempts -= 1
		print(f"You have {attempts} attempts left")
		
		if guess <  secret_num:
			print("Guess a higher number")
			
		elif guess >  secret_num:
			print("Guess a lower number")
		
		else :
			print("Congratulations , YOU WON !!!!".upper())
			break
	
	except ValueError:
		print("Only numbers can be entered !!!".upper())
else:
	print("Out of attempts\nGAME OVER!!!!".upper())
	print(f"The secret number was: {secret_num}")

		
	

	
	