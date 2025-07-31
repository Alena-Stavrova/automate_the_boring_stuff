#Chapter 6
#NOTE: the author suggests to end the program with:
#print('Chance of streak: %s%%' % (number_of_streaks / 100))
#...but this would be percentage for 1 experiment, and we did 100K, so I changed it to:
#% (number_of_streaks / 100 / 100000)
#Alternatively, we could create number_of_streaks = [], append each result and then avg_number_of_streaks = sum / len

#Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails.
#Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, and the second part checks if there is a streak in it.

#Put all of this code in a loop that repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row.
#As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

#To create a list, use a for loop that appends a randomly selected 'H' or 'T' to a list 100 times.

#To determine if there is a streak of six heads or six tails, create a slice like some_list[i:i + 6] (which contains the six items starting at index i)
#and then compare it to the list values ['H', 'H', 'H', 'H', 'H', 'H'] and ['T', 'T', 'T', 'T', 'T', 'T'].


import random
number_of_streaks = 0
for experiment_number in range(100000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    tosslist = []
    for i in range(100):
        toss = random.randint(0, 1) # 0 is tails, 1 is heads
        if toss == 0:
            tosslist.append('T')
        else:
            tosslist.append('H')
    #print(tosslist)

    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(tosslist) - 5):
        if tosslist[i:i+6] == ['H', 'H', 'H', 'H', 'H', 'H'] or tosslist[i:i+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            number_of_streaks += 1
    #print(number_of_streaks)

print('Chance of streak: %s%%' % (number_of_streaks / 100 / 100000))
