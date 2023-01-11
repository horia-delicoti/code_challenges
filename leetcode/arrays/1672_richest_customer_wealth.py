# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
#
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

def largest(arr):

    # Initialize maximum element
    max = arr[0]

    # Traverse array elements from second and compare every element with current max
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def maximumWealth(accounts):

    # keep track of every customers wealth in an array
    track_of_money = []

    # Traverse grid to get every money of every customer
    for account in accounts:
        
        # Keep track of every customer, one at a time
        counting_money = 0

        # For every money got for one customer, add it in counting_money
        for money in account:
            counting_money += money
        
        # After we got every money for one customer, add value to array to 
        # keep track of all individuals wealth
        track_of_money.append(counting_money)
    return largest(track_of_money)

accounts = [[1,2,3, 2],[3,2,1,3]]
print(maximumWealth(accounts))