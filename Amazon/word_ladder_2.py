from _collections import defaultdict
import string
def findLadders(beginWord: str, endWord, wordList):
    s = set(wordList)
    if endWord not in s:
        return []
    forward, backward = {beginWord}, {endWord}  # set([beginWord]), set([endWord])
    direc, parents = 1, defaultdict(set)

    while forward and backward:
        if len(forward) > len(backward):
            forward, backward = backward, forward
            direc *= -1
        s -= forward
        next_forward = set()

        for word in forward:
            for i in range(len(word)):
                p1, p2 = word[:i], word[i + 1:]
                for c in string.ascii_lowercase:
                    t = p1 + c + p2
                    if t in s:
                        next_forward.add(t)
                        if direc == 1:
                            parents[t].add(word)
                        else:
                            parents[word].add(t)
        if backward & next_forward:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[p] + r for r in res for p in parents[r[0]]]
            return res
        forward = next_forward
    return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord,endWord,wordList))
