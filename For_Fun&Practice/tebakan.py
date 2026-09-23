import os
from random import randint as r

computer = r(1,10)
os.system('clear')

user = int(input('Pick a number from 1-10: '))
print("Computer: ",computer, "User: ",user)