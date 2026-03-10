
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        output = []
        for i in strs:
            item = []
            for j in strs:
                if sorted(i) == sorted(j):
                    item.append(j)

            if i not in item:
                item.append(i)
            if sorted(item) not in output:
                output.append(sorted(item))
        return output


solution = Solution()
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
