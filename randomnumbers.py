import math
import random
import numpy as np


def total(random_num):
   return total(random_num)

def average(random_num):
   return round(sum(random_num) / length, 2)

def square(random_num):
    return np.square(random_num)

def reverse(random_num):
   return random_num[::-1]
  
def sort(random_num):
   return np.sort(random_num)

def log(random_num,base):
    base = int(input("Please enter a base: "))
    return[math.log(x, base) for x in random_num]

def cumulative(random_num):
    return np.cumsum(random_num)

def even(random_num):
    return [i for i in random_num if i % 2 == 0]

def greater(random_num, greater_num):
    greater_num = int(input("give value: "))
    return [i for i in random_num if i > greater_num]
    
def less(random_num, less_num):
    less_num = int(input("give value: "))
    return [i for i in random_num if i < less_num]

def generate_number_list(last_num, length):
    return [random.randint(0, last_num) for _ in range(length)]

input_last_num = int(input("Enter your last number: "))  # length
input_length = int(input("How many numbers do you want to produce: "))  # length
random_num_list = generate_number_list(input_last_num, input_length)
choose_operation = input(
    """
which operation do you need?:
Available Options: [total, average, square, reverse, sort, log, cumulative, even, greater, less]
option = """
)

print(f"Init List: {random_num}")
print(f"Choosed: {choose_operation}")

if choose_operation == 'total':
    result = total(random_num_list)
    
elif choose_operation == 'average':
    result = average(random_num_list)
    
"""..."""
## other functions
""" ... """
    
print(f"Result: {result}") ##how to return?




#if choose_operation == "total":
    #result = sum(random_num)



#elif choose_operation == "average":
    #average = sum(random_num) / length
    #result = round(average, 2)


#elif choose_operation == "square":
    #result = np.square(random_num)
    

#elif choose_operation == "reverse":
    #result = random_num[::-1]

    # # OR
    # result = random_num[:]
    # result.reverse()



#elif choose_operation == "sort":
    #result = np.sort(random_num)



#elif choose_operation == "log":
    # result = np.log(random_num)

    # list comprehension
    #base = int(input("Please enter a base: "))
    #result = [math.log(x, base) for x in random_num]


#elif choose_operation == "cumulative":
    #result = np.cumsum(random_num)
    

#elif choose_operation == "even":
    #result = [i for i in random_num if i % 2 == 0]
    



#elif choose_operation == "greater":
    #greater_num = int(input("give value: "))
    #result = [i for i in random_num if i > greater_num]
    
#elif choose_operation == "less":
    #less_num = int(input("give value: "))
    #result = [i for i in random_num if i < less_num]
