class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = []
        out = []
        for s in range(len(strs)):
            
            alph = sorted(strs[s])
            
            if alph in dic:
                pass
            else: 
                dic.append(alph)
                
                temp = []
                temp.append(strs[s])
                
                for i in range(s + 1, len(strs)):
                    
                    if sorted(strs[i]) == alph:
                        temp.append(strs[i])
                        
                out.append(temp)
                
        return out