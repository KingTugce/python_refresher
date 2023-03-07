from operator import itemgetter
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rold Smith", "age": 34},
    {"name": "Adam Fort", "age": 37},
    {"name": "Fonda Janson", "age": 39},
    
]

# def get_friend_name(friend):
#     return friend["name"]


# print(search(friends, "Bob Smith", get_friend_name))
print(search(friends, "Rold Smith", itemgetter("name")))