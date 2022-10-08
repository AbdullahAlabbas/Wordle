words = []
letter="a"
position=1
wordlist=[]
with open('FiveLetters.txt') as w:
  words = w.readlines()

while letter!='':
  del wordlist[:]
  letter=input("What letter do you know? ").lower()
  color=input("What color is it? (Y,G,B): ").lower()
  if color == 'g' or color == 'y':
    position=int(input("What position is it? (1-5)"))-1
  for word in words:
    if color == 'g':
      if word[position]==letter:
        wordlist.append(word)
    elif color == 'b':
      if letter not in word:
        wordlist.append(word)
    elif color == 'y':
      if letter in word:
        if word[position]!=letter:
          wordlist.append(word)
  words=wordlist.copy()
  print(*wordlist)