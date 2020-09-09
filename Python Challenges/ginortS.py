if __name__ == '__main__':
    word = input()

    lower, upper, odd, even = '', '', '',''

    for i in word:
        if i.islower():
            lower += i
        elif i.isupper():
            upper += i
        elif i.isnumeric():
            if int(i) % 2 != 0:
                odd += i
            else:
                even += i
    print(''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)))
