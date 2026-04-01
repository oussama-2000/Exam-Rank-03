

# def convert_base(n: str, base_from: int, base_to: int) -> str:

#     to_dicemal = int(n, base_from)

#     if (base_to == 10):
#         return str(to_dicemal)

#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = ""

#     while (to_dicemal > 0):
#         result = digits[to_dicemal % base_to] + result
#         to_dicemal = to_dicemal // base_to

#     if result == "":
#         return "0"

#     return result


# "1010"
# print(convert_base("42", 10, 16))   # -2A


# chat
def convert_base(n: str, base_from: int, base_to: int) -> str:

    # handle sign
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
        result = digits[to_dicemal % base_to] + result
        to_dicemal //= base_to

    if result == "":
        return "0"

    return sign + result
