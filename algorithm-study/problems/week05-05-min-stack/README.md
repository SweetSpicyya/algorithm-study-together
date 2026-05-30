# {155}. {Min Stack}

**Link:** https://leetcode.com/problems/min-stack/

**Difficulty:** Medium
**Topic:** Stack, Design

## Approaches & Discussion

### Rachel

- **Understand**: We need to implement a stack that supports push, pop, top, and getMin in O(1) time. A normal stack would require scanning all elements to find the minimum, which is O(n). We need a way to retrieve the minimum in constant time.
- **Match**: The key insight is maintaining a second minStack in parallel with the main stack. minStack[i] stores the minimum value of the main stack from index 0 to i. This way getMin is always just a peek at the top of minStack.
- **Plan**: On every push, I push the new value to stack and push the smaller of the new value and the curren minStack top to minStack. On pop, I pop both stacks together since they always stay the same size. top returns the top of stack, and getMin returns the top of minStack without popping.
- **Evaluate**:
  Time: O(1) - push, pop, top, and getMin each do a constant number of operations.
  Space: O(n) - minStack stores one value per push, same size as the main stack.

## Approaches & Discussion
### Angela

- So, this problem is asking me to design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element, **all in $O(1)$ constant time**.
- I will approach this by using a **tuple** to keep track of the current minimum value at each state. Now, let me code this up.
- My approach is to initialize an empty array for the stack. In the `push` function, **if the stack is empty**, it means the current value is also the minimum, so I append a tuple `(val, val)`. Otherwise, I compare the new value with the stored minimum from the top of the stack, and append a new tuple with the updated minimum. **For the `pop` function**, I simply remove the tuple at the top of the stack. **For the `top` function**, I look at the top tuple and return the actual value. **Lastly, for the `getMin` function**, I also look at the top tuple, but return the stored minimum value instead.
- Every function runs in **$O(1)$ time complexity** because we only perform basic array operations without any loops. The **space complexity is $O(N)$** since the stack array will hold up to the number of elements we push into it.
