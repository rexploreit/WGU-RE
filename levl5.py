from textwrap import dedent
from base64 import b64decode


def do_nothing():
    # why is this here?
    pass


def obscure_a():
    s = "Ｈｆｇｄ＂ｏｃｋｌ＊ｅ＋８Ｈ＂＂＂＂ｋｄ＂ｅ＂？？＂＀ｹ：５．＂５３．＂：７．＂６７．＂５：．＂５；．＂：２\
．＂４；．＂６７．＂６；．＂７２．＂７３．＂７０ｿ＀８＂ｒｐｋｌｖ＊＀ｪｃｔｇ＂｛ｍｗ＂ｖｐｋｇｆ＂ｆｇａｍｆｋ\
ｌｅ＂ｃ＂ｃｌｆ＂｀＝＀＋Ｈ＂＂＂＂ｇｎｑｇ８＂Ｈ＂＂＂＂＂＂＂＂ｑ＂？＂ｹ：５．＂５３．＂：７．＂６７．＂４\
；．＂：：．＂４；．＂４５．＂６７．＂６；．＂６：．＂７０．＂７２ｿＨ＂＂＂＂＂＂＂＂ｋｄ＂ｹｍｐｆ＊ａ＋＂ｄ\
ｍｐ＂ａ＂ｋｌ＂ｅｿ＂？？＂ｑ８Ｈ＂＂＂＂＂＂＂＂＂＂＂＂ｒｐｋｌｖ＊＀ｻｍｗ＂ｅｍｖ＂ｋｖ＀＋Ｈ＂＂＂＂＂＂＂\
＂ｇｎｑｇ８Ｈ＂＂＂＂＂＂＂＂＂＂＂＂ｒｐｋｌｖ＊＀ｶｐ｛＂ｃｅｃｋｌ＀＋Ｈ"
    return "".join([chr((~ord(c) & 0xFFFF) ^ 221) for c in s])


def obscure_b():
    return b64decode("ZGVmIGRvX25vdGhpbmcoKTogZXhlYyhhLCBnbG9iYWxzKCkp")


def main(guess):
    solution = [87, 71, 85, 45, 78, 79, 80, 69, 45, 49, 50, 51, 52]
    if guess == solution:
        print("You got it")
    else:
        print("Try again")


a = dedent(obscure_a())
b = obscure_b()

eval(compile(b, "", "exec"))

if __name__ == "__main__":
    do_nothing()
    guess = input("flag > ")
    main(guess)
