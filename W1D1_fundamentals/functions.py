"""
Python Functions
"""
# what is a function?
# it's a block of code that's excuted once invocked
# a set of instructions
# it could take parameters
#! ALL functions ALWAYS RETURN seomthing

# print(print("hello"))


# verbs
def greeting():
    print("hello sam")


# invoke the function
# greeting()


# parameters
def say_hello(name):
    return f"hello {name}"


result = say_hello("Morphes")
# print(result)


def say_times(times, name):
    for i in range(times):
        if i <= 3:
            print(f"hello {name}")


# say_times(5, "bob")


# ---- default parameters and named arguments


def say_times2(name, times):
    print(times, name)


# say_times2("bob", 3)


# Countdown
def countdown(num):
    list = []
    for index in range(num, -1, -1):
        list.append(index)
    return list


# print(countdown(10))


# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"},  # index 0
    {"first": "Alan", "last": "Turing"},  # index 1
    {"first": "Eric", "last": "Idle"},  # index 2
]


def loop_over_list(some_list):
    for item in some_list:
        print(item["first"])


# loop_over_list(users)


# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies": ["rock climbing", "knitting"],
}


# print(resume_data["languages"][0])


print("hello")
print("*" * 10)
print("hello")
