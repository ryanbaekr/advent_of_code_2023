"""Processing for Day 07"""

from collections import Counter

def camel_cards(hands: str, as_wild: bool) -> int:
    """Take the hands and return the appropriate value"""

    hands = (
        hands
        .replace("A", "S")  # ace now has the highest value
        .replace("K", "R")  # king now has the second highest value
        .replace("T", "I")  # ten now has the lowest value
    )

    if as_wild:
        hands = hands.replace("J", "1")

    hand_bid_map = {}

    type_pools = {
         4: [],  # 5 unique - 1 max =  4 (high card)
         2: [],  # 4 unique - 2 max =  2 (one pair)
         1: [],  # 3 unique - 2 max =  1 (two pair)
         0: [],  # 3 unique - 3 max =  0 (three of a kind)
        -1: [],  # 2 unique - 3 max = -1 (full house)
        -2: [],  # 2 unique - 4 max = -2 (four of a kind)
        -4: [],  # 1 unique - 5 max = -4 (five of a kind)
    }

    for line in hands.splitlines():
        hand, bid = line.split(" ")

        hand_bid_map[hand] = int(bid)

        if hand == "11111":
            type_pools[-4].append(hand)
        else:
            temp_hand = hand.replace("1", "")
            kinds = list(Counter(temp_hand).values())
            type_pools[len(kinds) - max(kinds) - len(hand) + len(temp_hand)].append(hand)

    hand_list = []

    for type_pool in list(type_pools.values()):
        hand_list.extend(sorted(type_pool))

    score = 0

    for hand_index, hand in enumerate(hand_list):
        score += (hand_index + 1) * hand_bid_map[hand]

    return score
