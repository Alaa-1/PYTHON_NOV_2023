# Fundamentals
# this is a comment !

"""
This is a multiline
comment !
"""

# * VARIABLES

# PRIMITIVES

my_float = 3.14
my_name = "Alice"
is_admin = False
my_num = 11

# snake_case

format_string = f"we can inject {my_num} varibale here."
non_format_string = "we cannot inject varibales " + str(my_num) + " this way"
# print(non_format_string)

# ? === COMPOSTIE TYPES ===

# === LISTS 0 indexed
#           0  1  2  3   4  5
num_list = [2, 3, 6, 9, 8, 4]

# print(num_list[4])

# append a number to the list
num_list.append(101)

# remove an element from the end of list
removed = num_list.pop()

# remove with specific index
num_list.pop(0)
# Other methods
num_list.sort()
# print(num_list)
num_list.sort(reverse=True)
# print(num_list)

# print(len(num_list))

# ==== DICTIONARY
# are not indexed
# ? Key - value pairs
# all keys are comma separated
# all keys are strings

dog_dict = {"name": "Spark", "age": 3, "color": "black", "has_owner": False}

# print(dog_dict["name"])
dog_dict["age"] = 4

# remove an item from dict

# dog_dict.pop("age")
# print(dog_dict)

dog_dict2 = {
    "name": "Rex",
    "age": 6,
    "colors": ["black", "brown"],
    "is_a_good_boy": True,
}

# print(dog_dict2["colors"][1])


# muppets = [
#     {"name": "Kermit the Frog", "location": "The swamp. I'm a frog."},
#     {"name": "Miss Piggy", "location": "The green room. Where's my champagne?"},
#     {"name": "Fozzie Bear", "location": "The Comedy Store - tonight at 8!"},
#     {"name": "Gonzo the Great", "location": "Waiting to be shot out of a cannon."},
# ]


# --- TUPLES
# ---- immutable ----
unicorns = (
    1,
    6,
    9,
    8,
)

print(unicorns[0])
# unicorns[0] = 88 # TYPEERROR
