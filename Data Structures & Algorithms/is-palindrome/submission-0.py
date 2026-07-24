class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()
         
        i = 0
        while i < len(string):
            if string[i] == string[-(i+1)]:
                i += 1
                continue
            else:
                return False
            
        return True

        