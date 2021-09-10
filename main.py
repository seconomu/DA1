# This is the first DA assignment for CPSC222 at Gonzaga University Fall 2021
# instructor: Gina Sprint
# student: Scott Economu

'''
The assignment:

Write a program (main.py) that declares a list with the following floating point numbers: 84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3, 47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0
Write code to compute and display the following statistics summarizing the above list of numbers (the only module you may use to compute these statistics is the math module... that means no statistics, numpy, scipy, pandas, etc...):
•	Count of the numbers
•	Average (mean) of the numbers
•	Standard deviation of the numbers (link to formula)
•	Median number
•	Smallest number
•	Largest number
Each statistic should have an informative string label displayed in front of it and should be rounded to 2 decimals places. Check your answers against a desk check (compute the stats by hand) and/or using Excel.
Next, prompt the user to enter a starting value (start) and an ending value (end). Replace all the values in the list that are between [start, stop] inclusive with the value 0. Then print the list to inform and show the user the modified list.
Bonus (3 pts) 
Print out the list in reverse in the following format (all on one line, numbers separated by _: 91.0 _ 25.1 _ 61.8 _ 75.6 _ 28.2 _ 50.5 _ 90.8 _ 58.3 _ 47.7 _ 30.3 _ 78.4 _ 40.5 _ 51.1 _ 25.9 _ 42.1 _ 75.8 _ 84.4
Do not use reverse() to do this. You must write your own loop to solve this problem.
'''

import math

my_List = [84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3, 47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0]
list_Sum = 0
list_Length = len(my_List)

print(my_List)
print(len(my_List))
for element in my_List:
    list_Sum = list_Sum + element

list_average = list_Sum / list_Length
print(list_average)




