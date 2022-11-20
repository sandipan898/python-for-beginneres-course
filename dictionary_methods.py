user = {
    "username": "sandipan",
    "email": "sandipan@mail.com",
    "firstname": "Sandipan",
    "lastname": "Das",
    "role": "Admin",
    "password": "something secret"
}

"""
clear()
Syntax: dictionary_name.clear()
"""
# user.clear()

"""
copy()
Syntax: dictionary_name.copy()
"""
# duplicated_user = user.copy()

"""
fromkeys()
Syntax: dictionary_name.fromkeys(sequence, value)
"""
# keys = ("k1", "k2", "k3", "k4", "k5")
# generated_dict = dict.fromkeys(keys, 10)

"""
get()
Syntax: dictionary_name.get(keys, default)
"""
# uname = user.get("username")
# is_active = user.get("is_active", "property not found")

"""
items()
Syntax: dictionary_name.items()
"""
# item_list = list(user.items())
# print(item_list)

"""
keys()
Syntax: dictionary_name.keys()
"""
# print(user.keys())

"""
pop()
Syntax: dictionary_name.pop(key)
"""
# print(user.pop("username"))

"""
popitem()
Syntax: dictionary_name.popitem()
"""
# print(user.popitem())

"""
setdefault()
Syntax: dictionary_name.setdefault(key, default_value)
"""
# user.setdefault("is_active", True)

"""
update()
Syntax: dictionary_name.update(another_dictionary)
"""
# additionals = {
#     "profession": "software developer",
#     "hobby": "drawing"
# }
# user.update(additionals)

"""
values()
Syntax: dictionary_name.values()
"""
print(list(user.values()))
