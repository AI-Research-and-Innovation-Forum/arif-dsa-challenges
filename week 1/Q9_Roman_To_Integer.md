
### 🧠 Q9: Roman to Integer

**Difficulty**: Easy
**Topic**: Strings, Hash Table, Simulation
**Platform**: LeetCode
**Challenge ID**: Q9
**Status**: ✅ Solved

---

#### 📄 Problem Statement

Roman numerals are represented by seven different symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Certain combinations require subtraction, such as:

* `IV` (4), `IX` (9)
* `XL` (40), `XC` (90)
* `CD` (400), `CM` (900)

**Given a Roman numeral string `s`, convert it into an integer.**

---

#### ✍️ Constraints

* `1 <= s.length <= 15`
* `s` contains only the characters: `'I', 'V', 'X', 'L', 'C', 'D', 'M'`
* It is guaranteed that `s` is a **valid Roman numeral** in the range `[1, 3999]`

---

#### 🔧 Function Signature

```cpp
int romanToInt(string s);
```

---

#### 📘 Examples

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 1 + 1 + 1 = 3
```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3
```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation:
M = 1000, CM = 900, XC = 90, IV = 4
Total = 1000 + 900 + 90 + 4 = 1994
```

---

#### 🚀 Optimal Strategy

* Map all Roman characters to their integer values.
* Traverse the string from left to right:

  * If the **current value** is **less** than the **next**, **subtract** it.
  * Otherwise, **add** it to the result.

**Time Complexity**: O(n)
**Space Complexity**: O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q9_Roman_To_Integer.md`
Tag your solutions with `Q9` in the repo for tracking and consistency.
