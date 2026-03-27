
def rotateList(li: list, k: int) -> list:
    print(li[-k:])
    print(li[:-k])
    rotated = li[-k:] + li[:-k]
    return rotated


print(rotateList([1, 2, 3, 4], 2))
