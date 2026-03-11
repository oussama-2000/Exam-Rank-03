# make a dict with key(array item): value(how many times repeated on the array)
# sort the dict by the values , reversed
# store the dict keys on a list
# return the output as a slicing ,exactly the k number of items

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        info = {}

        for i in nums:
            info[i] = nums.count(i)

        info = dict(sorted(info.items(), key=lambda a: a[1], reverse=True))
        out = [k for k in info.keys()]
        return out[:k]


solution = Solution()
print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))
