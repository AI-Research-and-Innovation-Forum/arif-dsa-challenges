
### 🧠 Q11: Length of Last Word

**Difficulty**: Easy
**Topic**: Strings
**Platform**: LeetCode
**Challenge ID**: Q11
**Status**: ✅ Solved

---

#### 📄 Problem Statement

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A **word** is defined as a maximal substring consisting of **non-space characters only**.

---

#### ✍️ Constraints

* `1 <= s.length <= 10^4`
* `s` consists of only English letters and spaces `' '`.
* There will be at least one word in `s`.

---

#### 🔧 Function Signature

```cpp
int lengthOfLastWord(string s);
```

---

#### 📘 Examples

**Example 1:**

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

---

#### 🚀 Approach

* Trim any trailing spaces at the end of the string.
* Iterate from the end of the string backwards to find the start of the last word.
* Count the characters until a space or the start of the string is reached.
* Return the count.

**Time Complexity**: O(n)
**Space Complexity**: O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q11_Length_of_Last_Word.md`
Tag your solutions with `Q11` for consistency and easy tracking.
