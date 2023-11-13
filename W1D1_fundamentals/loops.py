"""
Python LOOPS
"""


# For Loops

# ? for _iterator_ in _collection_ :

# range() a function that returns a squence of  numbers

# range(start, stop, step)
# start --- inclusive, optional - default 0
# stop --- Exclusive, required
# step --- optional, increment value(-/+)


# 1-10
# for i in range(1, 10 + 1):
#     print(i)

# 1-10 every 2
# for x in range(1, 11, 2):
#     print(x)

# 100 -1 down by 20
# for y in range(100, -1, -20):
#     print(y)


# x = 10
# y = 20

# for some_var in range(x, y + 1):
#     print(some_var)

# for letter in "Hello":
#     print(letter)


# for index, letter in enumerate("Hello"):
#     print(f"{index} => {letter}")


list_name = ["Ben", "Amy", "Joe", "Lucas"]

# for username in enumerate(list_name):
#     print(username)
#
car1 = {"brand": "Tesla", "plate_number": "qs6d8f453qs1", "color": "red"}
car2 = {"brand": "Lexus", "plate_number": "99999999", "color": "white"}


# loop over dict
# for bob in car1:
#     print(f"key = {bob} and the value is -> {car1[bob]}")


# print(car1["color"])

# for val in car2.values():
#     print(val)

# for k in car2.keys():
#     print(k)

# for k, v in car1.items():
#     print(k, v)


names = ["bob", "brown", "ben", "becky"]

names[0] = "unicorn"

username = "Alice"
username[0] = "P"
print(username)
