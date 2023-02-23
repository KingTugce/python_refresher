numbers = [1,3,5]
doubled = [x * 2 for x in numbers]

# for num in numbers:
#     doubled.append(num * 2)


friends = ["rolf", "sam", "samantha", "saurabh", "jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)
