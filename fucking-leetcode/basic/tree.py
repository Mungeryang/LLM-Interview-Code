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


# 层序遍历

from collectios import deque

def levelOrderTraverse(root):
	if root is None:
		return
	q = deque()
	q.append(root)
	while q:
		cur = q.popleft()

		if cur.left is not None:
			q.append(cur.left)
		if cur.right is not None:
			q.append(cur.right)

