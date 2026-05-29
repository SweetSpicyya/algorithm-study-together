# {155}. {Min Stack}

**Link:** https://leetcode.com/problems/min-stack/

**Difficulty:** Medium

**Topic:** 

## Problem Summary
design a stack that supports push, pop, top, and retrieving the minimum element, all in $O(1)$ constant time

## Approaches & Discussion
### Angela

- So, this problem is asking me to design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element, **all in $O(1)$ constant time**.
- I will approach this by using a **tuple** to keep track of the current minimum value at each state. Now, let me code this up.
- My approach is to initialize an empty array for the stack. In the `push` function, **if the stack is empty**, it means the current value is also the minimum, so I append a tuple `(val, val)`. Otherwise, I compare the new value with the stored minimum from the top of the stack, and append a new tuple with the updated minimum. **For the `pop` function**, I simply remove the tuple at the top of the stack. **For the `top` function**, I look at the top tuple and return the actual value. **Lastly, for the `getMin` function**, I also look at the top tuple, but return the stored minimum value instead.
- Every function runs in **$O(1)$ time complexity** because we only perform basic array operations without any loops. The **space complexity is $O(N)$** since the stack array will hold up to the number of elements we push into it.