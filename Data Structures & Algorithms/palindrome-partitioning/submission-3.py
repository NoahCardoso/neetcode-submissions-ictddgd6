class Solution:
    def partition(self, s: str) -> List[List[str]]:
        paths = []
        
        def valid(s):
            if s and s != "":
                s = s.lower().replace(" ", "")
                return s == s[::-1]
            return False

        def backtrack(index, path):
            if index >= len(s):
                if "".join(path) == s:
                    paths.append(path.copy())
            
            string = ""
            for i in range(index,len(s)):
                string += s[i]
                
                if valid(string):
                    path.append(string)
                    backtrack(i+1,path)
                    path.pop()
        backtrack(0,[])
        return paths

        