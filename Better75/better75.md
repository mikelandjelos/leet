# Better 75 list

- [Link](https://www.techinterviewhandbook.org/grind75/);

## Problems

1. [Two Sum](./1_TwoSum.py) - use hash map for mapping numbers to their indices, `O(n)` time, `O(n)` space;
2. [Valid Parentheses](./2_ValidParentheses.py) - use queue for storing left brackets, `O(n)` time, `O(n)` space;
3. [Merge Two Sorted Lists](./3_MergeTwoSortedLists.py) - singly-linked list, **didn't do it in-place**, `O(n)` time, `O(n)` space;
4. [Best Time To Buy And Sell Stocks](./4_BestTimeToBuyAndSellStocks.py) - two pointers, sliding window, `O(n)` time, `O(1)` space;
5. [Valid Palindrome](./5_ValidPalindrome.py) - `O(n)` time, `O(n)` space;
6. [Invert Binary Tree](./6_InvertBinaryTree.py) - inorder traversal, `O(logn)` time (tree height), `O(1)` space (in-place);
7. [Valid Anagram](./7_ValidAnagram.py) - use hash to map out the first string, and delete it when traversing second, `O(n)` time, `O(n)` space;
8. [Binary Search](./8_BinarySearch.py) - be careful with one-off mistakes, `O(logn)` time (like a tree), `O(1)` space;
9. [Flood Fill](./9_FloodFill.py) - `O(V + E)` time (where `V = MxN`, `E = MxNx4`, so basically `O(V + E) = O(MxN)`), `O(MxN)` space (same reasoning);
10. [Lowest Common Ancestor Of BST](./10_LowestCommonAncestorOfBST.py) - preorder, `O(logn)` time, `O(1)` space;
11. [Balanced Tree](./11_BalancedTree.py) - postorder, `O(logn)` time, `O(1)` space;
12. [Linked List Cycle](./12_LinkedListCycle.py) - **tortoise and hare algo**, `O(n)` time, `O(1)` memory;
13. [Implement Queue using Stacks](./13_ImplementQueueUsingStacks.py) - `O(1)` **amortized** pop, `O(1)` push;
14. [First Bad Version](./14_FirstBadVersion.py) - left binary search, `O(logn)` time, `O(1)` ;
15. [Ransom Note](./15_RansomNote.py) - alternative of valid palindrome, `O(n+m)` time, `O(n)` space;
16. [Climbing Stairs](./16_ClimbingStairs.py) - **INTRO TO DYNAMIC PROGRAMMING** (spoiler - Fibonacci is the solution), three ways to solve - brute force DFS `O(2^n)`, memoization DFS `O(n)`, Bottom-up DP `O(logn)` - [video](https://www.youtube.com/watch?v=Y0lT9Fck7qI);
17. [Longest Palindrome](./17_LongestPalindrome.py) - similar to original palindrome problem, with an extra step;
18. [Reverse Singly-LL](./18_ReverseLL.py) - three pointers (`prev`, `curr`, `next` - curr starting from `head`), loop while `next` not `null`, `temp` holds `next.next` - draw it on paper - time complexity `O(n)`, space constant;
19. [Majority Element](./19_MajorityElement.py) - `O(n)` time, `O(1)` space, array must have majority element for the optimal solution to work; easy solution uses hash and `O(n)` space;
20. [Add Binary](./20_AddBinary.py);
