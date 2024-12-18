for x in range(10, 0, -1):
    print(" " * (10 - x) * 2, end = "")
    for y in range(x):
        print("*", end = " ")
    print()