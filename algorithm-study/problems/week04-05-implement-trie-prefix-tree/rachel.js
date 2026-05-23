var Trie = function () {
  this.children = {};
  this.isEnd = false;
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
  let node = this;
  for (let char of word) {
    if (!node.children[char]) {
      node.children[char] = new Trie();
    }
    node = node.children[char];
  }
  node.isEnd = true;
};

Trie.prototype._find = function (word) {
  let node = this;
  for (let char of word) {
    if (!node.children[char]) return null;
    node = node.children[char];
  }
  return node;
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  const node = this._find(word);
  return node !== null && node.isEnd === true;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  return this._find(prefix) !== null;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
