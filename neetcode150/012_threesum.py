def threeSum(nums: List[int]) -> List[List[int]]:
  """
  Finds all triplets in an integer array that add up to zero, excluding duplicates.

  Args:
      nums: A list of integers.

  Returns:
      A list of lists, where each inner list represents a triplet that sums to zero.
  """
  results = []
  nums.sort()  # Sort the array for efficient two-pointer search

  for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first element
      continue
    left, right = i + 1, len(nums) - 1
    while left < right:
      current_sum = nums[i] + nums[left] + nums[right]
      if current_sum == 0:
        results.append([nums[i], nums[left], nums[right]])
        while left < right and nums[left] == nums[left + 1]:
          left += 1  # Skip duplicate second elements
        while left < right and nums[right] == nums[right - 1]:
          right -= 1  # Skip duplicate third elements
        left += 1
        right -= 1
      elif current_sum < 0:
        left += 1
      else:
        right -= 1
  return results

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
triplets = threeSum(nums)
print(f"All triplets that sum to zero: {triplets}")

