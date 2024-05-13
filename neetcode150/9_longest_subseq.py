def longestConsecutive(nums):
  """
  Finds the length of the longest consecutive sequence in an unsorted array.

  Args:
      nums: A list of integers.

  Returns:
      The length of the longest consecutive sequence.
  """
  # Create a set to store all unique elements in the array
  num_set = set(nums)
  longest_seq = 0
  
  # Iterate through each element in the array
  for num in nums:
    # Check if the element is the beginning of a potential sequence
    if (num - 1) not in num_set:
      # Start a new sequence and keep track of its length
      current_seq = 1
      while num + current_seq in num_set:
        current_seq += 1
      # Update the longest sequence if necessary
      longest_seq = max(longest_seq, current_seq)
  
  return longest_seq

# Example usage
nums = [100, 4, 200, 1, 3, 2]
longest_length = longestConsecutive(nums)
print(longest_length)  # Output: 4

