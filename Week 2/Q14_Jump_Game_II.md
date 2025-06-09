
### 🧠 Week 2 – Q14: Jump Game II

**Difficulty**: Medium
**Topic**: Greedy / Dynamic Programming
**Platform**: LeetCode
**Challenge ID**: Q14
**Status**: 🔓 Open

---

#### 📄 Problem Statement

You are given a **0-indexed** array of integers `nums` of length `n`. Each element `nums[i]` represents the **maximum forward jump length** from index `i`.

Return the **minimum number of jumps** needed to reach the last index.
You can **guarantee** that it is always possible to reach `nums[n - 1]`.

---

#### ✍️ Constraints

* `1 <= nums.length <= 10⁴`
* `0 <= nums[i] <= 1000`
* Guaranteed to be solvable

---

#### 🔧 Function Signature

```cpp
int jump(vector<int>& nums);
```

---

#### 📘 Examples

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: Jump from index 0 -> 1 -> 4
```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

---

#### 🚀 Approach

**Greedy Solution (Optimized):**

* Track:

  * `jumps`: number of jumps made
  * `currentEnd`: current range of the jump
  * `farthest`: the farthest index we can reach in the current jump window
* For each index `i`:

  * Update `farthest = max(farthest, i + nums[i])`
  * If `i == currentEnd`:

    * Make a jump
    * Update `currentEnd = farthest`

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

#### 📁 Submission Format

Please name your solution file as:

```
Q14_<yourname>.cpp
```

✅ Place it in the `Week2/` folder of the repo.
