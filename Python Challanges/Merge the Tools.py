def merge_the_tools(string, k):
    # your code goes here
    u = split(string, k)

    for i in u:
        print(i)

def split(s, k):
    u = []
    i = 0
    while i < len(s):
        u.append(clean(s[i:i+k]))
        i += k
    return u

def clean(string):
    bank = []
    new_string = ''

    for i in string:
        if i not in bank:
            bank.append(i)
            new_string += i
    return new_string

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)