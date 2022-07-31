"""ported from ruby levl01"""

def recursive(r):
    if len(r) == 1:
        return not_actually_recursive(r[0])
    else:
        return recursive(r[1 : len(r)]) + not_actually_recursive(r[0])


def not_actually_recursive(r):
    if r - 2 < 0:
        return [r]
    return super_recursive(~r & 0xFF)


def super_recursive(r, o=[], e=7):
    if len(o) == 8:
        return [int("".join([str(x) for x in recursive(o)]), 2)]
    if r < 2 ** e:
        o.append(0)
        super_recursive(r, o, e - 1)
    else:
        o.append(1)
        super_recursive(r - 2 ** e, o, e - 1)


if __name__ == "__main__":
    m = [89, 137, 9, 221, 251, 201, 201, 89, 21]
    print("".join([chr(c) for c in recursive(m)]))
