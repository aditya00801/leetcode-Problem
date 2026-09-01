class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();

        int sr = -1, sc = -1;
        int litterCount = 0;

        // Number the litter cells
        vector<vector<int>> litterId(m, vector<int>(n, -1));

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (classroom[r][c] == 'S') {
                    sr = r;
                    sc = c;
                }
                else if (classroom[r][c] == 'L') {
                    litterId[r][c] = litterCount++;
                }
            }
        }

        int fullMask = (1 << litterCount) - 1;

        // State:
        // row, col, remaining energy, collected litter mask
        struct State {
            int r, c, e, mask;
        };

        queue<State> q;

        // visited[r][c][energy][mask]
        vector<vector<vector<vector<bool>>>> visited(
            m,
            vector<vector<vector<bool>>>(
                n,
                vector<vector<bool>>(
                    energy + 1,
                    vector<bool>(1 << litterCount, false)
                )
            )
        );

        q.push({sr, sc, energy, 0});
        visited[sr][sc][energy][0] = true;

        int moves = 0;

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        while (!q.empty()) {
            int sz = q.size();

            while (sz--) {
                auto [r, c, e, mask] = q.front();
                q.pop();

                // All litter collected
                if (mask == fullMask) {
                    return moves;
                }

                // If no energy, we cannot move.
                // Being on R would already have reset our energy.
                if (e == 0)
                    continue;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    // Out of bounds
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n)
                        continue;

                    // Obstacle
                    if (classroom[nr][nc] == 'X')
                        continue;

                    int ne = e - 1;
                    int nmask = mask;

                    // Collect litter
                    if (classroom[nr][nc] == 'L') {
                        int id = litterId[nr][nc];
                        nmask |= (1 << id);
                    }

                    // Reset energy
                    if (classroom[nr][nc] == 'R') {
                        ne = energy;
                    }

                    if (!visited[nr][nc][ne][nmask]) {
                        visited[nr][nc][ne][nmask] = true;
                        q.push({nr, nc, ne, nmask});
                    }
                }
            }

            moves++;
        }

        return -1;
    }
};