class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        to_letters = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        paths = []
        def backtrack(d,path):
            if d >= len(digits):
                paths.append(path)
                return
            
            for c in to_letters[digits[d]]:
                path += c
                backtrack(d+1,path)
                path = path[:len(path)-1]
        if len(digits) > 0:
            backtrack(0,"")
        
        return paths
