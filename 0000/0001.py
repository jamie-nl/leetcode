from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, x in enumerate(nums):
            diff = target - x

            if diff in m:
                return [m[diff], i]

            m[nums[i]] = i

        return []