# 二叉树遍历
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def traverse(root: TreeNode):
	if root is None:
		return 
	traverse(root.left)
	traverse(root.right)
