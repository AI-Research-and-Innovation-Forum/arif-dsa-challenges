### 🧠 Q4: Remove Duplicates from Sorted Array II

**Difficulty**: Medium
**Topic**: Arrays, Two Pointers
**Platform**: LeetCode
**Challenge ID**: Q4
**Status**: ✅ Solved

---

#### 📄 Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that **each unique element appears at most twice**. The **relative order** of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, the result must be placed in the **first part** of the array `nums`.

**More formally**, if there are `k` elements after removing the duplicates, then the **first `k` elements** of `nums` should hold the final result. It doesn't matter what values are left beyond the first `k` elements.

---

#### ✍️ Constraints

* `1 <= nums.length <= 30,000`
* `-10⁴ <= nums[i] <= 10⁴`
* `nums` is sorted in non-decreasing order

---

#### 🔧 Function Signature

```cpp
int removeDuplicates(vector<int>& nums);
```

---

#### ✅ Custom Judge

The judge will test your solution with the following logic:

```cpp
vector<int> nums = [...];           // Input array
vector<int> expectedNums = [...];   // Expected result

int k = removeDuplicates(nums);     // Calls your implementation

assert k == expectedNums.size();
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, your solution is considered correct.

---

#### 📘 Examples

**Example 1:**

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation:
  The first 5 elements after removing extra duplicates are [1,1,2,2,3].
  Underscore (_) denotes values that can be ignored.
```

**Example 2:**

```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation:
  The first 7 elements are [0,0,1,1,2,3,3].
  Values beyond index 6 can be ignored.
```

---

#### 🚫 Constraints to Follow

* ✅ Do **not** allocate extra space for another array.
* ✅ Modify the input array **in-place**.
* ✅ Use only **O(1)** extra memory.

---

#### 📁 Repository Info

This problem is part of the [ARIF Club](https://github.com/) 🧠 DSA Challenges Repository.
Filename: `Q4_Remove_Duplicates_From_Sorted_Array_II.cpp`
Tag your solutions with `Q4` in the repo for easy navigation.

