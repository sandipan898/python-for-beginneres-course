colors = ['orange', 'red', 'yellow', 'black', 'green', 'skyblue']

# Traditional Way
new_colors = []
for x in colors:
    if x[-1] == 'e':
        new_colors.append(x)
# print(new_colors)

# List Comprehension
end_with_e_colors = [x for x in colors if x[-1] == 'e']
# print(end_with_e_colors)

"""
General Syntax:
new_list = [expression for item in iterable if condition == True]
"""

other_colors = [x for x in colors if x[-1] != 'e']
# print(other_colors)

# "orange" --> "ending with e"
# "Red" --> "red"

mismatch_colors = [x if x[-1] != 'e' else 'ending with e' for x in colors]
# print(mismatch_colors)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_nums = [x*x for x in nums]
print(squared_nums)

"""
1. We can put the condition check after the for loop.
2. We can put the condition check before the for loop.
   We can add else clause here.
3. Expression can be the item itself or any modified value
   from the original value.
4. Each time a new list will be created and old list will
   remain unchanged.
"""