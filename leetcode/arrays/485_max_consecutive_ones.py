def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    for i in nums:
        if i == 1:
            count += 1
            print('count = ', count)
            if max_count < count:
                max_count = count
                print('max_count = ', max_count)
        elif i == 0:
            count = 0
    print(max_count)

nums = [1,1,0,1,1,1]
findMaxConsecutiveOnes(nums)

# Time Complexity: O(n) because we iterate once the array
# Space Complexity: O(1) because we don't use any extra space