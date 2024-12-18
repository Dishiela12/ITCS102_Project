def forhello():
    print("Hello, IT1A")

def activity2():
    print("Hi, Dishiela")

isContinue = True

while isContinue:
    print("PLEASE SELECT FROM THE FOLLOWING CODE \n1 = FOR HELLO \n2 - HELLO, DISHIELA \n3 - EXIT")

    ask = input("which program would you like to run, select from then options above:   ")

    if ask == "1":
        forhello()
        continue

    elif ask == "2":
        activity2()
        continue

    elif ask == "3":
        print("program terminated")
        break
    else:
        print("invalid choice")
        continue