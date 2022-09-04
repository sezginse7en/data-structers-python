class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isWE = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def getInsertPosition(self,key):
        return ord(key) - ord('a')

    def insert(self,key):

        current = self.root

        for i in range(len(key)):
            
            pos = self.getInsertPosition(key[i])
            if not current.children[pos]:
                current.children[pos] = TrieNode()
            current = current.children[pos]
        
        current.isWE = True
    
    def search(self,key)->bool:

        current = self.root

        for i in range(len(key)):

            position = self.getInsertPosition(key[i])
            if current.children[position] is None:
                return False
            current = current.children[position]
        
        return current.isWE


keys = ["the","a","there","anaswe","any",
            "by","their"]
output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
t = Trie()
 
    # Construct trie
for key in keys:
    t.insert(key)
 
    # Search for different keys
print("{} ---- {}".format("the",output[t.search("the")]))
print("{} ---- {}".format("these",output[t.search("these")]))
print("{} ---- {}".format("their",output[t.search("their")]))
print("{} ---- {}".format("thaw",output[t.search("thaw")]))