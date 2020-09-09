
def fizzBuzz(n):
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0 and x % 5 != 0:
            print('Fizz')
        elif x % 3 != 0 and x % 5 == 0:
            print('Buzz')
        else:
            print(x)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
