#! python3

import os, re, random

#path to wordlist to be used
filepath = "c:\\pythonScripts\\eff_large_wordlist.txt"

#count the number of entries in the wordlist
with open(filepath) as lc:
    linecount = 0
    for cnt, line in enumerate(lc):
        linecount += 1

#randomize which word to select from word list
random1 = random.randint(0,linecount-1)

#select a random entry from the list
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt == random1:
            select = line

#randomize a two digit number to put after the selected word
random2 = random.randint(1,99)

#Add a leading zero if the number is less that 10
if random2 < 10:
    trail = "0" + str(random2)
else:
    trail = str(random2)
    
#Use regex to filter out everything but letters
#put everything together and capitalize the first letter
pattern =  ['[a-z]+']
for p in pattern:
    match = re.findall(p, select)
    print(match[0].capitalize() + trail)
    




