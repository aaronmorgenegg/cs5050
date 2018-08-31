#!/usr/bin/env python3

# Aaron Morgenegg, A02072659
# 3 heap NIM game, where the person to take the last stone loses

piles = (1,2,1) # Piles A, B, C

win_cache = {}

def Win(piles):
    try: # Return memoized value, if possible
        return win_cache[piles]
    except KeyError:
        pass

    # Simple Cases
    if sum(piles) == 1:  # If there is 1 stone left, you lose
        win_cache[piles] = False
        return False
    if sum(piles) == 2: # If there are 2 stones left, you win by taking 1
        win_cache[piles] = True
        return True 
    for pile, index in enumerate(piles): # For each pile,
        for i in range(pile): # try removing stones until you find the right number of stones to remove to win
            A = piles[0]
            B = piles[1]
            C = piles[2]
            if index == 0: A -= pile
            elif index ==1: B -= pile
            else: C -= pile
            simpler_pile = (A, B, C)
            if not Win(simpler_pile): 
                win_cache[piles] = True
                return True
    win_cache[piles] = False
    return False

print(Win(piles))

