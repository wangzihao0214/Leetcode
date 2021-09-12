class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())

#         result = []
#         dics = []
        
#         for ele in strs:
#             dic_ele = {}
#             for i in range(len(ele)):
#                 dic_ele[ele[i]] = dic_ele.get(ele[i], 0) + 1
#             same = False
#             for i in range(len(dics)):
#                 if dic_ele == dics[i]:
#                     result[i].append(ele)
#                     same = True
#                     break
#             if not same:
#                 dics.append(dic_ele)
#                 result.append([ele])
        
#         return result