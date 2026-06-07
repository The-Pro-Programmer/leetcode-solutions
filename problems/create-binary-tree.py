## https://leetcode.com/problems/create-binary-tree-from-descriptions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        children = set()

        for parentValue, childValue, isLeft in descriptions:
            if parentValue not in nodeMap:
                nodeMap[parentValue] = TreeNode(parentValue)
            parentNode = nodeMap[parentValue]
            if childValue not in nodeMap:
                nodeMap[childValue] = TreeNode(childValue)
            childNode = nodeMap[childValue]
            if isLeft == 1:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            children.add(childValue)

        for parentValue in nodeMap:
            if parentValue not in children:
                return nodeMap[parentValue]

        return None
        
