class Solution:
    def defangIPaddr(self, address: str) -> str:
        f_string = address.replace('.', '[.]')

        return f_string