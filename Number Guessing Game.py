import random

Cnumber = random.randrange(1,101)
Unumber = int(input("Please Enter Your Guess Number: "))


if Cnumber > Unumber:
    print("Your Guess Number is Too Low")
elif Unumber > Cnumber:
    print("Your Guess Number is Too HIGH")
else:
    print("Your Guess NUmber are Equal")