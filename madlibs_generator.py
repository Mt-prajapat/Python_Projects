with open("letter.txt","r") as f:
  letter = f.read()
  
words = set()
target_start = "<"
target_end = ">"
start_of_word = -1

for i,char in enumerate(letter):
  if char==target_start:
    start_of_word = i
    
  if char == target_end and start_of_word!=-1:
    word = letter[start_of_word: i +1]
    words.add(word)
    start_of_word = -1
    
answers = {}

for word in words:
  answer = input("Enter a word for "+word+": ")
  answers[word] = answer
  
for word in words:
  letter = letter.replace(word,answers[word])
  
print(letter)