from typing import List
from collections import defaultdict, deque
#array[start:end:step]
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord and endWord not in wordList:
            return 0
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                tf = word[:i] + "*" + word[i + 1:]  # transform
                # print(tf)
                
        # hot -> *ot, h*t, ho*t
        
                graph[tf].append(word)
                # print(graph)
        queue = deque([(beginWord, 1)])
        
        visited = set()
        
        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            
            visited.add(word)
            
            for i in range(len(word)):
                tf = word[:i] + "*" + word[i+1:]
                
                potential_words = graph.get(tf,None)
                
                if potential_words:
                    for potential_word in potential_words:
                        if potential_word not in visited:
                            queue.append((potential_word, distance + 1))
                            visited.add(potential_word)
                            
                            
        return 0 # If no transformation is possible    
                        
            


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))
