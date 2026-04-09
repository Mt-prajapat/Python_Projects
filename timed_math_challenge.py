import random
import time

Operators = ["+","-","*"]
Min_Operand = 3
Max_Operand = 12
Total_Problems = 10

def generate_questios():
  left = random.randint(Min_Operand,Max_Operand)
  right  = random.randint(Min_Operand,Max_Operand)
  operator = random.choice(Operators)
  
  expression = str(left) + " " + operator + " " + str(right)
  answer = eval(expression)
  return expression, answer

wrong = 0
input("Press enter to Start!")
print("----------------------")

start_time = time.time()

for i in range(Total_Problems):
  expressin, answer = generate_questios()
  while True:
    person = input("Problem #" + str(i+1) + ": " + expressin + " = ")
    if person == str(answer):
      break
    
    wrong += 1

end_time = time.time()
total_time = round(end_time - start_time,2)

print("-------------------------")
print("You are given Wrong answer",wrong,"times")
print("Nice Work! You finished in",total_time,"seconds!")