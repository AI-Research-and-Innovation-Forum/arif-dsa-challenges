
### 🧠 Q12: Find the Index of the First Occurrence in a String

**Difficulty**: Easy
**Topic**: String Searching
**Platform**: LeetCode
**Challenge ID**: Q12
**Status**: ✅ Solved

---

#### 📄 Problem Statement

Given two strings `needle` and `haystack`, return the **index of the first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

#### ✍️ Constraints

* `1 <= haystack.length, needle.length <= 10^4`
* `haystack` and `needle` consist of only lowercase English characters.

---

#### 🔧 Function Signature

```cpp
int strStr(string haystack, string needle);
```

---

#### 📘 Examples

**Example 1:**

```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.
```

**Example 2:**

```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" does not occur in "leetcode", so return -1.
```

---

#### 🚀 Approach

* Use a straightforward substring search (e.g., built-in functions or manual iteration).
* Iterate through `haystack` and check for the first index where substring `needle` matches.
* Return the index if found; otherwise, return -1.

**Time Complexity**: O(n \* m) in worst case (where n = haystack length, m = needle length)
**Space Complexity**: O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q12_Find_First_Occurrence.md`
Tag your solutions with `Q12` for consistency and easy tracking.
