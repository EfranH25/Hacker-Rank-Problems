def math(x, y, z, n):
    matrix = []

    [[[matrix.append([i, j, k]) for k in range(z+1) if i + j + k != n] for j in range(y+1)] for i in range(x+1)]
    return matrix


if __name__ == '__main__':
    x = 1
    y = 1
    z = 1
    n = 2

    print(math(x,y,z,n))


