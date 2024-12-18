isContinue = True
triangle = 0  

while isContinue:
    ask = input("Do you like to create more triangles (yes / no): ")
    if ask.lower() == "no":
        print("Program Terminated")
        break
    
    elif ask.lower() == "yes":
        triangle += 1  
        print(f"Creating triangle #{triangle}:\n")
        
        for x in range(1, 6):  
            for y in range(x):  
                print("*", end=" ")
            print()  
            
    else:
        print("Invalid answer, please only answer 'yes' or 'no'")