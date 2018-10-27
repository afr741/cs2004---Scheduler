from random import randint, seed


#Calls function printA() if value is even, otherwise calles function printB()
def scheduler (value):
    if value <= 20:
        printA()
    elif value > 20 and value <= 50:
        printB()
    elif value > 50:
        printC()




#Prints "A" to the screen on every call
def printA():
    print ("A")




#Prints "B" to the screen on every call
def printB():
    print ("B")


#Prints "B" to the screen on every call
def printC():
    print ("C")


#Generates and prints a random value between 1 and limit, based on valueOfSeed. Makes call to scheduler with the random value as input.
def randNumSeq(valueOfSeed, limit):
    seed(valueOfSeed) #Sets the seed value for randint()
    print("\n\nPress the return key to start the program.\nPress return key after every run to proceeed to the next stage.\nEnter 'q' as input value (Q key, then Return key) to stop the program")
    while input().lower() != 'q':
        value = randint(1, limit)
        print (value, end=" ")
        scheduler(value)




def main ():
    #lets the user to run multiple instances of the program with various settings
    while True: 
        option = input("\n1. Run program\n2. Exit\nEnter your choice (1 or 2):")
        while option != "1" and option != "2":
            option = input("\nWrong input. Enter either 1 or 2:")
        if option == "2": #Exits the program based on user's choice
            return

    #set the value of seed and allows the user to select between random seed mode and User-provided seed mode
        option = input("\n1. Random seed\n2. User-provided seed\nSelect mode (1 or 2):")
        while option != "1" and option != "2" and option != "3":
            option = input("\nWrong input. Enter either 1 or 2 or 3:")
        if option == "2":
            valueOfSeed = int(input("\nEnter any positive integer for the seed value of the random number generator:"))
        else:
            valueOfSeed = (randint(1,200))
 #Set range value
        limit = int(input("\nPlease enter the RANGE for random number sequence: "))
        randNumSeq(valueOfSeed, limit)
main()
