# 1. Print a Multiplication Table

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i * j}", end="\t")
        print()
        
        
# 2. Check if a Matrix Is An Identity Matrix:

matrix = [[1,0,0],[0,1,0],[0,0,1]]
is_identity = True

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j and matrix[i][j] != 1:
            is_identity = False
        elif i != j and matrix[i][j] != 0:
            is_identity = False
            
    if is_identity:
        print("The Matrix Is an  Identity Matrix.")
    else:
        print("The Matrix Is Not AN Identity Matrix.")                        