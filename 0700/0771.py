class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0

        for x in list(stones):
            if x in jewels:
                ans += 1

        return ans