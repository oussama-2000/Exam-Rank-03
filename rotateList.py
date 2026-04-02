
# [1, 2, 3, 4] 2 -> [3, 4, 1, 2]
def rotateList(li: list, k: int) -> list:
    for _ in range(k):
        last_item = li.pop()
        li.insert(0, last_item)
    return li


print(rotateList([1, 2, 3, 4], 2))
