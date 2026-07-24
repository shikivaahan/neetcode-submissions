class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        needed = defaultdict(int)
        left = 0

        for s in s1:
            needed[s] += 1
        
        for right, char in enumerate(s2):
            left = right - n + 1
            if char in needed:
                needed[char] -= 1

            if all(value == 0 for value in needed.values()):
                return True

            if left >= 0:
                if s2[left] in needed:
                    needed[s2[left]] += 1
                
        return False
                
            
                
            

                


        