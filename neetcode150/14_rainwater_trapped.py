def trap(height: List[int]) -> int:
  """
  Calculates the amount of water trapped after raining on an elevation map.

  Args:
      height: A list of integers representing the elevation map.

  Returns:
      The total amount of water trapped.
  """
  n = len(height)
  left_max = [0] * n  # Array to store maximum height seen to the left of each bar
  right_max = [0] * n  # Array to store maximum height seen to the right of each bar

  # Fill left_max array
  left_max[0] = height[0]
  for i in range(1, n):
    left_max[i] = max(left_max[i - 1], height[i])

  # Fill right_max array (start from the end)
  right_max[n - 1] = height[n - 1]
  for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], height[i])

  # Calculate the trapped water at each bar
  total_water = 0
  for i in range(n):
    # Water trapped is limited by the lower of left and right max heights
    water_level = min(left_max[i], right_max[i])
    # If the current height is less than the water level, water gets trapped
    if water_level > height[i]:
      total_water += water_level - height[i]

  return total_water

# Example usage
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
total_water = trap(heights)
print(f"Total amount of water trapped: {total_water}")

