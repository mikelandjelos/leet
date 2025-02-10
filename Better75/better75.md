# Better 75 list

- [Link](https://www.techinterviewhandbook.org/grind75/);

## Problems

1. [Two Sum](./1_TwoSum.py) - use hash map for mapping numbers to their indices, `O(n)` time, `O(n)` space;
2. [Valid Parentheses](./2_ValidParentheses.py) - use queue for storing left brackets, `O(n)` time, `O(n)` space;
3. [Merge Two Sorted Lists](./3_MergeTwoSortedLists.py) - singly-linked list, **didn't do it in-place**, `O(n)` time, `O(n)` space;
4. [Best Time To Buy And Sell Stocks](./4_BestTimeToBuyAndSellStocks.py) - two pointers, sliding window, `O(n)` time, `O(1)` space;
5. [Valid Palindrome](./5_ValidPalindrome.py) - `O(n)` time, `O(1)` space;
6. [Invert Binary Tree](./6_InvertBinaryTree.py) - inorder traversal, `O(logn)` time (tree height), `O(1)` space (in-place);
7. [Valid Anagram](./7_ValidAnagram.py) - use hash to map out the first string, and delete it when traversing second, `O(n)` time, `O(n)` space;
8. [Binary Search](./8_BinarySearch.py) - be careful with one-off mistakes, `O(logn)` time (like a tree), `O(1)` space;
9. [Flood Fill](./9_FloodFill.py) - `O(V + E)` time (where `V = MxN`, `E = MxNx4`, so basically `O(V + E) = O(MxN)`), `O(MxN)` space (same reasoning);
10. [Lowest Common Ancestor Of BST](./10_LowestCommonAncestorOfBST.py) - preorder, `O(logn)` time, `O(1)` space;
