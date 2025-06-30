def collatz(number):
    if number % 2 == 0:
        return(number // 2)

    elif number % 2 == 1:
        return(3 * number + 1)

print('Enter an integer')

try:
    usersNumber = int(input())
    while usersNumber != 1:
        print(collatz(usersNumber))
        usersNumber = collatz(usersNumber)
        if usersNumber == 1:
            break
except ValueError:
    print('You must have entered a string. Please enter an integer.')



