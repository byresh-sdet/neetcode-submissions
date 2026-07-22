class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen= len(s)
        tlen= len(t)
        count = {}
        if slen != tlen:
            return False
        for ch in s:
            if ch in count:
                count[ch] +=1
            else:
                count[ch] =1
        
        for ch in t:
            if ch in count:
                count[ch] -=1
                if count[ch] < 0:
                    return False
            else :
                return False
        return True
        
        

        

        