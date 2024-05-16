def encode(strs):
  """
  Encodes a list of strings into a single string for transmission.

  Args:
      strs: A list of strings.

  Returns:
      A string containing the encoded representation of the list.
  """
  encoded_string = ""
  for s in strs:
    # Add the length of the current string followed by a separator
    encoded_string += str(len(s)) + "#" + s
  return encoded_string

def decode(encoded_string):
  """
  Decodes a string back into the original list of strings.

  Args:
      encoded_string: The string containing the encoded list of strings.

  Returns:
      A list of strings decoded from the encoded string.
  """
  decoded_strings = []
  start = 0
  while start < len(encoded_string):
    # Find the separator "#" to determine the length of the current string
    separator_index = encoded_string.find("#", start)
    if separator_index == -1:
      break
    # Extract the length of the current string
    string_length = int(encoded_string[start:separator_index])
    # Extract the current string based on its length
    decoded_string = encoded_string[separator_index + 1:separator_index + 1 + string_length]
    decoded_strings.append(decoded_string)
    # Move to the next string
    start = separator_index + 1 + string_length
  return decoded_strings

# Example usage
strs = ["apple", "banana", "cherry"]
encoded_string = encode(strs)
print(encoded_string)  # Output: 5#apple#6#banana#6#cherry

decoded_list = decode(encoded_string)
print(decoded_list)  # Output: ['apple', 'banana', 'cherry']

