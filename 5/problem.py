print("""Your Next Challenge: Valid Parentheses
Let's keep this momentum going with a classic data structure problem. This one moves away from pure array/string indexing and introduces the concept of a Stack, which is incredibly important for interviews.

Problem Description
You are given a string s containing just the characters '(', ')', '{', Internal', '[' and ']'. Your task is to determine if the input string is valid.

An input string is valid if:  

Open brackets must be closed by the same type of brackets.  

Open brackets must be closed in the correct order.  

Every close bracket has a corresponding open bracket of the same type.  

Examples
Example 1
Input: s = "()[]{}"

Output: True

Example 2
Input: s = "(]"

Output: False

Example 3
Input: s = "([)]"

Output: False

Explanation: Even though all brackets have a pair, they are closed out of order. The [ must be closed before the (.

Example 4
Input: s = "{[]}"

Output: True

Constraints
  
The string will contain at least 1 character.

The string consists only of the characters ()[]{}.""")