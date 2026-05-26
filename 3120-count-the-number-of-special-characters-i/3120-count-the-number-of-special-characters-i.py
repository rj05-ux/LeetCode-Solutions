class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        import string 
        count = 0
        for letter in string.ascii_lowercase:
            found_lower = False
            found_upper = False
            for char in word :
                if char == letter:
                     found_lower = True
                if char == letter.upper():
                    found_upper = True

            if found_lower and found_upper:
                            count += 1
        return count