n = 5
size = 2 * n - 1
center = n - 1

for i in range(size):
    for j in range(size):
        if abs(i - center) + abs(j - center) == center:
            print("*", end="")
        else:
            print(" ", end="")
    print()
