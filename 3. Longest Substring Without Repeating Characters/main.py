class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        temp = 0
        left = 0
        right = 1
        n = len(s)

        if n == 0:
            return 0

        for left in range(n):
            right = left + 1
            if left + result > n - 1:
                return result
            while right < n and s[right] not in s[left: right]:
                right += 1
            temp = right - left
            if result < temp:
                result = temp
        return result

        # if n == 1:
        #     return 1
        # dic = {}
        # dic[s[left]] = left
        # while right < n:
        #     if s[right] in dic and dic[s[right]] != right and dic[s[right]] >= left:
        #         temp = right - left
        #         left = dic[s[right]] + 1
        #         dic[s[right]] = right
        #     else:
        #         temp = right - left + 1
        #         dic[s[right]] = right
        #         right += 1
        #     if temp > result:
        #             result = temp
        # return result