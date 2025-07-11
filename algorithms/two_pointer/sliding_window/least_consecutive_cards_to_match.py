# A bunch of cards is laid out in front of you in a line, where the value of each
# card ranges from 0 to 10^6. A pair of cards is matching if they have the same number value.
# Given a list of integers cards, your goal is to match a pair of cards, but you can only
# pick up cards in a consecutive manner. What's the minimum number of cards that you need to
# pick up to make a pair? If there are no matching pairs, return -1.
# 
# For example, given cards = [3, 4, 2, 3, 4, 7], then picking up [3, 4, 2, 3] makes a
# pair of 3s and picking up [4, 2, 3, 4] matches two 4s. We need 4 consecutive cards to match
# a pair of 3s and 4 consecutive cards to match 4s, so you need to pick up at least 4 cards to make a match.

def least_consecutive_cards_to_match(cards):
    left = 0
    window = set()
    min_length = len(cards) + 1

    for right in range(len(cards)):
        while cards[right] in window:
            min_length = min(min_length, right - left + 1)
            window.remove(cards[left])
            left += 1
        window.add(cards[right])

cards = [3, 4, 2, 3, 4, 7]

print(least_consecutive_cards_to_match(cards))