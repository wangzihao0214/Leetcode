class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def DFS(path, index):
            if index == len(s):
                res.append(path)
                return
            if s[index].isdigit():
                DFS(path + s[index], index+1)
            else:
                if s[index].islower(): # 小写转大写
                    DFS(path + s[index].upper(), index+1)
                else:
                    DFS(path + s[index].lower(), index+1)
                DFS(path + s[index], index+1)
                
        res = []
        DFS("", 0)
        return res