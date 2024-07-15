class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        # Regular expression for a valid number
        pattern = re.compile(r"""
            ^[+-]?                  # Optional sign
            (                       # Start of main group
                (                   # Start of group for decimals
                    \d+(\.\d*)?     # Digits followed by an optional dot and digits
                    |               # OR
                    \.\d+           # A dot followed by digits
                )                   # End of group for decimals
                |                   # OR
                \d+                 # Digits (integer)
            )                       # End of main group
            ([eE][+-]?\d+)?         # Optional exponent
            $                       # End of string
        """, re.VERBOSE)

        # Return if the pattern matches the input string
        return bool(pattern.match(s))



        