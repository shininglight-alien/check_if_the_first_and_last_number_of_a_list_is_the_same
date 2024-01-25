# Check if the first and last number of a list is the same

def check_first_last(nums):
    first_num = nums[0]
    last_num = nums[-1]
    result = first_num == last_num
    return first_num, last_num, result

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

first_num, last_num, result = check_first_last(numbers_x)
print(f"For the Given x = {numbers_x}, First Number: {first_num}, Last Number: {last_num}, Same: {result}")

first_num, last_num, result = check_first_last(numbers_y)
print(f"For the Given y = {numbers_y},First Number: {first_num}, Last Number: {last_num}, Same: {result}")