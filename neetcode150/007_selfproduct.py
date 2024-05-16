def productExceptSelf(nums):
  """
  Finds the product of all elements of an array except the current element.

  Args:
      nums: A list of integers.

  Returns:
      A list of integers where each element is the product of all other elements in nums.
  """
  n = len(nums)
  # Create two arrays to store prefix and suffix products
  left_product = [1] * n
  right_product = [1] * n

  # Calculate prefix products (product of all elements to the left)
  for i in range(1, n):
    left_product[i] = left_product[i - 1] * nums[i - 1]

  # Calculate suffix products (product of all elements to the right)
  for i in range(n - 2, -1, -1):
    right_product[i] = right_product[i + 1] * nums[i + 1]

  # Combine prefix and suffix products for each element (excluding itself)
  result = [left * right for left, right in zip(left_product, right_product)]
  return result

# Example usage
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]

