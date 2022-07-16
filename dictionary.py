"""
Characteristics:

1. Dictionaries are ordered. (V3.7 or higher. Means it kept the order of the values as it is inserted).

2. Mutable in nature. The values can be changed or updated.

3. Dictionaries are Dynamic in size. It can grow and shrink in size as needed.

4. Dictionaries can be nested. (A distionary can contain another dictionary).

5. Dictionary elements can be accessed by keys instead of index.

6. Duplicate keys are not allowed in Dictionaries.

7. The values can be of any data type.

8. Keys can't be of type list or dictionary. values can be.

"""

# Creating a Dictionary

"""
Syntax:
d = {
    <key_1>: <value_1>,
    <key_2>: <value_2>,
      .
      .
      .
    <key_k>: <value_k>
}
"""

course_details = {
	"title": "Python for absolute beginners",
	"duration": "5hrs",
	"rating": 5,
	"price": None,
	"rating": 5.5
}

# wrong_dict = {
# 	[1, 2, 3]: "nums"
# }

tuple_as_a_key = {
	(1, 2, 3): "nums"
}

# print(tuple_as_a_key)


"""
Syntax:
d = dict([
    (<key_1>, <value_1>),
    (<key_2>, <value_2>),
      .
      .
      .
    (<key_k>, <value_k>)
])
"""

marks = dict([
	("suresh", 90),
    ("rakesh", 87),
    ("Anish", 78),
    ("rahul",  95) 
])
# print(marks)

# Accessing values

# print(marks[0]) # wrong
# print(marks["suresh"])
# print(marks["Rakesh"]) # wrong


# Bonus

int_key = {
	0: 'A',
	1: 'B',
	2: 'C',
	3: 'D',
	4: 'E'
}
# print(int_key[0])


any_key = {
	"abc": "string",
	10: "integer",
	0.5: "float",
	(1, 2, 4): "tuple",
	True: "boolean",
	None: "null"
}
# print(any_key)


# Bonus

types_key = {
	int: 89,
	float: 8.6,
	str: "hello",
	list: [1, 2, 3],
	tuple: (2, 3, 5),
	dict: {
		'a': 'A',
		'b': 'B',
	},
	bool: False
}
print(types_key)
