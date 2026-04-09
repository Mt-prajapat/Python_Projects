import random

print("Welcome to the Number Guessing Game!")
num = input("Type a number: ")

if num.isdigit():
  num = int(num)
  
  if num<=0:
    print('Please type a number larger than 0 next time.')
    quit()
else:
  print("Please type a number next time.")
  quit()
 
random_number = random.randint(0,num)
guesses = 0

while True:
  guesses+=1
  user_guess = input("Make a Guess: ")
  
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print('Please type a number next time.') 
    continue
  
  if user_guess==random_number:
    print("You got it!")
    break
  elif user_guess>random_number:
    print("You were above the number!")
  else:
    print("You were below the number!")
print("you got it in",guesses,"guesses")