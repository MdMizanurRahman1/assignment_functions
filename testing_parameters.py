#4
#Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list,
# call the function, and print out the value it returned.

def main_function(numbers_list):
    sum_of_numbers=sum(numbers_list)
    return sum_of_numbers

number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result=main_function(number_list)
print(result)