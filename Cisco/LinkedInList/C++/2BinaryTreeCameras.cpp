#include <tuple>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
    int numCameras;

public:
    int minCameraCover(TreeNode *root)
    {
        bool camera, monitored;
        tie(camera, monitored) = dfs(root);
        return monitored ? numCameras : numCameras + 1;
    }

    tuple<bool, bool> dfs(TreeNode *root)
    {
        if (!root)
            return {false, true};

        bool cameraLeft, monitoredLeft;
        tie(cameraLeft, monitoredLeft) = dfs(root->left);

        bool cameraRight, monitoredRight;
        tie(cameraRight, monitoredRight) = dfs(root->right);

        bool camera = !monitoredLeft || !monitoredRight,
             monitored = camera || cameraLeft || cameraRight;

        if (camera)
            numCameras++;

        return {camera, monitored};
    }
};