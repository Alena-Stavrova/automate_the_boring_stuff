#Chapter 6

spam = ['apples', 'bananas', 'tofu', 'cats']
blabla = [1, 'oranges', 2, 100, 'Norway', True]
empty_list = []

#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with 'and' inserted before the last item.
#For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
#But your function should be able to work with any list value passed to it.
#Be sure to test the case where an empty list [] is passed to your function.

def list_stringinator(list):
    if len(list) != 0:
        for i in range(len(list)-1):
            print(str(list[i]), end = ', ')
        print('and ' + str(list[-1]))
    else: #Not sure how an empty list should work, this is my best guess
        print(' , and ') 

list_stringinator(blabla)
