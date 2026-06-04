class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            digits = [int(d) for d in str(n)]
            if len(digits) < 3:
                return 0
            
            count = 0
            # Only check middle digits (not first or last)
            for i in range(1, len(digits) - 1):
                left  = digits[i - 1]
                curr  = digits[i]
                right = digits[i + 1]
                
                if curr > left and curr > right:   # Peak
                    count += 1
                elif curr < left and curr < right: # Valley
                    count += 1
            
            return count
        
        total = 0
        for num in range(num1, num2 + 1):
            total += waviness(num)
        
        return total