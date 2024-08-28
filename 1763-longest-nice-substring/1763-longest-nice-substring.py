class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)  # length of the input string
        longest_nice_substring = ''  # Initialize the longest nice substring

        # Iterate over the string with two pointers
        for i in range(n):
            lower_case_flags = 0  # Bit flags for lowercase letters
            upper_case_flags = 0  # Bit flags for uppercase letters

            # Explore the substring starting from index i
            for j in range(i, n):
                if s[j].islower():
                    # Set the bit corresponding to the lowercase letter
                    lower_case_flags |= 1 << (ord(s[j]) - ord('a'))
                else:
                    # Set the bit corresponding to the uppercase letter
                    upper_case_flags |= 1 << (ord(s[j]) - ord('A'))

                # Check if the current substring is nice (lowercase and uppercase bits match)
                if lower_case_flags == upper_case_flags and len(longest_nice_substring) < j - i + 1:
                    # Update the longest nice substring if the current one is longer
                    longest_nice_substring = s[i : j + 1]

        # Return the longest nice substring found
        return longest_nice_substring

        