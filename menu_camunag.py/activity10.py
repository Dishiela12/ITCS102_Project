name = input("Enter your name:   ")
isStudent = input("Are you a current student of DLL(yes/no)?:     ")

if isStudent.lower() == "yes":
    yearLevel = input("What are yu currently enrolled for? \nF- Freshmen \nS- Sophomore \nJ- Junior \nSR- Senior:  \nPlease input your answer here:   ")

    if yearLevel.lower() == "f":
        print(f"Hi {name}, Freshmen, Welcome to DLL ")
    elif yearLevel.lower() == "s":
        print(f"Hi {name}, Sophomore, Welcome to DLL ")
    elif yearLevel.lower() == "j":
        print(f"Hi {name}, Junior, Welcome to DLL ")
    elif yearLevel.lower() == "sr":
        print(f"Hi {name}, Senior, Welcome to DLL ")
if isStudent.lower() == "no":
    print("Sorry, you're not allowed to use the system")
else:
    print("Thank you for using the system")