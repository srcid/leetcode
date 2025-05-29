#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int M, N;
    vector<vector<char>> matrix;

    vector<pair<int, int>> adjs(int row, int col)
    {
        vector<pair<int, int>> neighbors;
        vector<pair<int, int>> candidates = {{row + 1, col}, {row, col + 1}, {row + 1, col + 1}};

        for (auto [a, b] : candidates)
        {
            if (0 <= a && a < M && 0 <= b && b < N)
            {
                neighbors.emplace_back(a, b);
            }
        }
        return neighbors;
    }

    vector<pair<int, int>> expand_sqr(const vector<pair<int, int>> &sqr)
    {
        vector<pair<int, int>> next_sqr;

        for (const auto &[p, q] : sqr)
        {
            for (const auto &[a, b] : adjs(p, q))
            {
                // Check if (a, b) is already in sqr or next_sqr
                if (find(sqr.begin(), sqr.end(), make_pair(a, b)) == sqr.end() &&
                    find(next_sqr.begin(), next_sqr.end(), make_pair(a, b)) == next_sqr.end())
                {
                    if (matrix[a][b] == '1')
                    {
                        next_sqr.emplace_back(a, b);
                    }
                    else
                    {
                        return {};
                    }
                }
            }
        }

        return (next_sqr.size() == sqr.size() + 2) ? next_sqr : vector<pair<int, int>>{};
    }

    int bfs(int i, int j)
    {
        vector<pair<int, int>> sqr = {{i, j}};
        int n = 0;

        while (true)
        {
            vector<pair<int, int>> next_sqr = expand_sqr(sqr);
            n += 1;

            if (!next_sqr.empty())
            {
                sqr = next_sqr;
            }
            else
            {
                break;
            }
        }
        return n;
    }

    int maximalSquare(vector<vector<char>> &matrix)
    {
        this->matrix = matrix;
        M = matrix.size();
        if (M == 0)
            return 0;
        N = matrix[0].size();
        int maximal = 0;

        for (int i = 0; i < M; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                if (matrix[i][j] == '1')
                {
                    int cr = i + 1;
                    while (cr < M && matrix[cr][j] == '1')
                        ++cr;

                    int cc = j + 1;
                    while (cc < N && matrix[i][cc] == '1')
                        ++cc;

                    if ((min(cr - i, cc - j)) * (min(cr - i, cc - j)) <= maximal)
                        continue;

                    int n = bfs(i, j);
                    maximal = max(maximal, n * n);
                }
            }
        }
        return maximal;
    }
};
