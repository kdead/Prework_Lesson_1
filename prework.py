# Question 1
# Write a function to print "hello_USERNAME!" Useername is the input of the function. 
def hello_name(user_name):
    """Greet the user."""
    print("Hello " + user_name + "!")
hello_name("Karneisha")  


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    """Print odd numbers from 1-100."""
    for number in range(1, 100):
        if number % 2 != 0:
            print(number)
first_odds()            


#Question 3
# Write a python function, max_num_in list to return the max number in a given list. 

def max_num_in_list(a_list):
    """Return the max number in the given list."""
    if not a_list:
        return None
    return max(a_list) 
a_list = [56, 38, 15, 22]
max_value = max_num_in_list(a_list)
max_num_in_list(a_list)
print(max_num_in_list(a_list))


# Question 4
# Write a function to return if the given year is a leap year.

def is_leap_year(a_year):
    """Return True if the year is a leap year."""
    if (a_year % 4 ==0  and a_year % 100 != 0) or (a_year % 400 == 0): 
        return True
    else:
        return False
print(is_leap_year(1986))     


# Question 5 
# Write a function to check to see if all numbers in list are consecutive numbers. 

def is_consecutive(a_list):
    """Return True if the list is consecutive numbers"""
    if not a_list:
        return False
    for i in range(len(a_list) - 1):
        if a_list [i] + 1 != a_list[i + 1]:
            return False
    return True
print(is_consecutive([3, 4, 5, 6]))