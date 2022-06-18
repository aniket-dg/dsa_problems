Initialize 4 pointers
first, mid, last, prev
prev : indicates last visited element
first : indicates element where ascesnding order property false
mid : where we find element of which prev element is wrong
last : indicates last element which invalidate property
​
if first and last : means we have to swap first and last val
else first and mid
​
do normal inorder dfs