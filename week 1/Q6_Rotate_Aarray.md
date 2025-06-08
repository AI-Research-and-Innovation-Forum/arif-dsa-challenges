### 🧠 Q6: Rotate Array

**Difficulty**: Medium
**Topic**: Arrays, Two Pointers, In-Place Algorithms
**Platform**: LeetCode
**Challenge ID**: Q6
**Status**: ✅ Solved

---

#### 📄 Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

---

#### ✍️ Constraints

* `1 <= nums.length <= 10⁵`
* `-2³¹ <= nums[i] <= 2³¹ - 1`
* `0 <= k <= 10⁵`

---

#### 🔧 Function Signature

```cpp
void rotate(vector<int>& nums, int k);
```

---

#### 📘 Examples

**Example 1:**

```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3  
Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:
After 1 step: [7, 1, 2, 3, 4, 5, 6]  
After 2 steps: [6, 7, 1, 2, 3, 4, 5]  
After 3 steps: [5, 6, 7, 1, 2, 3, 4]
```

**Example 2:**

```
Input: nums = [-1, -100, 3, 99], k = 2  
Output: [3, 99, -1, -100]
```

---

#### 🚀 Follow-Up Challenges

* ✅ Try to come up with **multiple solutions** (there are at least **three**).
* ✅ Can you solve it **in-place** using only **O(1)** extra space?

> 💡 Tip: Think about reversing sections of the array!

---

#### 🧠 Approaches You Can Try

1. **Brute Force**: Rotate one by one — Time: O(k\*n), Space: O(1)
2. **Using Extra Array** — Time: O(n), Space: O(n)
3. **In-place Reversal (Optimal)** — Time: O(n), Space: O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q6_Rotate_Array.cpp`
Tag your solutions with `Q6` in the repo for easy access and tracking.

