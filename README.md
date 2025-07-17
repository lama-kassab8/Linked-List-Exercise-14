# LeetCode - Rotate List

## Problem

Given the `head` of a linked list and an integer `k`, rotate the list to the right by `k` places.

🔗 [LeetCode Link](https://leetcode.com/problems/rotate-list/?envType=problem-list-v2&envId=linked-list)

## Approach

To rotate the list:

1. **Edge Case Check**  
   - If the list is empty, has one node, or `k` is zero, return the head as-is.

2. **Find the Length and Tail**  
   - Traverse the list to find its length and the current tail node.

3. **Make the List Circular**  
   - Connect the tail to the head to form a circular list.

4. **Find the New Tail**  
   - Compute the index of the new tail: `length - (k % length) - 1`.

5. **Break the Circle**  
   - Traverse to the new tail, set `new_head = new_tail.next`, then disconnect the circle.

6. **Return the New Head**

