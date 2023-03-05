def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor


# this value operator turn into a function:
def calculate(*values, operator):
    return operator(*values)


# we normally call a funtion adding "()" but this time sadece esitliyoruz. operator = divide ayni sey oluyor.
result = calculate(20,4, operator=divide)
print(result)

