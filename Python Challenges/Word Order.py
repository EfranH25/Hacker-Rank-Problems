if __name__ == '__main__':
    x = int(input())
    dict = {}

    for i in range(x):
        word = input()

        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    print(len(dict))

    for i in dict:
        print(dict[i], end=' ')