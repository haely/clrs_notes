def twoSum(numbers: List[int], target: int) -> List[int]:
  """
  Finds two numbers in a sorted array that add up to a specific target number.

  Args:
      numbers: A sorted list of integers.
      target: The target sum.

  Returns:
      A list containing the indices (1-indexed) of the two numbers that add up to the target.
  """
  left, right = 0, len(numbers) - 1
  while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
      return [left + 1, right + 1]
    elif current_sum < target:
      left += 1
    else:
      right -= 1
  return []

# Example usage
numbers = [2, 7, 11, 15]
target = 9
indices = twoSum(numbers, target)
print(f"Indices of the two numbers: {indices}")

