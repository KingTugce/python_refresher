# **by the way, there no ways adding and removing elements from tuples.Tuples are immutable*
# immutable things are, tuples, strings,integers,floats and booleans..All the rest are mutable.
#  "a" and "b" 's are names, a value is the list after "=" 
a = []
b = a

a.append(35)
print(a)
print(b)

# id will give location of them
print(id(a))
print(id(b))


# python doesnt create the same lists twice. So id will remain the same.
a = 3456
b = 3456

print(id(a))
print(id(b))


a = "hello"
b = a

print(a)
print(b)

# This is basically:  'a = a + "world" '
a += "world"

