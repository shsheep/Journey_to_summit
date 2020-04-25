class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        for (int i=0; i<grid.size(); ++i) {
            for (int j=0; j<grid[0].size(); ++j) {
                if (i == 0 && j == 0)
                    continue;
                
                if (i == 0)
                    grid[i][j] += grid[i][j-1];
                else if (j == 0)
                    grid[i][j] += grid[i-1][j];
                else
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j]);
            }
        }
        return grid[grid.size()-1][grid[0].size()-1];
    }
    
    /* Time Limit Exceeded
    int ret = INT_MAX;
    
    void dfs(int x, int y, int curr, vector<vector<int>> grid) {
        if (curr >= ret)
            return;
        if (x == grid.size()-1 && y == grid[0].size()-1)
            ret = min(ret, curr);
        
        if (x != grid.size()-1)
            dfs(x+1, y, curr+grid[x+1][y], grid);
        if (y != grid[0].size()-1)
            dfs(x, y+1, curr+grid[x][y+1], grid);
    }
    
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.size() == 1 && grid[0].size() == 1)
            return grid[0][0];
        dfs(0, 0, grid[0][0], grid);
        return ret;
    }
    */
};

/**
 * Runtime: 8 ms, faster than 85.41% of C++ online submissions for Minimum Path Sum.
 * Memory Usage: 8.3 MB, less than 100.00% of C++ online submissions for Minimum Path Sum.
 **/
