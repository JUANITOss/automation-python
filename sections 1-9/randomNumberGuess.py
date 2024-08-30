import random

def guessNumber(li, ls, tries):
    
    number = random.randint(li,ls)
    
    for i in range(tries):
        inputNumber = int(input("Insert a number: "))
        
        if inputNumber > number:
            print("Number is too high")
        elif inputNumber < number:
            print("Number is too low")
        else:
            break
    
    return inputNumber, number       
        
def checkGuessNumber(ni, nr):
    
    if ni == nr:
        print("well done! Thats the correct number")
    else:
        print("sorry, the number you entered is wrong :(") 

def main(args=None):
    number, mNumber = guessNumber(0,10,5)
    checkGuessNumber(number, mNumber)

main()
