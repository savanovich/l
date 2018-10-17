import numpy as np

DEBUG = False


def roll_dices(n):
    return np.round(np.random.uniform(1, 6, n)).astype(int)


def play_round(i):
    if DEBUG: print(f'ROUND {i}')

    res1 = roll_dices(5)
    not_scored_n1 = np.sum(res1 != i)

    res2 = roll_dices(not_scored_n1)
    not_scored_n2 = np.sum(res2 != i)

    res3 = roll_dices(not_scored_n2)
    not_scored_n3 = np.sum(res3 != i)

    if DEBUG:
        print('rol1', res1, 5 - not_scored_n1)
        print('rol2', res2, 5 - not_scored_n2)
        print('rol3', res3, 5 - not_scored_n3)
        print(f'result: {5 - not_scored_n3} * [{i}] =', (5 - not_scored_n3) * i, '\n')

    return (5 - not_scored_n3) * i


def play_game():
    total = 0
    # 6 rounds
    for i in range(1, 7):
        res = play_round(i)
        total += res
    if DEBUG: print(f'Total: {total}')
    return total


def run(n):
    return [play_game() for _ in range(n)]


if __name__ == '__main__':
    score = play_game()
    print(score)
    if score >= 42:
        if DEBUG: print('BONUS!')

    # res = run(10000)
    # print(res)