class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted = ""
        for i in strs:
            encrypted += str(len(i)) + ','
        encrypted += "@"
        for i in strs:
            for j in i:
                encrypted += chr(ord(j) + 1)
        return encrypted

    def decode(self, s: str) -> List[str]:
        secret = s[:s.index("@") - 1].split(',')
        lengths = []
        print(secret)
        for i in secret:
            if i == '':
                return []
            lengths.append(int(i))
        
        rest = s[s.index("@") + 1:]
        result = []
        index = 0

        for i in lengths:
            mini = ""
            for j in range(i):
                mini += chr(ord(rest[index]) - 1)
                index += 1
            result.append(mini)
        return result