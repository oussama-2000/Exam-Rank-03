
def convert_base(n: str, base_from: int, base_to: int) -> str:

    sign = ""
    if n[0] == '-':
        sign = "-"
        n = n[1:]

    to_dicemal = int(n, base_from)

    if base_to == 10:
        return sign + str(to_dicemal)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while to_dicemal > 0:
        result += digits[to_dicemal % base_to]
        to_dicemal //= base_to

    if result == "":
        return "0"

    return sign + result
