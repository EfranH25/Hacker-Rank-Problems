if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    second = arr[0]
    max = max(arr)

    for x in arr:
        if x >= second and x < max:
            second = x
    print(second)


