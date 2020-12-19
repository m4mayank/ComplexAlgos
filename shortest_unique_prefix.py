#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
    
    def insert_word(self, word):
        current = self.root
        for i in word:
            if i not in current.children:
                new = TrieNode(i)
                current.children[i] = new
            current.frequency += 1
            current = current.children[i]
        current.frequency += 1
        current.children["."] = TrieNode(".")

    def check_word(self, word):
        current = self.root
        for i in word:
            if i not in current.children:
                return False
            current = current.children[i]
        if "." in current.children:
            return True
        else:
            return False

    def check_prefix(self, word):
        str = ""
        current = self.root.children[word[0]]
        for i in range(len(word)):
            if word[i] == current.val:
                str += word[i]
            if current.frequency == 1:
                return str
            if "." in current.children and ((i+1) == len(word)):
                return str
            else:
                current = current.children[word[i+1]]
class TrieNode:
    def __init__(self, value):
        self.val = value
        self.children = {}
        self.frequency = 0

tr = Trie()
words = ["zebra", "dog", "duck", "dove", "waiter", "wait"]
for word in words:
    tr.insert_word(word)

#print(tr.check_word("zebra"))
print(tr.check_word("dog"))
print(tr.check_word("duck"))
print(tr.check_word("dove"))
print(tr.check_word("wait"))
print(tr.check_word("waiter"))

print(tr.check_prefix("zebra"))
print(tr.check_prefix("dog"))
print(tr.check_prefix("duck"))
print(tr.check_prefix("dove"))
print(tr.check_prefix("waiter"))
print(tr.check_prefix("wait"))