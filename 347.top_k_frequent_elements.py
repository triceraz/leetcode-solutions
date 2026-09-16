from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in frequencies.items():
            buckets[frequency].append(num)

        res = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)

                if len(res) == k:
                    return res
        return res
