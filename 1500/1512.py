from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_map = {}

        count = 0

        for num in nums:
            count += num_map.get(num, 0)
            num_map[num] = num_map.get(num, 0) + 1
        
        return count