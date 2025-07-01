# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers be
# numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Time Complexity O(n^2) because we are using two nested loops to find the two numbers
# Space Complexity O(1) because we are not using any extra space
def twoSum(numbers, target):
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            print("numbers i : ", numbers[i])
            print("numbers j : ", numbers[j])
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
    return 0

# Time Complexity O(n) because we are using two pointers
# Space Complexity O(1) because we are not using any extra space
def twoSum2(numbers, target):
    left, right = 0, len(numbers) - 1
    print(numbers[left])
    print(numbers[right])

    while left < right:
        sum = numbers[left] + numbers[right]
        print("sum : ", sum)
        if sum == target:
            return [left + 1, right + 1]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return 0

numbers = [2, 7, 11, 15]
target = 9

print(twoSum2(numbers, target))