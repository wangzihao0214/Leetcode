class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        result = []
        
        if n1 == 0 or n2 == 0:
            return result
        
        pointer1 = 0
        pointer2 = 0
        
        while pointer1 < n1 and pointer2 < n2:
            print(pointer1, pointer2)
            if not(firstList[pointer1][0] > secondList[pointer2][1] or firstList[pointer1][1] < secondList[pointer2][0]):
                left = max(firstList[pointer1][0], secondList[pointer2][0])
                right = min(firstList[pointer1][1], secondList[pointer2][1])
                result.append([left, right])
            
            if firstList[pointer1][1] < secondList[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1
        return result