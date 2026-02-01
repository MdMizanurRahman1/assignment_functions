#5
#Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as
# the original list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list,
# call the function, and then print out both the original as well as the cut-down list.

def main_function(integers_list):
    second_list=[]
    for number in integers_list:
        if number%2==0:
            second_list.append(number)
    return second_list

integers_list=[1,2,3,4,5,6,7,8,9,10,21,22,23,24,25,26,27,28,29,30,31]
final_list=main_function(integers_list)
print("The original number list:", integers_list)
print("The even number list:", final_list)