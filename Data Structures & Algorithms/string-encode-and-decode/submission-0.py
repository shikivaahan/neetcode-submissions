class Solution:

    def encode(self, strs: List[str]) -> str:
        
        delimiter = '#'
        secret = ''

        for word in strs:
            secret += str(len(word)) + delimiter + word
        return secret 

    def decode(self, s: str) -> List[str]:
        message = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            message.append(word)
            i = j + 1 + length
        return message
    

                            


             

