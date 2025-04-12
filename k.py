import random 
print ("guess the number")
hidden = random.randint(1,20)
guess = int (input ("enter a number between 1 and 20: "))
while guess!= hidden:
    if guess > hidden:
        print ("too high")
    else:
        print ("too low")
    print (guess, "it's not correct")
    guess = int (input ("enter a number between 1 and 20: "))
    
print(guess, "this is correct. Well done!")
