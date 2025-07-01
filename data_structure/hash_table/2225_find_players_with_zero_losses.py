# 2225. Find Players with Zero or One Losses
#
# You are given an integer array matches where matches[i] = [winneri, loseri]
# indicates that the player winneri defeated player loseri in a match.
# 
# Return a list answer of size 2 where:
#
#   answer[0] is a list of all players that have not lost any matches.
#   answer[1] is a list of all players that have lost exactly one match.
#
# The values in the two lists should be returned in increasing order.

def findWinners(matches):
    dict = {}

    for winner, loser in matches:
        dict[winner] = dict.get(winner, 0)
        dict[loser] = dict.get(loser, 0) + 1
    
    zero_lose, one_lose = [], []

    for player, count in dict.items():
        if count == 0:
            zero_lose.append(player)
        if count == 1:
            one_lose.append(player)
    
    return sorted(zero_lose), sorted(one_lose)

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

print(findWinners(matches))
