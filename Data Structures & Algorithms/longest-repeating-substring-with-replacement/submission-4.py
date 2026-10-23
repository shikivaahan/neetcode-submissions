class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        longest = 0
        max_freq = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            length = right - left + 1
            longest = max(longest, length)
        
        return longest
        

        
        