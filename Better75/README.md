# Better 75 list

- [Link](https://www.techinterviewhandbook.org/grind75/);
- Legend:
  - 🔴 - hard problem;
  - 🟡 - medium problem;
  - 🟢 - easy problem;

## Problems

1. 🟢 [Two Sum](./1_TwoSum.py) - use hash map for mapping numbers to their indices, `O(n)` time, `O(n)` space;
   1. There is also 🟡 [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) which has one difference - the array is sorted - this problem can be done using two pointer approach in linear time (`O(n)`) and constant space (`O(1)`);
2. 🟢 [Valid Parentheses](./2_ValidParentheses.py) - use queue for storing left brackets, `O(n)` time, `O(n)` space;
3. 🟢 [Merge Two Sorted Lists](./3_MergeTwoSortedLists.py) - singly-linked list, **didn't do it in-place**, `O(n)` time, `O(n)` space;
4. 🟢 [Best Time To Buy And Sell Stocks](./4_BestTimeToBuyAndSellStocks.py) - two pointers, sliding window, `O(n)` time, `O(1)` space;
5. 🟢 [Valid Palindrome](./5_ValidPalindrome.py) - `O(n)` time, `O(n)` space;
6. 🟢 [Invert Binary Tree](./6_InvertBinaryTree.py) - inorder traversal, `O(logn)` time (tree height), `O(1)` space (in-place);
7. 🟢 [Valid Anagram](./7_ValidAnagram.py) - use hash to map out the first string, and delete it when traversing second, `O(n)` time, `O(n)` space;
8. 🟢 [Binary Search](./8_BinarySearch.py) - be careful with one-off mistakes, `O(logn)` time (like a tree), `O(1)` space;
9. 🟢 [Flood Fill](./9_FloodFill.py) - `O(V + E)` time (where `V = MxN`, `E = MxNx4`, so basically `O(V + E) = O(MxN)`), `O(MxN)` space (same reasoning);
10. 🟢 [Lowest Common Ancestor Of BST](./10_LowestCommonAncestorOfBST.py) - preorder, `O(logn)` time, `O(1)` space;
11. 🟢 [Balanced Tree](./11_BalancedTree.py) - postorder, `O(logn)` time, `O(1)` space;
12. 🟢 [Linked List Cycle](./12_LinkedListCycle.py) - **tortoise and hare algo**, `O(n)` time, `O(1)` memory;
13. 🟢 [Implement Queue using Stacks](./13_ImplementQueueUsingStacks.py) - `O(1)` **amortized** pop, `O(1)` push;
14. 🟢 [First Bad Version](./14_FirstBadVersion.py) - left binary search, `O(logn)` time, `O(1)` ;
15. 🟢 [Ransom Note](./15_RansomNote.py) - alternative of valid palindrome, `O(n+m)` time, `O(n)` space;
16. 🟢 [Climbing Stairs](./16_ClimbingStairs.py) - **INTRO TO DYNAMIC PROGRAMMING** (spoiler - Fibonacci is the solution), three ways to solve - brute force DFS `O(2^n)`, memoization DFS `O(n)`, Bottom-up DP `O(logn)` - [video](https://www.youtube.com/watch?v=Y0lT9Fck7qI);
17. 🟢 [Longest Palindrome](./17_LongestPalindrome.py) - similar to original palindrome problem, with an extra step;
18. 🟢 [Reverse Singly-LL](./18_ReverseLL.py) - three pointers (`prev`, `curr`, `next` - curr starting from `head`), loop while `next` not `null`, `temp` holds `next.next` - draw it on paper - time complexity `O(n)`, space constant;
19. 🟢 [Majority Element](./19_MajorityElement.py) - `O(n)` time, `O(1)` space, array must have majority element for the optimal solution to work; easy solution uses hash and `O(n)` space;
20. 🟢 [Add Binary](./20_AddBinary.py) - one loop to max `len`, with default `0`;
21. 🟢 [Diameter of Binary tree](./21_DiameterOfBinaryTree.py) - can be done with global variable + DFS height approach, time `O(logn)` (balanced BT), constant space;
22. 🟢 [Middle of the LL](./22_MiddleOfTheLL.py) - again, two pointers, tortoise and hare version;
23. 🟢 [Maximum Depth of Binary Tree](./23_MaximumDepthOfBT.py) - recursive DFS, iterative BFS and DFS for practice - `O(n)` time;
24. 🟢 [Contains Duplicate](./24_ContainsDuplicate.py) - just use a hashset, `O(n)` time and `O(n)` space - can be done brute force, with sorting, and the optimal with set;
25. 🟡 [Maximum Subarray](./25_MaximumSubarray.py) - `O(n^3)` worst solution, `O(n^2)` optimization, `O(n)` optimal (**Kadane's Algo**, remove negative prefix);
26. 🟡 [Insert Interval](./26_InsertInterval.py) - three edge cases, two with non-overlapping and one with overlapping, linear time and space;
27. 🟡 [01 Matrix](./27_01Matrix.py) - `O(MxN)` time and space complexity, it's kinda BSF inspired algorithm - uses queue;
    1. Same as 🟡 [Map of Highest Peak question](https://leetcode.com/problems/map-of-highest-peak/description/);
28. 🟡 [K Closest Points to Origin](./28_KClosestPointsToOrigin.py) - using minheap insead of sorting gives `O(klogn)` instead `O(nlogn)`, space complexity is `O(1)` because **heapify** is done in-place;
29. 🟡 [Longset Substring Without Repeating Characters](./29_LongestSubstringWithoutRepeatingCharacters.py) - sliding window + hashset, `O(n)` time `O(n)` space;
30. 🟡 [Three Sum](./30_ThreeSum.py) - sorting to remove duplicates + two pointers approach - gives `O(n^2)` time and `O(1)` space;
31. 🟡 [BST Level Order Traversal](./31_LevelOrderTraversal.py) - `O(n)` time, `O(n)` space - BFS with level elements buffering, using the `len(q)` property;
32. 🟡 [Clone Graph](./32_CloneGraph.py) - DFS to traverse, hashmap to map old to new - time complexity `O(V + E)`, space complexity `O(V)`;
33. 🟡 [Evaluate Reverse Polish Notation](./33_EvaluateReversePolishNotation.py) - use stack, be careful with **rounding to zero**, time and space are linear;
34. 🟡 [Course Schedule](./34_CourseSchedule.py) - can be solved by using recursive DFS approach, or by using iterative approach - topological sort - both have time complexity `O(V+E)` and space `O(V)`;
    1. Also 🟡 [Course Schedule II](./32_2_CourseScheduleII.py) - can be solved using **Kahn's algorithm** (topological sort);
35. 🟡 [Implement Trie (Prefix Tree)](./35_ImplementTrie.py) - `TrieNode` with hashmap, `insert`, `search` and `startsWith` methods, all with `O(n)` time complexity;
36. 🟡 [Coin Change](./36_CoinChange.py) - greedy not applicable, top-down backtracking with memoization, bottom-up DP for optimal solution - `O(NxK)` time and `O(N)` space, where `N` is amount and `K` is number of coins;
37. 🟡 [Product of Array Except Self](./37_ProductOfArrayExceptSelf.py) - can be done using prefix and postfix array in linear time and space; optimal - 2 passes, computing the prefix summs - `O(2n) == O(n)` time;
38. 🟡 [Min Stack](./38_MinStack.py) - two arrays - one for the actual stack, and one "history of minimums" stack - `O(1)` `getMin` time complexity, and `O(n)` space complexity for ensuring constant time;
39. 🟡 [Validate BST](./39_ValidateBST.py) - top-down recursive approach with interval propagation - time complexity `O(n)`, and constant space;
40. 🟡 [Number of Islands](./40_NumberOfIslands.py) - iterative DFS (using stack) when island found until its fully mapped, skip water and already mapped parts, `O(MxN)` space and time complexity;
41. 🟡 [Rotten Oranges](./41_RottingOranges.py) - level order graph traversal - `O(MxN)` time and space;
42. 🟡 [Search in Rotated Sorted Array](./42_SearchInRotatedSortedArray.py) - left and right sorted arrays (conditions to find out in which part you are), subcases for each - time is logarithmic (`O(logN)`) and space is constant;
43. 🟡 [Combination Sum](./43_CombinationSum.py) - backtracking, exponential time (`O(2^N)`) and space complexity;
44. 🟡 [Permutations](./44_Permutations.py) - recursion + iteration - `O(N!)` problem - optimal solution;
45. 🟡 [Merge Intervals](./45_MergeIntervals.py) - sorting the interval array (pivot is the starting of the interval) is the key to solving - `O(nlogn)` time complexity;
46. 🟡 [Lowest Common Ancestor (LCA) of a Binary Tree](./46_LCAofBST.py) - `O(n)` time and `O(1)` space - 3 cases (root is left, root is right, or root is neither);
