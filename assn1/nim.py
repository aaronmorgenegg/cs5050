#!/usr/bin/env python3

# Aaron Morgenegg, A02072659
# 3 heap NIM game, where the person to take the last stone loses

piles = [4,2,5] # Piles A, B, C

def Win(piles):
    if sum(piles) == 1: return False # If there is 1 stone left, you lose
    if sum(piles) == 2: return True # if there is 2 stones left, take 1 and force the opponent to lose

print(Win(piles))

