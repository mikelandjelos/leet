#include <vector>
#include <string>
#include <memory>

using namespace std;

class Solution
{
    struct TrieNode
    {
        vector<shared_ptr<TrieNode>> children;
        int wordIndex;
        TrieNode() : children(26), wordIndex(-1) {}
    };

    const char VISITED = '#';

    shared_ptr<TrieNode> buildTrie(const vector<string> &words)
    {
        auto root = make_shared<TrieNode>();

        int i = 0;
        for (const auto word : words)
        {
            auto node = root;
            for (auto ch : word)
            {
                ch -= 'a';
                if (!node->children[ch])
                    node->children[ch] = make_shared<TrieNode>();
                node = node->children[ch];
            }
            node->wordIndex = i++;
        }

        return root;
    }

    void dfs(vector<vector<char>> &board, const vector<string> &words,
             vector<string> &foundWords, int i, int j, shared_ptr<TrieNode> currentNode)
    {
        if (currentNode->wordIndex != -1)
            foundWords.push_back(words[currentNode->wordIndex]), currentNode->wordIndex = -1;

        if (i < 0 or i >= board.size() or j < 0 or j >= board[0].size() or
            board[i][j] == VISITED)
            return;

        char temp = board[i][j] - 'a';
        if (!currentNode->children[temp])
            return;

        board[i][j] = VISITED;

        dfs(board, words, foundWords, i + 1, j, currentNode->children[temp]);
        dfs(board, words, foundWords, i - 1, j, currentNode->children[temp]);
        dfs(board, words, foundWords, i, j + 1, currentNode->children[temp]);
        dfs(board, words, foundWords, i, j - 1, currentNode->children[temp]);

        board[i][j] = temp + 'a';
    }

public:
    vector<string>
    findWords(vector<vector<char>> &board, vector<string> &words)
    {
        shared_ptr<TrieNode> trie = buildTrie(words);
        vector<string> foundWords;

        for (int i = 0; i < board.size(); ++i)
            for (int j = 0; j < board[0].size(); ++j)
                dfs(board, words, foundWords, i, j, trie);

        return foundWords;
    }
};
