# ord
# chr

def shift_string(string: str, k: int) -> str:

    shifted = ""

    for c in string:
        if c.isalpha():
            if c.islower():
                shifted += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
            else:
                shifted += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            shifted += c

    return shifted


print(shift_string("Hello", 1))  # Ifmmp
print(shift_string("xyz", 3))  # Abc
