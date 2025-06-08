
### 🧠 Q13: Longest Common Prefix

**Difficulty**: Easy
**Topic**: Strings
**Platform**: LeetCode
**Challenge ID**: Q13
**Status**: ✅ Solved

---

#### 📄 Problem Statement

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

#### ✍️ Constraints

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* Each `strs[i]` consists of only lowercase English letters if it is non-empty.

---

#### 🔧 Function Signature

```cpp
string longestCommonPrefix(vector<string>& strs);
```

---

#### 📘 Examples

**Example 1:**

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

---

#### 🚀 Approach

* Start by assuming the first string as the prefix.
* Compare the prefix with each string in the array.
* Reduce the prefix length each time a mismatch is found.
* If at any point prefix becomes empty, return "".
* After checking all strings, return the prefix.

**Time Complexity:** O(S), where S is the sum of all characters in all strings.
**Space Complexity:** O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q13_Longest_Common_Prefix.md`
Please tag your solutions with `Q13` for easy organization.
