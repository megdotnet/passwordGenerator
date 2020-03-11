#! python3

import os, random, ctypes

filepath = "c:\\pythonScripts\\eff_large_wordlist.txt"
random1 = random.randint(0,7775)
random2 = random.randint(1,99)

if random2 < 10:
    trail = "0" + str(random2)
else:
    trail = str(random2)

with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt == random1:
            select = line[6:]
            pword = select.capitalize().rstrip() + str(trail)
            print(pword)
            #input()
            #ctypes.windll.user32.MessageBoxW(0, str(pword), "Password Generator", 1)

