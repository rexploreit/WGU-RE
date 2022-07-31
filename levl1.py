def test(guess):
    if (
        guess
        == "".join(
            [
                chr(o ^ i)
                for i, o in enumerate(
                    [49, 49, 50, 51, 41, 73, 80, 66, 68, 36, 95, 76, 91]
                )
            ]
        )[::-1]
    ):
        return 1
    return 0


if __name__ == "__main__":
    password = input("What is the password?\n")
    print("Correct!!" if test(password) else "Please try again")

