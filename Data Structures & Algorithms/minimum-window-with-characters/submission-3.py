from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        needed = Counter(t)
        missing = len(t)
        left = 0

        shortest_length = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            if char in needed:
                if needed[char] > 0:
                    missing -= 1

                needed[char] -= 1

            while missing == 0:
                length = right - left + 1

                if length < shortest_length:
                    shortest_length = length
                    best_start = left

                if s[left] in needed:
                    needed[s[left]] += 1

                    if needed[s[left]] > 0:
                        missing += 1

                left += 1

        if shortest_length == float("inf"):
            return ""

        return s[best_start:best_start + shortest_length]