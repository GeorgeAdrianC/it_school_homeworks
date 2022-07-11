def main(n,x):
    matrix = []
    if 2<=n<=20:
        for i in range(1, n):
            for j in range(1, n):
                a.append(int(input()))
            matrix.append(a)
            print(matrix[i][j], end = " ")
        print()
    else:
        print("You're out from the requested range.")
    return matrix
    