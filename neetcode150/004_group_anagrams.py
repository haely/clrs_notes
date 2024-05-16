from collections import defaultdict

def groupAnagrams(strs):
  """
  Groups the anagrams from a list of strings.

  Args:
      strs: A list of strings.

  Returns:
      A list of lists, where each inner list contains anagrams.
  """
  ans = defaultdict(list)
  for s in strs:
    # Sort the characters in each string to create a unique key
    ans["".join(sorted(s))].append(s)
  return list(ans.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = groupAnagrams(strs)
print(anagrams)

