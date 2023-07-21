''' Python Functions Challenges'''

# Challenge 1

def sum_to(n):
    sum = 0
    for num in range(1, n + 1):
        sum += num
    return sum
# print(sum_to(6))
# print(sum_to(10))

# Challenge 2
def largest(nums):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num

    return max_num

# print(largest([10, 4, 2, 231, 91, 54]))

# Challenge 3
def occurrences(str1, str2):
    total = 0
    idx = 0
    while idx < len(str1):
        new_idx = str1.find(str2, idx)
        if new_idx == -1:
            break
        total += 1
        idx = new_idx + 1

    return total

# print(occurrences('fleep floop', 'e'))   # returns 2
# print(occurrences('fleep floop', 'p'))   # returns 2
# print(occurrences('fleep floop', 'ee'))  # returns 1
# print(occurrences('fleep floop', 'fe'))  # returns 0


# Challenge 4
def product(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

# print(product(-1, 4))
# print(product(2, 5, 5))
# print(product(4, 0.5, 5))


# BONUS Challenge 

def steps_to_zero(num):
    num = abs(num)
    step = 0
    while True:
        if num == 0:
            return step
        if num % 2 == 0:
            num /= 2
            step += 1
        if num % 2 != 0:
            num -= 1
            step += 1

# print(steps_to_zero(14))
# print(steps_to_zero(100))