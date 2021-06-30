import random
import time
print('''
This peice of code prints classic hello world but the twist is 
that it chooses a random alphabet and compares it to the aplphabets of hello world
until it gets it correct.
To demonstrate it more accurately this code will take a 0.2 sec break after printing
every correct alphabet and a 0.05 sec break for every wrong alphabet...  
''')
l = ['h','e','l','l','o',' ','w','o','r','l','d']
str=''
while True:
    word = random.choice('abcdefghijklmnopqrstuvwxyz ')
    try:
        if word==l[0]:
            str+=word
            print(str, end='\r')
            time.sleep(0.2)
            l.pop(0)
            #print(l)
        else:
            print(word, end='\r')
            time.sleep(0.05)
            continue
    except:
        b = input("\nHit any key to exit")
        break
