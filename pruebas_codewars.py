import re

# Remove vowels

# def disemvowel(string_):
#     to_remove = ["A","a","e","E","i","I","o","O","u","U"]
#     removed = string_
#     for remove in to_remove:
#         removed = removed.replace(remove,"")
#         print(removed)
#     return removed
    
    
    
# result = disemvowel("This website is for losers LOL!")
# print(result)
    
    
#___________________________________________________________________________
#___________________________________________________________________________


# square every digit of a number and concatenate them

# def square_digits(num):
#     squared = ""
#     for i in str(num):
#         squared += str(int(i) ** 2)
#     return int(squared)
    
    
    
    
# result = square_digits(9119)
# print(result)


#___________________________________________________________________________
#___________________________________________________________________________


# Given an integral number, determine if it's a square number:

# def is_square(n):    
#     if n < 0:
#         return False
#     elif (n ** 0.5) % 2 == 0:
#         return True
#     elif (n ** 0.5) % 2 == 1:
#         return True
#     else:
#         return False
# result = is_square(25)
# print(result)


#___________________________________________________________________________
#___________________________________________________________________________

# Implement a function which convert the given boolean value into its string representation

# def boolean_to_string(b):
#     return str(b)
    
# result = boolean_to_string(False)
# print(result)

#___________________________________________________________________________
#___________________________________________________________________________


#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     lowest_1 = numbers[0]
#     lowest_2 = numbers[1]
#     return lowest_1 + lowest_2   
# sum_two_smallest_numbers([5, 8, 12, 18, 22])
# print(result)


#___________________________________________________________________________
#___________________________________________________________________________


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     distance_left = mpg * fuel_left
#     if distance_left - distance_to_pump >= 0:
#         return True
#     else:
#         return False
# result = zero_fuel(100, 50, 1)
# print(result)


#___________________________________________________________________________
#___________________________________________________________________________


# def are_you_playing_banjo(name):
#     if name[0].lower() == "r":
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"
# result1 = are_you_playing_banjo("Rikke")
# result2 = are_you_playing_banjo("martin")
# print(result1)
# print(result2)


#___________________________________________________________________________
#___________________________________________________________________________





