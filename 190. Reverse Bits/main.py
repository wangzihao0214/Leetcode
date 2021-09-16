class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))[2:]
        length =len(n)
        if length < 32:
                n = "0" * (32 - length) + n
        result = 0
        
        for i in range(32):
            result += int(n[i]) * (2**i)

        return result