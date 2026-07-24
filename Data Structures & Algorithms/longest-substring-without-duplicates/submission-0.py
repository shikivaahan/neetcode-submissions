class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0

        for right, char in enumerate(s):
            
            if s[right] not in seen:
                seen.add(char)
                length = right - left + 1
                longest = max(length, longest)
            
            else:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1

                if left != right:
                    left += 1
        
        return longest
            



        
        
        