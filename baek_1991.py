import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

tree = defaultdict(list)

for _ in range(N):
    root, right, left = input().split()
    tree[root].append(right)
    tree[root].append(left)

preorder_str = ""
inorder_str = ""
postorder_str = ""

def preorder(node):
    global preorder_str

    preorder_str += node

    if tree[node][0] != '.':
        preorder(tree[node][0])

    if tree[node][1] != '.':
        preorder(tree[node][1])

def inorder(node):
    global inorder_str

    if tree[node][0] != '.':
        inorder(tree[node][0])

    inorder_str += node

    if tree[node][1] != '.':
        inorder(tree[node][1])

def postorder(node):
    global postorder_str

    if tree[node][0] != '.':
        postorder(tree[node][0])

    if tree[node][1] != '.':
        postorder(tree[node][1])

    postorder_str += node

preorder('A')
inorder('A')
postorder('A')

print(preorder_str)
print(inorder_str)
print(postorder_str)

