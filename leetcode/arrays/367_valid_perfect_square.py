# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

def isPerfectSquare(num):
    left,right = 1, num
    if num < 2:
        return True

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == num:
            return True
        if square > num:
            right = mid - 1
        else:
            left = mid + 1

    return False

num = 104976

print(isPerfectSquare(num))

# Time Complexity: O(log n) because we are using binary search to find the square root.
# Space Complexity: O(1) because we are using a constant amount of space.