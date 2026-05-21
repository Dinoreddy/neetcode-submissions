class Solution:

    def encode(self, strs: List[str]) -> str:
        res= []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return str("".join(res))

    def decode(self, s: str) -> List[str]:

        res , i = [] , 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j+=1

            lenght = int(str(s[i:j]))

            res.append(s[j+1 : lenght + j + 1])

            i = lenght + j + 1

        return res

      


