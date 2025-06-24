        
# node that contains a letter
class TrieNode:
    def __init__(self):
        self.children = {} # letter derived from array
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Takes each letter in word and instert it in the prefix_tree"""
        # edge case
        if not word:
            return
        
        # create node for first letter
        current_node = self.root
        # add the word, link all children
        for char in word:
            if char not in current_node.children:
                # create the children nodes
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        # mark the node as end of word
        current_node.end_of_word = True
        

    def search(self, word: str) -> bool:
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                # the word is not in the tree
                return False
            current_node = current_node.children[char]
        # check if the current node is end of word
        # if true the word is in the trie
        return current_node.end_of_word
      
    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                # the prefix is not in the trie
                return False
            current_node = current_node.children[char]
        # found all letters in prefix, return true
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie =Trie()
trie.insert("apple")
print(trie.search("apple"))  # return True
print(trie.search("app"))   # return False
print(trie.startsWith("app")); # return True
print(trie.insert("app"))
print(trie.search("app"))    # return True