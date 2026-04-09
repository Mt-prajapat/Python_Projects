name = input("Enter your name: ")
print("Welcom",name,"to this adventure!")

question = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go(left/right)? ").lower()
if question=="left":
  question = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross(walk/swim): ")
  
  if question == "swim":
    print("You swam acrross and were eaten by an alligator.")
  elif question == "walk":
    print("You walked for many miles, ran out of water and you lost the game.")
  else:
    print("Not a valid option. You lose.")

elif question=="right":
  question = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
  
  if question=="back":
    print("You go back and lose.")
  elif question=="cross":
    question = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
    
    if question=="yes":
      print("You talk to the stanger and they give you gold. You WIN!")
    elif question=="no":
      print("You ignore the stranger and they are offended and you lose.")
    else:
      print("Not a valid option. You lose.")
  else:
    print("Not a valid option. You lose.")
else:
  print("Not a valid option. You lose.")

print("Thank you for trying",name)