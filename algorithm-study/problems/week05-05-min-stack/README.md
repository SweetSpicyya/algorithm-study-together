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
