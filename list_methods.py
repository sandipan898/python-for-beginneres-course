"""
1. sort()
"""
numbers = [22, 4, 6, 1, 100, 5, 4, 11]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)


"""
2. append()
"""
days = ["Sunday", "Monday", "Tuesday"]
days.append("Wednesday")
# print(days)


"""
3.extend()
"""
days.extend(["Thursday", "Friday", "Saturday"])
# print(days)


"""
4. index()
"""
# print(days.index("Sunday"))
# print(days[0])
nums = [1, 2, 4, 1, 3, 1, 5]
# print(nums.index(1))


"""
5. insert()
"""
nums.insert(4, 10)
print(nums)


"""
6. remove()
"""
nums.remove(10)
print(nums)


"""
7. pop()
"""
nums.pop(1)
print(nums)

data = nums.pop(2)
print(data)
