# {232}. {Implement Queue using Stacks}

**Link:** https://leetcode.com/problems/implement-queue-using-stacks/

**Difficulty:** Easy

**Topic:** Stack, Design, Queue

## Problem Summary
Implement a first in first out (FIFO) queue using only two stacks

## Approaches & Discussion
### Angela

- **This problem is asking me to** implement a FIFO queue using only two stacks.
- **My approach is to** make two arrays called stack_push which stores elements, stack_pop which retrieves elements and in the push function, push elements onto stack_push using append method which runs in O(1). In the pop method, to implement FIFO from stack transfer elements from stack_push to stack_pop using pop method also before it, check whether stack_pop is empty or not to avoid redundant transfers which runs in amortized O(1). Next, in peek function, check whether stack_pop is empty or not and return the front element only when the stack_pop isn't empty which runs in amortized O(1). Lastly, if both stacks are empty, return True otherwise return False which runs in O(1).
- **This runs in** O(n) space complexity because both stacks can hold up to n elements