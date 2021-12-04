# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    new_lst = []
    for val in range(num, -1, -1):
        new_lst.append(val)
    return new_lst
print(countdown(255))

# Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(lst):
    print(lst[0])      
    return lst[1]
print(print_and_return([3,5]))

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(lst):
    return lst[0] + len(lst)
print(first_plus_length([10,2,3,4,4,5,6,8]))

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(lst):
    new_lst = []
    if len(lst) < 2:
        return False
    for val in range(len(lst)):
        if val > lst[1]:
            new_lst.append(val)
    print(len(new_lst))
    return new_lst
print(values_greater_than_second([5,2,3,2,1,4]))


# /* Challenge 1: Leap year
# A leap year occurs when the year is divisible by 4.  There are exceptions, however:
# - If the year is divisble by 100 as well, it is NOT a leap year - but there's an exception to this too:
#   * If the year is divisible by 400, that is a leap year.
# Write a function that returns true if the given year is a leap year and false otherwise. 
# Examples: 2008 -> true, 2000 -> true (divisible by 400), 1900 -> false (divisible by 100 but not 400), 1885 -> false */

def leap_year(num):
    if num % 4 == 0 and num % 100 == 0 and num % 400 != 0:
        return False 
    if num % 400 == 0:
        return True
    if num % 4 == 0:
        return True 
    if num % 4 == 0 and num % 100 == 0 and num % 400 == 0:
        return True
    else:
        return False
print(leap_year(4))

# * Challenge 2: Sum numbers from 1 to N to a specific goal 
# Given a goal sum X, return the smallest integer N such the sum 1 + 2 + 3 + ... + N >= X.
# Examples:
# * Goal: 100: return 14 since 1 + 2 + 3 + 4 + 5 + ... + 14 = 105 >= 100 (summing 1 to 13 gives us 91, which is not enough)
# * Goal: 10: return 4 since 1 + 2 + 3 + 4 = 10 >= 10
# HINT: You might find a while loop useful. */

# take in 2 numbers one is gonna be iterated through adding all the numbers together i.e 1+2+3+4 = 10
#the second number is a goal to compare the sum to so as long as the sum is less than the goal it will run ?

def sum_num(x,y):
    sum = 0
    for num in range(1,x+1,1):
        while num < y:
            sum += num
    return sum 
print(sum_num(14, 100))