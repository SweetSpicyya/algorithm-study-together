# {155}. {Min Stack}

**Link:** https://leetcode.com/problems/min-stack
**Difficulty:** Medium
**Topic:** Stack, Design

## Approaches & Discussion
### Yourim
The main challenge is recovering the previous minimum value when the current minimum is popped from the stack. 
To solve this, we can use two synchronized stacks. A main stack for actual data, and a min_stack to track the minimum history. 
When pushing a value, we append it to the main stack and simultaneously push the smaller value between the new input and the current minimum into the min_stack. 
When popping, we must remove elements from both stacks together to maintain the exact same history and length. 
As a result, all operations—including getMin—can access the top elements directly, achieving a time complexity of O(1) and a space complexity of O(n).