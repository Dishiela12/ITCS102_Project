
number = int(input("Enter Number Amount:  "))
limit = 0
while limit < number:
    loop_number = int(input("Enter Number: "))
    loop_number = loop_number + loop_number
    limit += 1

print("The sum of all the numbers given is", loop_number)