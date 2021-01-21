from more_itertools import split_at
grps = split_at(map(str.rstrip, open('d22.txt')), pred=lambda e: e == '')
grps = list(grps)
grp1 = list(map(int, grps[0][1:]))
grp2 = list(map(int, grps[1][1:]))

FIRST_DECK_WON = 0
SECOND_DECK_WON = 1

old_print=print
print=lambda *args: None
def match(grp1, grp2, depth=0):
    memo = set()
    print('Match')
    print('-' * 30)
    round = 1
    while grp1 and grp2:
        print(f'Round {round} (Game {depth + 1})'); round += 1
        print(f"Player 1's deck: {','.join(map(str,grp1))}")
        print(f"Player 2's deck: {','.join(map(str,grp2))}\n")
        if (tuple(grp1), tuple(grp2)) in memo:
            print('Game repeat detected')
            return FIRST_DECK_WON

        if len(grp1) > grp1[0] and len(grp2) > grp2[0]:
            memo.add((tuple(grp1), tuple(grp2)))
            which_deck_won = match(grp1[:][1:1+grp1[0]], grp2[:][1:1+grp2[0]], depth+1)
            print(f"Returning from sub-game {depth+1}")
            print("<" * 30)
            if which_deck_won == FIRST_DECK_WON:
                print(f'Player 1 won sub-game {depth+1}')
                # if player 1 wins, then the order of cards added to player 1's deck
                # is P1's winning card, _then_ P2's losing card
                grp1.append(grp1[0])
                grp1.append(grp2[0])
            else:
                print(f'Player 2 won sub-game {depth+1}')
                grp2.append(grp2[0])
                grp2.append(grp1[0])

        elif grp1[0] < grp2[0]:
            # p2 wins
            memo.add((tuple(grp1), tuple(grp2)))
            grp2.append(grp2[0])
            grp2.append(grp1[0])
        else:
            # p1 wins
            memo.add((tuple(grp1), tuple(grp2)))
            grp1.append(grp1[0])
            grp1.append(grp2[0])
        del grp1[0]
        del grp2[0]

    winner = SECOND_DECK_WON if not grp1 else FIRST_DECK_WON
    return winner

winner = match(grp1, grp2)
winner = grp2 if winner == SECOND_DECK_WON else grp1
pts = sum((len(winner) - pos) * val for pos, val in enumerate(winner))
old_print(pts)
# return (SECOND_DECK_WON if not grp1 else FIRST_DECK_WON), pts