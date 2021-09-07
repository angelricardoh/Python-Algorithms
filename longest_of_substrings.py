class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWord = 0
        
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            hash_map = list()
            hash_map.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in hash_map:
                    break
                else:
                    hash_map.append(s[j])
                    
            if len(hash_map) > maxWord:
                maxWord = len(hash_map)
        
        return maxWord