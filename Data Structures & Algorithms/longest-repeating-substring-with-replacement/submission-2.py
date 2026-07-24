class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        longest = 0

        for right, char in enumerate(s):
            freq[char] += 1
            top_freq = max(freq.values())

            while (right - left + 1) - top_freq > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            length = right - left + 1
            longest = max(length, longest)
        
        return longest


            

        