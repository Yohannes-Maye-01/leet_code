class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)  
        longest_nice_substring = '' 

      
        for i in range(n):
            lower_case_flags = 0  
            upper_case_flags = 0 

           
            for j in range(i, n):
                if s[j].islower():
                  
                    lower_case_flags |= 1 << (ord(s[j]) - ord('a'))
                else:
                    
                    upper_case_flags |= 1 << (ord(s[j]) - ord('A'))

               
                if lower_case_flags == upper_case_flags and len(longest_nice_substring) < j - i + 1:
                   
                    longest_nice_substring = s[i : j + 1]

        return longest_nice_substring

        