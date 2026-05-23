class Trie(object):

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        for char in word:
            if not char in curr.children:
                curr.children[char]=Trie()
            curr = curr.children[char] 
        
        curr.is_end_of_word = True   

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self
        for char in word:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        if curr.is_end_of_word == True:
            return True
        else : return False


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        
        curr = self
        for char in prefix:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)