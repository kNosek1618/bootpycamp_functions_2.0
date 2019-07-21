

# EXAMPLE OF USING '*args' in function

def sum_all_nums(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5

print(sum_all_nums(4, 6, 8, 3, 4)) # 25

################################################

def sum_all_nums(*args): # using *args
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(4, 6, 8, 3, 4)) # 25

