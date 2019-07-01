
import random
import time
count = 1
x = random.randint(1,10)
print("Hi there ...")
time.sleep(0.75)
print("I'm thinking of a number...")
time.sleep(0.75)
y = int(input("Can you guess it?: "))
while x != y:
    count +=1
    print("Wrong! Ty again :)")
    time.sleep(0.25)
    if y > x:
       print("HINT: It's smaller than the number you just entered.")
    elif x > y:
        print("HINT: It's larger than the number you just entered.")
    else:
        print("Next time, please enter a number!!")
    y = int(input("Can you guess the number I am thinking of?: "))
print("Well done, that's right!")
time.sleep(0.75)
if count == 1:
    print("It took you " + str(count) + " guess to get this correct.")
    time.sleep(1.0)
else:
    print("It took you " + str(count) + " guesses to get this correct.")
    time.sleep(1.0)
    
