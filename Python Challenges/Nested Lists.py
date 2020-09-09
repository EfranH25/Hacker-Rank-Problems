# Key to sort array by number
def sort_key(val):
    return val[1]

# Key to sort array by alphabet
def sort_key2(val):
    return val[0]


if __name__ == '__main__':
    # adds inputs to an array

    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        arr.append([name, score])

    arr.sort(key=sort_key)

    # gets min value
    min = arr[0][1]

    # puts second min value
    for x in arr:
        if x[1] > min:
            second_min = x[1]
            pos = x
            break

    #adds all second min value to answer array
    answer = []

    for i in arr[1:]:
        if i[1] == second_min:
            answer.append(i)
        if i[1] > second_min:
            break

    #sorts asnwer array alphabetically and prints output
    answer.sort(key=sort_key2)

    for z in answer:
        print(z[0])