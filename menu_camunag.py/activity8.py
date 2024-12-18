password = input("Enter your password --> : ")

if password.lower() == "panackes":
    print("Access Granted")
    print("Enjoy using the system")
elif "burgers":
    print("beef patty")
    print("Access Granted")
elif password.lower() == "creamstew":
    print("jumbosize")
    print("Access Granted")
elif password.lower() == "icecream":
    print("chocolate")
    print("Access Granted")

else:
    print("Access Denied")

print("System Exit")