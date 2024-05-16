def isPalindrome(s: str) -> bool:
  """
  Checks if a given string is a palindrome.

  Args:
      s: The string to check.

  Returns:
      True if the string is a palindrome, False otherwise.
  """

  s = ''.join(char.lower() for char in s if char.isalnum())
  return s == s[::-1]

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  # False

