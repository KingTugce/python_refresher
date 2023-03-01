# the first prepare a list with tuples
users= [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longpssw"),
    (3, "username", "1245"),
]

# and then use dictionary comprehensionnnn oooooohhhh 


# "user[1]" means the first list with all the tuples in it:
username_mapping = {user[1]: user for user in users }


# '["Bob"]' pulls just Bob's information
# print(username_mapping["Bob"] )


#  if l don't use mapping like upward infos than :
# for user in users:
#     if user[1] == "Bob":
#         print(user)


#  if l want to users to login than l ask them using "input":

username_input = input("What is your username? ")
password_input = input("Enter your password: ")


# This way unpackage it/ destructure it into this 3 variables:
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")




