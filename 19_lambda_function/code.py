def double(x):
    return x * 2



sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# doubled = [(lambda x: x * 2)(x) for x in sequence]
# doubled = list(map(double, sequence))

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)

# "Map" does go over each value of the sequence such as list, tuples, sets
# and applies to double function on each element then return the final sequence
