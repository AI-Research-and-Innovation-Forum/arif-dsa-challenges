### 🧠 Q5: Majority Element

**Difficulty**: Easy
**Topic**: Arrays, Hashing, Divide and Conquer, Bit Manipulation
**Platform**: LeetCode
**Challenge ID**: Q5
**Status**: ✅ Solved

---

#### 📄 Problem Statement

Given an array `nums` of size `n`, return the **majority element**.

The **majority element** is the element that **appears more than ⌊n / 2⌋ times**.

You may assume that the majority element **always exists** in the array.

---

#### ✍️ Constraints

* `n == nums.length`
* `1 <= n <= 50,000`
* `-10⁹ <= nums[i] <= 10⁹`

---

#### 🔧 Function Signature

```cpp
int majorityElement(vector<int>& nums);
```

---

#### 📘 Examples

**Example 1:**

```
Input: nums = [3, 2, 3]
Output: 3
Explanation: 3 appears more than n / 2 times (i.e., more than once).
```

**Example 2:**

```
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
Explanation: 2 appears 4 times in a 7-element array.
```

---

#### 🚀 Follow-Up

Can you solve this problem in:

* ✅ **Linear time complexity** (`O(n)`)
* ✅ **Constant space** (`O(1)`)

  > Hint: Consider using **Boyer-Moore Voting Algorithm**.

---

#### 📁 Repository Info

This problem is part of the [ARIF Club](https://github.com/) 🧠 DSA Challenges Repository.
Filename: `Q5_Majority_Element.cpp`
Tag your solutions with `Q5` in the repo for easy navigation.
