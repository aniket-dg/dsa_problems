initlialie first element of preorder as root
​
cause inorder referes to root-left-right
​
so,
root = inorder[0]
​
mid = find index of root in inorder - referes to - left : root : right
​
means all element to left side of mid are of left sub tree
same for right
​
return root