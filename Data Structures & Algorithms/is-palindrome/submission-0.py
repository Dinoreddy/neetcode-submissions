class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(cl)-1

        while(i<j):
            if cl[i] != cl[j]:
                return False
            i += 1
            j -= 1
        return True    


        