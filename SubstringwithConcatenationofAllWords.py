class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        concDic = list(permutations(words))
        for i in range(len(concDic)):
            sentence = ""
            for j in range(len(concDic[i])):
                sentence += concDic[i][j]
            concDic[i] = sentence
            
        wordsize = len(concDic[0])
        
        diff = len(s) - wordsize
        out = []
        
               
        for i in range(diff):
            if s[i:i+wordsize] in concDic:
                out.append(i)
        
        return(out)