# Order hands of cards, introducing jokers that can change hand types to a better one

import sys
from enum import Enum
from itertools import groupby

LABEL_ORDER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
class HandType(Enum):
    FIVE = 1
    FOUR = 2
    FULL_HOUSE = 3
    THREE = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    SINGLE = 7

def identify_type(hand_string):

    joker_n = hand_string.count('J')
    if joker_n == 5:
        return HandType.FIVE
    hand_string = hand_string.replace('J', '')

    sorted_groups_n = sorted([len(list(label_iter)) for _, label_iter in groupby(sorted(hand_string))], reverse=True)
    if sorted_groups_n[0] == 5 - joker_n:
        return HandType.FIVE
    if sorted_groups_n[0] == 4 - joker_n:
        return HandType.FOUR
    if sorted_groups_n[0] == 3 - joker_n:
        if sorted_groups_n[1] == 2:
            return HandType.FULL_HOUSE
        return HandType.THREE
    if sorted_groups_n[0] == 2 - joker_n:
        if sorted_groups_n[1] == 2:
            return HandType.TWO_PAIR
        return HandType.ONE_PAIR
    return HandType.SINGLE


hand_list = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        l = line.split()
        hand_list.append((l[0], identify_type(l[0]), int(l[1])))

def sort_hand_key(hand):
    hand_string, hand_type, bid = hand
    return (hand_type.value, [LABEL_ORDER.index(card) for card in hand_string])
sorted_hand_list = sorted(hand_list, key=sort_hand_key, reverse=True)

sorted_bid_list = [bid for _, _, bid in sorted_hand_list]
total = sum([(i+1)*bid for i, bid in enumerate(sorted_bid_list)])
print(total)
