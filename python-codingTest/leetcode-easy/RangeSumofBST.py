class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if (root == None):
            return 0
        s=0
        if root.val >= low and root.val <= high:
            s +=root.val    
        
        return s + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)

#Use recursive method