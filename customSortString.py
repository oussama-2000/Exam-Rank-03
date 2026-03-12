ar = [
    "Apple",
    "bZPLE",
    "BZPLE",
    "chor"
]


def custom_sort(arr: list) -> list:

    return sorted(arr, key=(lambda i: (len(i), i, sum(
        [1 for c in i if c.lower() in "ouaie"]
    ))))


print(custom_sort(ar))
