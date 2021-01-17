# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. You can return the output in any order.

 

# Example 1:

# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: S = "3z4"
# Output: ["3z4","3Z4"]
# Example 3:

# Input: S = "12345"
# Output: ["12345"]
# Example 4:

# Input: S = "0"
# Output: ["0"]

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 1:
            if S.isupper() or S.islower():
                return [S.upper(), S.lower()]
            else:
                return [ S ]
        llist = self.letterCasePermutation(S[1:])
        new_list = []
        for _ in range(len(llist)):
            x = llist.pop()
            if S[0].isupper() or S[0].islower():
                new_list.append((S[0].upper())+x)
                new_list.append((S[0].lower())+x)
            else:
                new_list.append(S[0]+x)
        return new_list