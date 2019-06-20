
def check(word,limit):
    for i in range(len(word)):
        if word.count(word[i:i+1]) == limit:
            return True
    return False

def find_correct_boxID(boxids):
    for y in range(len(boxids)):
       for x in range(y+1,len(boxids)):
           count = 0
           for i in range(len(boxids[x])): 
               if boxids[x][i] != boxids[y][i]: 
                   count = count + 1
           if count == 1: 
               print(boxids[x] + " , " + boxids[y])                   

import os 
print(os.getcwd())

text_file = open("AD2.txt", "r")
words = text_file.readlines()
count3 = 0
count2 = 0
for x in range(len(words)):
    if check(words[x],2):
        count2 = count2 + 1
    if check(words[x],3):
        count3 = count3 + 1
print (count2 * count3)

print(find_correct_boxID(words))
text_file.close()

#huh thats pretty odd
#Im trying again to commit these changes