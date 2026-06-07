## my way

class Solution:
    def isValid(self, s: str) -> bool:
        brakets = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        str_stack = []
        for char in s:
            if char in brakets:
                if brakets[char] == str_stack[-1]:
                    str_stack.pop()
                    continue

            str_stack.append(char)

        if len(str_stack) == 0:
            return True
        else:
            return False

##################################################
## better way

class Solution:
    def isValid(self, s: str) -> bool:
        brakets = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        str_stack = []
        for char in s:
            if char in brackets:
                if not str_stack or str_stack[-1] != brackets[char]:
                    return False

                str_stack.pop()
            else:
                str_stack.append(char)

        if len(str_stack) == 0:
            return True
        else:
            return False
