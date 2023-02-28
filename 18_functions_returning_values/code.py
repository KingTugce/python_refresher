def add(x,y):
    print(x + y)

add(5 , 8)
result = add(5 , 8)
print(result)

# it runs none because first it reads inside of the paranthesis thats why
# we use "return" instead of "print(result)"

def add(x, y):
    return x + y

add(5, 8)
result = add(5, 8)
print(result)

# "return" function also end the cycle.

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 2) * 5
print(result)