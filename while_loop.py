"""
Indefinite Loop
Definite Loop
"""

"""
while loop

Syntax:

while condition:
    # body of while loop
"""
# count = 0 # 5
# while count < 5: # 5 < 5
#     print("Count:", count) # prints 4
#     count += 1 # count = count + 1

# total = 0 # 0
# num = 1   # 1
# while num <= 10: # 11 <= 10 -> true
#     total += num # total = 3 + 3 = 6
#     num += 1     # num = 3 + 1 = 4
# print("The sum is :", total)

"""
Password matcher
"""
password = "" # hello
while password != "secret": # "secret" != "secret" -> False
    password = input("Enter the password:")
print("Access Granted!")
