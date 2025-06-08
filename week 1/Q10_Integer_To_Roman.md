
### 🧠 Q10: Integer to Roman

**Difficulty**: Medium
**Topic**: Math, Strings, Simulation
**Platform**: LeetCode
**Challenge ID**: Q10
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

Roman numerals are formed by appending symbols from highest to lowest value following these rules:

* If the current value does **not** start with 4 or 9, append the symbol with the maximal value that can be subtracted from the number, subtract it, and repeat.
* If the current value starts with 4 or 9, use the **subtractive notation**:

  * 4 → IV (1 less than 5)
  * 9 → IX (1 less than 10)
  * 40 → XL (10 less than 50)
  * 90 → XC (10 less than 100)
  * 400 → CD (100 less than 500)
  * 900 → CM (100 less than 1000)
* Symbols I, X, C, and M can be repeated up to 3 times consecutively.
* Symbols V, L, and D cannot be repeated.
* For 4 repetitions, use subtractive notation instead.

Given an integer `num`, convert it to its Roman numeral representation.

---

#### ✍️ Constraints

* `1 <= num <= 3999`

---

#### 🔧 Function Signature

```cpp
string intToRoman(int num);
```

---

#### 📘 Examples

**Example 1:**

```
Input: num = 3749
Output: "MMMDCCXLIX"

Explanation:
3000 = MMM
700 = DCC
40 = XL
9 = IX
```

**Example 2:**

```
Input: num = 58
Output: "LVIII"

Explanation:
50 = L
8 = VIII
```

**Example 3:**

```
Input: num = 1994
Output: "MCMXCIV"

Explanation:
1000 = M
900 = CM
90 = XC
4 = IV
```

---

#### 🚀 Optimal Strategy

* Use arrays or maps of Roman numeral symbols and their values ordered from highest to lowest.
* Iteratively subtract the largest possible symbol value from `num` and append the symbol to the result.
* Continue until `num` reduces to zero.

**Time Complexity**: O(1) (since max input is fixed at 3999)
**Space Complexity**: O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q10_Integer_To_Roman.md`
Tag your solutions with `Q10` for consistency and easy tracking.

