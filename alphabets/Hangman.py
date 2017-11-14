import random

#Disclaimer
print("""This is Emmet's super basic experimental hangman AI.
The computer only gets to mess up thrice.
The cruelty is good for it.""")

#opens library for current combo, guesses based on pre-established biases
def guess(num1,num2):
    name = "alphabet" + str(num1) + str(num2) + ".txt"
    name = name.replace(' ', '')
    file = open(name, 'r')
    alphabet = file.read()
    letters = alphabet.split(sep=",")
    if num2 == 0:
        guess = letters[(random.randint(1,len(letters)))-1]
        print(guess, "\n")

#gametime
def game():
    first = input("What is the first letter?\n")
    guess(first, 0)

#Infinite loop starts
while True:
    startAns = input("Are you ready to begin?\n")
    if startAns == "yes":
        game()
    elif startAns == "no":
        print("That's alright, take your time\n")
    else:
        print("What does", startAns, "mean!?\n")
        #rectify()
