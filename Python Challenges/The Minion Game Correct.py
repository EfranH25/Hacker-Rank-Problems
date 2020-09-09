def minion_game(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    stuart, kevin = 0, 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string)-i
        else:
            stuart += len(string)-i

    if stuart > kevin:
        print('Stuart ' + str(stuart))
    elif kevin > stuart:
        print('Kevin ' + str(kevin))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)