class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        return self.check(self.root, word)
    
    def check(self, cur, word):
        #checks if you can construct the string from the current node
        if not word and cur.endOfWord:
            return True
        elif not word:
            return False
        if len(cur.children.keys()) == 0:
            return False
        
        if word[0] == '.':
            if len(word) == 1 and cur.endOfWord:
                return True
            for a in cur.children.values():
                answer = self.check(a, word[1:])
                if answer:
                    return True
            return False
        else:
            if word[0] not in cur.children.keys():
                return False
            cur = cur.children[word[0]]
            if len(word) == 1 and cur.endOfWord:
                return True
            return self.check(cur, word[1:])
