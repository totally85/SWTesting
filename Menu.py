import sys
import emailVerifier

def displayMenu():
    print("Choose one of the below:")
    print("1. Body Mass Index")
    print("2. Retirement")
    print("3. Distance Formula")
    print("4. Email Verifier")
    print("5. Exit")
    choice = input("Number: ")
    return choice

def choices(x):
    if x == 1:
        import bmiMain
    elif x == 2:
        import retirementMain
    elif x == 3:
        import distanceMain
    elif x == 4:
        address = input("Enter email address: ")
        isValid = emailVerifier.verifyEmail(address)

        if isValid == True:
            print("Email is valid")
        else:
            print("Invalid email address")
    elif x == 5:
        exit(0)
    else:
        c = input("Invalid number chosen. Choose again: ")
        x = int(c)
        choices(x)

def main():
    number = displayMenu()
    choices(int(number))

if __name__ == "__main__":
    main()

