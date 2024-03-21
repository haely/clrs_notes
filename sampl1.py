class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    dp = {} # (index, total) -> # of ways

    def backtrack(i, total):
      if i == len(nums):
        return 1 if total == target else 0
      if (i, total) in dp:
        return dp[(i, total)]

      dp[(i, total)] = (backtrack(i+1, total + nums[i]) +
                        backtrack(i+1, total - nums[i]))
      return dp[(i, total)]

    return backtrack(0, 0)


class Solution:
  def alienOrder(self, words: List[str]) -> str:
    adj = { c:set() for w in words for c in q }
    for i in range(len(words) - 1):
      w1, w2 = words[i], words[i+1]
      minLen = min(len(w1), len(w2))
      if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
        return ""
      for j in range(midLen):
        if w1[j] != w2[j]:
          adj[w1[j]].add(w2[j])
          break

    visit = {}
    res = []

    def dfs(c):
      if c in visit:
        return visit[c]
      visit[c] = True
      for nei in adj[c]:
        if dfs(nei):
          return True
      visit[c] = False
      res.append(c)

    for c in adj:
      if dfs(c):
        return ""
      res.reverse
      return "".join(res)
