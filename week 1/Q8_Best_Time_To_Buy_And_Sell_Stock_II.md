
### 🧠 Q8: Best Time to Buy and Sell Stock II

**Difficulty**: Medium
**Topic**: Arrays, Greedy, Dynamic Programming
**Platform**: LeetCode
**Challenge ID**: Q8
**Status**: ✅ Solved

---

#### 📄 Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

On each day, you may **buy and/or sell** the stock. You can only **hold at most one share** of the stock at a time.
However, you can **buy and sell on the same day**.

Return the **maximum profit** you can achieve.

---

#### ✍️ Constraints

* `1 <= prices.length <= 30,000`
* `0 <= prices[i] <= 10,000`

---

#### 🔧 Function Signature

```cpp
int maxProfit(vector<int>& prices);
```

---

#### 📘 Examples

**Example 1:**

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 7
Explanation:
  Buy on day 2 (1), sell on day 3 (5), profit = 4  
  Buy on day 4 (3), sell on day 5 (6), profit = 3  
  Total profit = 4 + 3 = 7
```

**Example 2:**

```
Input: prices = [1, 2, 3, 4, 5]
Output: 4
Explanation:
  Buy on day 1 (1), sell on day 5 (5), profit = 4
```

**Example 3:**

```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation:
  No profitable transaction is possible.
```

---

#### 🚀 Optimal Strategy

This is a classic **greedy** problem:

* Any time `prices[i] > prices[i - 1]`, **take the profit**.
* You don’t need to track exact buy/sell days — just sum all upward price differences.

**Time Complexity**: O(n)
**Space Complexity**: O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q8_Best_Time_To_Buy_And_Sell_Stock_II.md`
Tag your solutions with `Q8` in the repo for consistency and easy tracking.
