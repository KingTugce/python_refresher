def add(x , y):
    return x + y

nums = [3 , 5]
print(add(*nums))        
# call the function with "*" so it can pass one value for each arguments(3,5)