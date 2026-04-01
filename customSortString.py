ar = [
    "Apple",
    "bZPLE",
    "BZPLE",
    "chor"
]


def custom_sort(arr: list) -> list:

    return sorted(arr, key=(lambda i: (len(i), i.lower(), sum(
        [1 for c in i if c.lower() in "ouaie"]
    ), ar.index(i))))


print(custom_sort(ar))
