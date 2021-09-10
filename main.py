# This is the first DA assignment for CPSC222 at Gonzaga University Fall 2021
# instructor: Gina Sprint
# student: Scott Economu

'''
The assignment:

Write a program (main.py) that declares a list with the following floating point numbers: 
84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3, 47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0
Write code to compute and display the following statistics summarizing the above list of numbers 
(the only module you may use to compute these statistics is the math module... that means no statistics, numpy, scipy, pandas, etc...):
•	Count of the numbers
•	Average (mean) of the numbers
•	Standard deviation of the numbers 
•	Median number
•	Smallest number
•	Largest number
Each statistic should have an informative string label displayed in front of it and should be rounded to 2 decimals places. Check your answers 
against a desk check (compute the stats by hand) and/or using Excel.

Next, prompt the user to enter a starting value (start) and an ending value (end). Replace all the values in the list that are between [start, stop] 
inclusive with the value 0. Then print the list to inform and show the user the modified list.

Bonus (3 pts) 
Print out the list in reverse in the following format (all on one line, numbers separated by _: 91.0 _ 25.1 _ 61.8 _ 75.6 _ 28.2 _ 50.5 _ 90.8 _ 58.3 _ 47.7 _ 30.3 _ 78.4 _ 40.5 _ 51.1 _ 25.9 _ 42.1 _ 75.8 _ 84.4
Do not use reverse() to do this. You must write your own loop to solve this problem.
'''

import math

# build the list
my_List = [84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3, 47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0]

# get the number of elements
list_Length = len(my_List)

# get the sum of the list elements
list_Sum = 0
for element in my_List:
    list_Sum = list_Sum + element

# calculate the average value of the elements (the mean)
list_average = list_Sum / list_Length

# get the standard deviation
list_of_means = []
for x in my_List: # subtract mean from element
    list_of_means.append((x-list_average) ** 2)
means_average = 0
for x in list_of_means: # get the sum of the means
    means_average = means_average + x
means_average = means_average / len(list_of_means) # get the average of the means
std_dev = math.sqrt(means_average)

#sort the list to get the median, largest,  and smallest numbers
my_list_sorted = my_List
my_list_sorted.sort()
median_number = my_list_sorted[int (round((len(my_list_sorted)/2),0))]
smallest_number = my_list_sorted[0]
largest_number = my_list_sorted[len(my_list_sorted)-1]

# print the results
print("The list is: ", my_List)
print("There are", list_Length, "numbers in the list.")
print("The average value of the the numbers in the list is: ", "{:.2f}".format(list_average))
print("The standard deviation of the numbers in the list is: ", round(std_dev, 2))
print("The median number in the list is", median_number)
print("The smallest number in the list is", smallest_number)
print("The largest number in the list is", largest_number)

