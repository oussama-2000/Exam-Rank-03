def alternate_case(string: str) -> str:
    result = ""

    alternate = True
    for c in string:
        if c.isalpha():
            if alternate:
                c = c.upper()
                alternate = False
            else:
                c = c.lower()
                alternate = True
            result += c
        else:
            result += c
    return result


print(alternate_case("hello world!"))
