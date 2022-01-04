class Solution:
    def trap(self, height: List[int]) -> int:
    
        #use of two pointers to indicate the two points of which the water will reside
        length = len(height)
        p = p2 = 0
        dips = []
        while p <= len(height)-2:
            if height[p] > height[p+1]:
                #peak found
                p2 = p + 1
                try:
                    while height[p2] < height[p]:
                        p2 += 1
                    #right peak found
                    dips.append([p, p2])
                    p = p2
                    
                except:
                    p += 1
            else:
                p += 1
        
        #volume determination
        acca = 0
        for d in dips:
            
            #height
            if height[d[0]] < height[d[1]]:
                low = height[d[0]]
            else: low = height[d[1]]
                
            #width
            diff = d[1] - d[0] - 1
            
            maxV = diff * low
            
            #volume taken from elevation
            loss = sum(height[d[0]+1:d[1]])
            
            aV = maxV - loss
            
            acca += aV
                
                
        return acca
                
                
        