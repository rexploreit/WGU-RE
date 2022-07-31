from typing import List


def cut(deck: List[str]):
    return deck[len(deck) // 2 :], deck[: len(deck) // 2]


def riffle(second_half: List[str], first_half: List[str]):
    riffled = []
    for i, fh in enumerate(first_half):
        riffled.append(second_half[i])
        riffled.append(fh)
        if len(second_half) > i == (len(first_half) - 1):
            riffled.append(second_half[i + 1])
    return riffled


def shuffle(deck: List[str], num_times: int):
    for i in range(num_times):
        sh, fh = cut(deck)
        deck = riffle(sh, fh)
    return "".join(deck)


correct = "C1GR5--WA3UD2"
solved = False

while not solved:
    guess = input("Please enter Guess > ")
    if shuffle(guess, 3) == correct:
        solved = True
print("You got it!")
