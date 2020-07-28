#Write a Python code to print out the given sudoku puzzle matrix in the following format.
#Use not more than "control flow statement and boolean logic operators" in solving this code problem.

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
counti = 0

for i in sudoku:
    if counti % 3 == 0:
        print("\n") if counti != 0 else print("")
        for j in range(len(i)+2):
            print("-") if j == len(i)+2 else print("-", end=" ")
                    
    count = 0
    countj = 0
    print("\n")
    for j in i:
        countj += 1
        count +=1
        print(j) if count == len(i) else print(j, end=" ")
        if count == 3 and countj != len(i):
            print("|", end=" ")
            count = 0
        

    counti += 1

    if counti == len(i):
        print("\n")
        for j in range(len(i)+2):
            print("-", end=" ")
    
