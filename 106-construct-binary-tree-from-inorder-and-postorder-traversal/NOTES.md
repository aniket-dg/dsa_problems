two approaches second one is space efficient
​
1. Approach
create root node from last element of postorder list cause
postorder = left, right, root
then find mid using index from inoder
then **create right subtree first** bacause we are traversing from last of list so order is like root -> right -> left
then create left subtree
2.  Approach
Create a dictionary from inorder list
pass 2 index low, and high
and only pass low, and high insted of sub list