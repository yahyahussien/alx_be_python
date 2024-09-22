size = int (input("enter the size of the pattern: "))
i = 1
while i <= size:
    j = 1
    for j in range(size):
        print("*", end = "")
        j += 1
    print() 
    i += 1