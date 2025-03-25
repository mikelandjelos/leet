#include <vector>
#include <string>

using namespace std;

class Solution
{
    const vector<pair<int, int>> DIRECTIONS = {
        {0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    const char VISITED = '#';

    bool dfs(vector<vector<char>> &board, const string &word, int i, int j, int k)
    {
        if (k == word.size())
            return true;

        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[k])
            return false;

        char temp = board[i][j];
        board[i][j] = VISITED;

        for (const auto &[dx, dy] : DIRECTIONS)
        {
            int x = i + dx, y = j + dy;
            if (dfs(board, word, x, y, k + 1))
                return true;
        }

        board[i][j] = temp;
        return false;
    }

public:
    bool exist(vector<vector<char>> &board, string word)
    {
        for (int i = 0; i < board.size(); ++i)
            for (int j = 0; j < board[0].size(); ++j)
                if (board[i][j] == word[0] && dfs(board, word, i, j, 0))
                    return true;
        return false;
    }
};
