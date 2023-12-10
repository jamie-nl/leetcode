class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            l_char = s[l]
            r_char = s[r]

            if not l_char.isalnum():
                l += 1
            elif not r_char.isalnum():
                r -= 1
            else:
                if l_char.lower() != r_char.lower():
                    return False
                else:
                    l += 1
                    r -= 1

        return True