if __name__ == '__main__':
    array_size, set_size = input().split()

    numbers = input().split()

    a_set = set(input().split())
    b_set = set(input().split())

    score = sum([(i in a_set) - (i in b_set) for i in numbers])

    print(score)
    '''
    
    score - numbers.count(b_set[i])
    
        
    
    dic = {}
    number = input().split()

    for i in number:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1


    print(dic)
    
    a_set = input().split()
    b_set = input().split()



    score = 0

    for x in dic:
        if x in a_set:
            score += dic[x]
        elif x in b_set:
            score -= dic[x]

    print(score)
    '''
