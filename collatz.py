#Write a function named collatz() that has one parameter named number.
#If number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
    if number % 2 == 0:
        return(number// 2)
    else:
        return(3 * number + 1)

#Then, write a program that lets the user enter an integer and that keeps calling collatz() on that number until the function returns the value 1.

#Add try and except statements to the previous project to detect whether the user entered a non-integer string.
#Normally, the int() function will raise a ValueError error if it is passed a non-integer string, as in int('puppy').
#In the except clause, print a message to the user saying they must enter an integer.

user_number = input()
try:
    while int(user_number) != 1:
        user_number = collatz(int(user_number))
        print(user_number)
except ValueError:
        print('Please enter an integer')


