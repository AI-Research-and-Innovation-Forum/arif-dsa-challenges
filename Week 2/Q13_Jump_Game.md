
### 🧠 Week 2 – Q13: Jump Game

**Difficulty**: Medium
**Topic**: Dynamic Programming / Greedy
**Platform**: LeetCode
**Challenge ID**: Q13
**Status**: 🔓 Open

---

#### 📄 Problem Statement

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your **maximum jump length** at that position.

Return `true` if you can reach the **last index**, or `false` otherwise.

---

#### ✍️ Constraints

* `1 <= nums.length <= 10⁴`
* `0 <= nums[i] <= 10⁵`

---

#### 🔧 Function Signature

```cpp
bool canJump(vector<int>& nums);
```

---

#### 📘 Examples

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3, which has a jump length of 0.
```

---

#### 🚀 Approach

**Greedy Solution:**

* Track the furthest index you can reach.
* Iterate through the array:

  * If current index `i` is beyond the max reachable index, return `false`.
  * Update max reachable index as `max(maxReach, i + nums[i])`.
* If the loop ends without returning false, return true.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

#### 📁 Submission Format

Please name your solution file as:

```
Q13_<yourname>.cpp
```

✅ Make sure to test your code and submit a clean, well-commented version.
📌 Commit it under `Week2/` folder in the repo.
