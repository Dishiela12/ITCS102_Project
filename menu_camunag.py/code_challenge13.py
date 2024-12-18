for x in range(1, 6):
    for a in range(5 - x):
        print(" ", end=" ")
    for b in range(x, 0, -1):
        print(b, end=" ")
    for c in range(2, x + 1):
        print(c, end=" ")
    print()


for x in range(4, 0, -1):
    for d in range(5 - x):
        print(" ", end=" ")
    for e in range(x, 0, -1):
        print(e, end=" ")
    for f in range(2, x + 1):
        print(f, end=" ")
    print()
