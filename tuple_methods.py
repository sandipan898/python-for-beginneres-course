numbers = (6, 7, 3, 6, 10, 12, 5, 6, 8, 5)

# count()
# returns the number of times a specified value occures in a tuple
# print(numbers.count(6))


# index
# search for a specified value in the tuple and returns the position where it is found
# if the specified element is not found it will throw ValueError
# finds the first occurance
# print(numbers.index(5))


# builtin functions
print(sum(numbers))
print(min(numbers))
print(max(numbers))


# slicing and comprehension
print([x*x for x in numbers])

print(numbers[1:5])
