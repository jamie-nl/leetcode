class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_string = str(s).lower()
        r_string = f_string[::-1]

        if f_string != r_string:
            return False
        
        return True