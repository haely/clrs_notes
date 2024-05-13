def topKFrequent(nums, k):
  """
  Finds the k most frequent elements in a list of integers without using Counter.

  Args:
      nums: A list of integers.
      k: An integer representing the number of most frequent elements to return.

  Returns:
      A list of the k most frequent elements in nums.
  """
  # Create a dictionary to store element counts
  element_counts = {}
  for num in nums:
    # Increment the count for the current element
    element_counts[num] = element_counts.get(num, 0) + 1

  # Sort the elements based on their counts (descending order)
  # Use a list comprehension to create key-value pairs with count first
  sorted_elements = sorted([(count, element) for element, count in element_counts.items()], reverse=True)

  # Extract the k most frequent elements
  result = [element for count, element in sorted_elements[:k]]
  
  return result

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
frequent_elements = topKFrequent(nums, k)
print(frequent_elements)

