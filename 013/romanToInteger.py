class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        checkMinus = False
        for i in range(len(s)):
            if checkMinus:
                checkMinus = False
                if s[i - 1] == 'I':
                    if s[i] == 'V':
                        num += 3
                        continue
                    elif s[i] == 'X':
                        num += 8
                        continue
                elif s[i - 1] == 'X':
                    if s[i] == 'L':
                        num += 30
                        continue
                    elif s[i] == 'C':
                        num += 80
                        continue
                elif s[i - 1] == 'C':
                    if s[i] == 'D':
                        num += 300
                        continue
                    elif s[i] == 'M':
                        num += 800
                        continue
                
            if s[i] == 'I':
                num += 1
                checkMinus = True
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'X':
                num += 10
                checkMinus = True
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'C':
                num += 100
                checkMinus = True
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'M':
                num += 1000
            else:
                print("Something wrong...")
                    
        
        return num       
 
