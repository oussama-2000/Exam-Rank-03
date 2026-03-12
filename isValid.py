class Solution:
    def isValid(self, s: str) -> bool:
        opposits = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        brackets = {}

        opens = opposits.keys()
        closes = opposits.values()

        i = 0
        while i < int(len(s) / 2):
            if s[i] in closes:
                return False
            i += 1
        # char = [i for i in s if i in "([{}])"]
        for i in s:
            brackets[i] = s.count(i)

        # print(brackets)

        c = 1
        for k, v in brackets.items():
            if c == int(len(s) / 2):
                break
            if v != brackets[opposits[k]]:
                return False
            c += 1
        # print(brackets)
        # j = 0
        # for i in char:
        #     if i in opposits.keys() and opposits[i] not in char[j:]:
        #         return False
        return True


solution = Solution()
print(solution.isValid("[(])"))
