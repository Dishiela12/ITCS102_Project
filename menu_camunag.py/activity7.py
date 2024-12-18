gold = 6
miner = input("Hi, what is your name?: ")

isGold = input("is the mineral gold? ")

if isGold.lower() == "yes":
    gold += 7
    print(f"Hi {miner}, Your total number of {gold}")
else:
    print(f"Hi {miner}, Your total number of {gold}")