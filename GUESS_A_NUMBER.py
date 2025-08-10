'''
Guess an integer number in a range(0,9)
with input as chances
'''
chance=int(input("Enter how many chances you want : "))
num=7
for i in range(0,chance):
    guess=int(input("Enter your guess : "))
    if guess==num:
        print("YOUR GUESS IS CORRECT!")
    elif guess>num:
        print("YOUR GUESS IS HIGH")
    else:
        print("YOUR GUESS IS LOW")
