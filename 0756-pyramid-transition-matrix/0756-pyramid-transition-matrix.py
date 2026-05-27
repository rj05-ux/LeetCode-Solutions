from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        
        mapping = defaultdict(list)
        for pattern in allowed:
            mapping[(pattern[0], pattern[1])].append(pattern[2])
        
        
        def build(currentRow, nextRow, index):
            
            
            if len(currentRow) == 1:
                return True
            
            
            if index == len(currentRow) - 1:
                return build(nextRow, "", 0)
            
           
            left = currentRow[index]
            right = currentRow[index + 1]
            
           
            for top in mapping[(left, right)]:
                if build(currentRow, nextRow + top, index + 1):
                    return True
            
            
            return False
        
        
        return build(bottom, "", 0)