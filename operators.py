"""
Operators:
1. Arithmatic Operator
2. Assignment Operator
3. Comparison Operator 
4. Logical Operator
5. Bitwise Operator
"""

"""
Arithmatic Operator
-> +, -, *, /, %, **, //
"""
# print(5%3)
# print(3**3)

"""
Assignment Operator
-> =, +=, -=, *=, /=, %=
"""
x = 10
x += 5 # x = x+5

"""
Comparison Operator
-> ==, !=, >, <, >=, <=
"""
x = 5
y = 10
# print(x < y) 

"""
Logical Operator
-> and, or, not

False or True -> True
True and False -> False 
not False -> True
"""
# x == y, x < y
# print(x == y or x < y)
# print(not(x < y and x != 5))

"""
Bitwise Operator
-> &, |, ^, !, >>, <<

Bunary:
4 -> 100
5 -> 0101
(1 -> True, 0 -> False)

0101
0100 
----
0100 -> 4
"""
x = 4
y = 5
print(x&y)
