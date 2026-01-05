from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        patterns = defaultdict(list)
        L = len(beginWord)

        for word in wordSet:
            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                patterns[pat].append(word)

        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                for nxt in patterns[pat]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, dist + 1))
                patterns[pat] = []  # optimization to avoid repeats

        return 0
