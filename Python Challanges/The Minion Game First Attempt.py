def minion_game(string):
    # your code goes here
    (stuart, kevin) = word_list(string)

    print(get_score(stuart, kevin))



def check_vowel(x):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return True if x in vowels else False


def word_list(string):
    stuart = {}
    kevin = {}

    i = 0

    while i < len(string):
        if check_vowel(string[i]) is True:
            add_list(string[i:], kevin)
        else:
            add_list(string[i:], stuart)

        i += 1
    return stuart, kevin


def add_list(string, player):
    i = 0
    while i <= len(string):
        if string[:i] != '':
            if string[:i] not in player:
                player[string[:i]] = 1
            else:
                player[string[:i]] += 1
        i += 1
    return player


def get_score(s, k):
    s_score, k_score = 0, 0

    for i in s:
        s_score += s[i]

    for i in k:
        k_score += k[i]

    if s_score > k_score:
        return 'Stuart ' + str(s_score)
    elif s_score < k_score:
        return 'Kevin ' + str(k_score)
    else:
        return 'Draw'

if __name__ == '__main__':
    s = input()
    minion_game(s)