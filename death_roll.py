

import numpy as np

import time


# #############
# Deathroll custom implementation (dice gambling)
# single shot deathroll is the classic luck one
# multi roll is an addition I made where players can decide to roll multiple times
# runs with the 'play' function
# #############




# single shot deathroll
# first player to 1 loses
# returns winning player id and the value won
def deathroll(value = None, player_names = None):
    
    if player_names == None:
        player_names = ['0', '1']
    
    val = np.random.randint(1000, 10000) if value == None else value
    # val = 1000
    value = val
    print("\n****\n\nDeathroll starts with initial value of " + str(val), end = '')
    a_b = 0 # player indicator
    round_counter = 0
    while val > 1:
        a_b = 1 - a_b # switch player
        input('')
        new_val = np.random.randint(1, val +1)
        print(f'> {player_names[a_b]} rolls {new_val} out of {val}\n{val/new_val:0.2f} x reduction', end = '')
        val = new_val
        round_counter += 1
    
    print(f'\n\n>>>> {player_names[1 - a_b]} wins {value}')
    
    return 1 - a_b, value


# multi shot deathroll
# each roll is replaced by n rolls
# the sum won is multiplied by the nb of rolls per round of the winner
# returns winning player id and the value won
def multiroll_deathroll(value = None, player_names = None):
    
    
    if player_names == None:
        player_names = ['0', '1']
    
    val = np.random.randint(1000, 10000) if value == None else value
    # val = 1000
    value = val
    print("\n****\n\nDeathroll starts with initial value of " + str(val))
    a_b = 0 # player indicator
    player_multiplicator = {k:0 for k in player_names} # to multiply the sum
    player_rounds = {k:0 for k in player_names} # to average the multiplicator
    round_counter = 0
    while val > 1:
        a_b = 1 - a_b # switch player
        nb_rolls = input(f'> {player_names[a_b]} wants to roll _ times out of {val} : ')
        nb_rolls = int(nb_rolls)
        temp_clone_val = val
        player_rounds[player_names[a_b]] += 1
        while nb_rolls >= 1 and val > 1:
            new_val = np.random.randint(1, val +1)
            nb_rolls = nb_rolls - 1
            player_multiplicator[player_names[a_b]] += 1
            print(f'  > {player_names[a_b]} rolls {new_val} out of {val}\n  {val/new_val:0.2f} x reduction', end = '\n\n')
            val = new_val
            time.sleep(0.75)
        print(f'{temp_clone_val/new_val:0.2f} total reduction')
        round_counter += 1
        print(player_multiplicator, round_counter, player_rounds)
    
    won_sum = value * player_multiplicator[player_names[1 - a_b]]/player_rounds[player_names[1 - a_b]]
    
    print(f'\n>>>> {player_names[1 - a_b]} wins {won_sum}')
    
    return 1 - a_b, won_sum


# main wrapping function
# dictionary for the player sums
# 'single' or 'multi' for the play mode
# asks for a value every time 
def play(player_sums = None, multi_or_single = 'single'):
    
    if player_sums == None:
        player_sums = {0:100, 1:100}
    
    player_names = [input(f"player {i} name : ") for i in range(0, 2)]
    for i in range(len(player_names)):
        player_sums[player_names[i]] = player_sums.pop(i)
    
    print("Initial player sums", player_sums)
    
    initial_value = input("initial value (9 digits max): ")
    
    if multi_or_single == 'single':
        winner, won_sum = deathroll(int(initial_value), player_names)
    if multi_or_single == 'multi':
        winner, won_sum = multiroll_deathroll(int(initial_value), player_names)
    
    player_sums[player_names[winner]] += int(won_sum)
    player_sums[player_names[1 - winner]] -= int(won_sum)
    
    print("\nResulting player sums", player_sums)
    
    return player_sums





















