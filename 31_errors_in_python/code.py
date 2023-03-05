def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor



Student = [
    {"name":"Bob", "grades": [99,33,86,98,100]},
    {"name":"Rolf", "grades": []},
    {"name":"Sarah","grades": [98,78,45,87,99]},
]

print("Welcome to the average grade program. ")
try:
    for students in Student:
        name = students["name"]
        grades = students["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}. ")
        
except ZeroDivisionError as e:
    print("ERROR: {name} has no grades yet in the list.")
else:
    print("All the student average is calculated.")
finally:
    print("End of student average calculation.")