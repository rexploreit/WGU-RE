def f(plaintext: [int]):
    return plaintext[:: int(True) * -1]


def g(plaintext: str):
    cipher = []
    for l, c in enumerate(plaintext):
        cipher.append(h(plaintext[l], plaintext[(l + 1) % len(plaintext)]))
    return cipher


def h(i, j):
    return ord(i) ^ ord(j)


def authenticate(the_guess, cipher):
    print(the_guess)
    return the_guess == cipher


def main():
    ciphered_text = [101, 2, 0, 0, 29, 97, 26, 19, 9, 97, 120, 18, 16]
    solved = False
    while not solved:
        guess = input("Please enter code: >")
        if authenticate(f(g(guess)), ciphered_text):
            solved = True
    print("You got it!")


if __name__ == "__main__":
    ciphered_text = [101, 2, 0, 0, 29, 97, 26, 19, 9, 97, 120, 18, 16]
    ct = f(ciphered_text)

    out = ""
    pos1 = "W"
    next = 1
    for n in ct:
        while ord(pos1) ^ next != n:
            next += 1
        out += pos1
        pos1 = chr(next)
        next = 1

    print(out)

    main()
