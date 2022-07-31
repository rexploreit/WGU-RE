def nibble_flip(x):
    return ((0x0F & x) << 4) | (x >> 4)

def rail_fence(text, rails):
    p = 2 * (rails - 1)
    fences = [""] * rails
    for i in range(len(text)):
        if i % p < rails:
            fences[i % p] += text[i]
        else:
            fences[p - (i % p)] += text[i]
    output = ""
    for this_rail in fences:
        output += this_rail
    return output

correct_answer = [117, 149, 210, 131, 116, 210, 244, 37, 19, 19, 85, 85, 99]
solved = False
while not solved:
    guess = input("Please enter code: >")
    step_one = rail_fence(guess, 3)
    step_two = []
    for char in step_one:
        step_two.append(nibble_flip(ord(char)))
    if step_two == correct_answer:
        solved = True
print("You got it!")
