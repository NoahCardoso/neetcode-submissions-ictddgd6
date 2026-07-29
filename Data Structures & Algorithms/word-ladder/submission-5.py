from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = dict()

        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        for word in wordList:
            adj[word] = set()
        for word1 in wordList:
            for word2 in wordList:
                if word2 in adj[word1]:
                    continue
                if self.one_char_difference(word1,word2):
                    adj[word1].add(word2)
                    adj[word2].add(word1)
        ### bfs
        q = deque()
        q.append(beginWord)
        seen = set()
        parent = dict()
        parent[beginWord] = None
        complete = False
        seen.add(beginWord)
        while q:
            node = q.popleft()
            if node == endWord:
                complete = True
            for nei in adj[node]:
                if nei not in seen:
                    parent[nei] = node
                    q.append(nei)
                    seen.add(nei)
        if complete:
            count = 1
            c = endWord
            print(parent)
            while parent[c] != None:
                count += 1
                c = parent[c]
            return count
        return 0


    def one_char_difference(self,s1: str, s2: str) -> bool:
        differences = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                differences += 1
                if differences > 1:
                    return False

        return differences == 1