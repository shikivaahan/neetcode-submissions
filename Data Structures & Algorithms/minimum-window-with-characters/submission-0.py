class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_length = len(s) + 1
        shortest = ""
        best_length = len(s) + 1
        needed = defaultdict(int)
        left = 0

        for char in t:
            needed[char] += 1

        missing = len(t)
        
        for right, char, in enumerate(s):
            if char in needed:
                if needed[char] > 0:
                    missing -= 1  

                needed[char] -= 1

            while missing == 0:
                length = right - left + 1

                if length < best_length:
                    shortest = s[left:right + 1]
                    best_length = length

                if s[left] not in needed:
                    left += 1
                
                elif needed[s[left]] < 0:
                    needed[s[left]] += 1
                    left +=1

                else:
                    needed[s[left]] += 1
                    missing += 1
                    left += 1
        
        return shortest



            
            
        
                
                
                    
                

                    
                    
            

        