### 🧠 Q7: Best Time to Buy and Sell Stock

**Difficulty**: Easy
**Topic**: Arrays, Dynamic Programming, Greedy
**Platform**: LeetCode
**Challenge ID**: Q7
**Status**: ✅ Solved

---

#### 📄 Problem Statement

You are given an array `prices` where `prices[i]` represents the price of a given stock on the `i-th` day.

You want to maximize your **profit** by choosing a **single day to buy one stock** and a **different day in the future to sell** that stock.

Return the **maximum profit** you can achieve from this transaction.
If no profit is possible, return `0`.

---

#### ✍️ Constraints

* `1 <= prices.length <= 10⁵`
* `0 <= prices[i] <= 10⁴`

---

#### 🔧 Function Signature

```cpp
int maxProfit(vector<int>& prices);
```

---

#### 📘 Examples

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation:
  Buy on day 2 (price = 1)  
  Sell on day 5 (price = 6)  
  Profit = 6 - 1 = 5
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation:
  No profitable transaction possible.
```

---

#### 🚀 Optimal Approach

* Track the **minimum price so far**
* For each day, compute the potential profit `prices[i] - minPrice`
* Update the maximum profit accordingly

**Time Complexity**: O(n)
**Space Complexity**: O(1)

---

#### 📁 Repository Info

This problem is part of the [ARIF Club DSA Challenges Repo](https://github.com/AI-Research-and-Innovation-Forum/arif-dsa-challenges).
Filename: `Q7_Best_Time_To_Buy_And_Sell_Stock.md`
Tag your solutions with `Q7` in the repo for consistency and clarity.
