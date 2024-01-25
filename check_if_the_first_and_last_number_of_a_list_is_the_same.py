# Check if the first and last number of a list is the same

def check_first_last(nums):
    return nums[0] == nums[-1]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(check_first_last(numbers_x))  # Output: True
print(check_first_last(numbers_y))  # Output: False
