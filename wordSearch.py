import random
from random_word import RandomWords
rw = RandomWords()
# Creating a random word object
rw.get_random_words(hasDictionaryDef = "true",
                maxLength = 10,
                limit = 4)


def randomFill(wordSearch):
    Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(0,12):
        for col in range(0,12):
            if wordSearch[row][col]=="-":
                randomLetter = random.choice(Letters)
                wordSearch[row][col] = randomLetter

def  displayWordSearch(wordSearch):
    print(" _________________________")
    print("|                         |")
    for row in range(0,12):
        line="| "
        for col in range(0,12):
            line = line + wordSearch[row][col] + " "
        line = line + "|"
        print(line)
    print("|_________________________|")

#def addWord(rw, wordSearch):
#    row = random.randint(0,11)
#    col = 0
#    for i in range(0,len(rw.get_random_words)):
#        wordSearch[row][col+i] = rw[i]

def addWord(word, wordsearch):
  row=random.randint(0,11)
  col=0
  for i in range(0,len(word)):
    wordsearch[row][col+i]=word[i]

wordSearch = []
for row in range(0,12):
    wordSearch.append([])
    for col in range(0,12):
        wordSearch[row].append("-")


#addWord(rw, wordSearch)
addWord("example", wordSearch)
#print(rw.get_random_words)

randomFill(wordSearch)

displayWordSearch(wordSearch)

