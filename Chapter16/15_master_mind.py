from random import randint

def mastermind_game(inp1, inp2, inp3, inp4):

    comp = [randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4)]
    user = [inp1, inp2, inp3, inp4]
    hits = 0
    pseudo_hits = 0

    played = user[:]
    for i, pair in enumerate(zip(comp, user)):
        if pair[0] == pair[1]:
            hits += 1
            played[i] = -1
        elif pair[0] in played:
            pseudo_hits += 1
            played[played.index(pair[0])] = -1

    print(f"Computer played {comp}")

    return hits, pseudo_hits


for _ in range(10):

    user = randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4)
    hits, pseudo_hits = mastermind_game(user[0], user[1], user[2], user[3])
    print(f"User played {user}")
    print(f"{hits} Hits, {pseudo_hits} Pseudo Hits")
