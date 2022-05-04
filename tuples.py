"""
Characteristics:
1. A tuple is a ordered collection of objects or data.

2. tuples are immutable, means unlike lists, the elements in a defined tuple cannot be changed.

3. We define a tuple by enclosing the elements in parentheses () instead of square brackets [].

4. Elements in a tuple are stored in a comma separated manner, just like a list.
"""

colors = ("red", "green", "blue", "brown", "orange", "purple")
# print(colors)
# print(colors[0])
# print(colors[1])

# using negative index
# print(colors[-1])

studentData = (1, "Rahul", [90, 89, 87, 76, 85], "A+")
# print(studentData)
marks = studentData[2]
# print(marks)

bagpack = ("bottle", ("pen", "notebook"), "laptop")
print(bagpack)
print(bagpack[1])
