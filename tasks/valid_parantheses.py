# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
def is_valid(s: str) -> bool:
    stack = []
    mapper = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for char in s:
        if char in mapper:
            if not stack or stack.pop() != mapper[char]:
                return False
        else:
            stack.append(char)

    return True if not stack else False


if __name__ == '__main__':
    assert is_valid("()") is True
    assert is_valid("{()[]{}}") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("[") is False
