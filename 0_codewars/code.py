def positive_sum(arr):
    print(arr)
    nums = []
    for num in arr:
        if sum(num) >= 0:
            nums.append(arr)
            return num
        
        else:
            return 0
num = [3,5,6]
print(positive_sum(num))