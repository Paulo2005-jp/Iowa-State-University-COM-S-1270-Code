# Paulo Juarez - 2025-05-06
# Assignment: isPalindrome.py
# This script checks if a string is a palindrome using both iterative and recursive methods.

def isPalindromeIterative(s):
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeRecursive(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursive(s[1:-1])

def main():
    user_input = input("Enter a string: ")
    print("Iterative Palindrome Check:", isPalindromeIterative(user_input))
    print("Recursive Palindrome Check:", isPalindromeRecursive(user_input))

if __name__ == "__main__":
    main()
