### 🧠 Week 2 – Q15: H-Index

**Difficulty**: Medium
**Topic**: Sorting / Counting
**Platform**: LeetCode
**Challenge ID**: Q15
**Status**: 🔓 Open

---

#### 📄 Problem Statement

You are given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`th paper. Return the researcher's **h-index**.

👉 The **h-index** is defined as the maximum value of `h` such that the researcher has published at least `h` papers that have each been cited at least `h` times.

---

#### ✍️ Constraints

* `n == citations.length`
* `1 <= n <= 5000`
* `0 <= citations[i] <= 1000`

---

#### 🔧 Function Signature

```cpp
int hIndex(vector<int>& citations);
```

---

#### 📘 Examples

**Example 1:**

```
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: The researcher has 3 papers with at least 3 citations each.
```

**Example 2:**

```
Input: citations = [1,3,1]
Output: 1
```

---

#### 🚀 Approach

**Approach 1: Sort + Linear Scan**

* Sort the citations array in descending order.
* Iterate through the sorted list.
* At each index `i`, check if `citations[i] >= i+1`.
* The maximum `i+1` satisfying the condition is the h-index.

**Time Complexity:** O(n log n) (because of sorting)
**Space Complexity:** O(1) or O(n) depending on the sort implementation.

---

#### 📁 Submission Format

Please name your solution file as:

```
Q15_<yourname>.cpp
```

✅ Place it in the `Week2/` folder of the repo.
