colors = ['orange', 'red', 'yellow', 'black', 'green', 'skyblue']
"""
Syantax: colors[m:n:s]
m --> start index
n --> ending index (excluded)
s --> step
"""

# index 2 to index 4
# print(colors[2:5])

# include all the elements
# print(colors[:]) # [0:len(colors)]
# print(colors[0: len(colors)])

# from starting to a perticular index
# print(colors[:4])

# from a perticular index to the end
# print(colors[3:])

# Negative index
# print(colors[:-2])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])

# reversing a list
print(nums[::-1])

# using with built-in functions
print(sum(nums[2:6]))
