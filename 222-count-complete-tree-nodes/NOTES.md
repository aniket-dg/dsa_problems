```
if not root:
return 0
res = []
total = 0
res.append(root)
while res:
total += 1
x = res.pop()
if x.left:
res.append(x.left)
if x.right:
res.append(x.right)
return total
```
​
this method is traversing each and every node in tree and returning total
similar to inorder, preorder, postorder traversal
​
second method is interesting
​
traverse leftmodst child and rightmost child and check both are equal then return 2**level - 1
​
else return 1 + recursive call on left  + right