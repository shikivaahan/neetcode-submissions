class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        length = 0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                length = max(right - left + 1, length)
            
            else:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                
                left += 1
        
        return length

        