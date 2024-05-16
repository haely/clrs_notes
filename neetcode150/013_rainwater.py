def maxArea(height: List[int]) -> int:
  """
  Finds the maximum area of water a container can store given an array of heights.

  Args:
      height: A list of integers representing the heights of vertical lines.

  Returns:
      The maximum area of water the container can store.
  """
  left, right = 0, len(height) - 1
  max_area = 0
  while left < right:
    # Calculate the width of the container
    width = right - left

    # Get the minimum height between left and right walls
    current_height = min(height[left], height[right])

    # Calculate the current area
    area = width * current_height

    # Update the max_area if necessary
    max_area = max(max_area, area)

    # Move the shorter wall inwards to potentially find a larger container
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

  return max_area

# Example usage
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_water = maxArea(heights)
print(f"Maximum water the container can store: {max_water}")

