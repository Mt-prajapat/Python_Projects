import random

colors = ["R","G","B","W","O","P"]
Tries = 10
Code_Length = 4

def generate_code():
  code = []
  
  for _ in range(Code_Length):
    color = random.choice(colors)
    code.append(color)
    
  return code

def guess_code():
  
  while True:
    guess = input("Guess: ").upper().split(" ")
    
    if len(guess) != 4:
      print(f"You must guess {Code_Length} colors.")
      continue
    
    for color in guess:
      if color not in colors:
        print(f"Invalid color: {color}. Try again.")
        break
      
    else:
      break
  
  return guess

def check_code(guess, real_code):
  color_counts = {}
  correct_pos = 0
  incorrect_pos = 0
  for color in real_code:
    if color not in color_counts:
      color_counts[color] = 0
    color_counts[color] += 1

  
  for guess_color, real_color in zip(guess, real_code):
    if guess_color == real_color:
      correct_pos += 1
      color_counts[guess_color] -= 1
      
  for guess_color, real_color in zip(guess, real_code):
    if guess_color in color_counts and color_counts[guess_color] > 0:
      incorrect_pos += 1
      color_counts[guess_color] -= 1
      
  return correct_pos, incorrect_pos

def game():
  print(f"Welcome to mastermind, you have {Tries} to guess the code...")
  print("The valid colors are",*colors)
  
  code = generate_code()
  for attempts in range(1, Tries+1):
    guess = guess_code()
    correct_pos, incorrect_pos = check_code(guess, code)
    
    if correct_pos == Code_Length:
      print(f"You guessed the code in {attempts} tries!")
      break
    
    print(f"Correct Position: {correct_pos} | Incorrect Position: {incorrect_pos}")
    
  else:
    print("You ran out of tries, the code was: ", *code)
    
if __name__ == "__main__":
  game()