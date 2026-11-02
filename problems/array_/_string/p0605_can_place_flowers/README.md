# Problem Description

```text
LeetCode 605: Can Place Flowers
Category: Array / String
Difficulty: EASY
URL: https://leetcode.com/problems/can-place-flowers/

=== Description ===
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.



Given an integer array `flowerbed` containing `0`&#39;s and `1`&#39;s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the `flowerbed` without violating the no-adjacent-flowers rule and `false` otherwise.



 


Example 1:


```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

```

Example 2:


```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

```


 


Constraints:




	- `1 <= flowerbed.length <= 2 * 104`

	- `flowerbed[i]` is `0` or `1`.

	- There are no two adjacent flowers in `flowerbed`.

	- `0 <= n <= flowerbed.length`
```

## Solution

See [`solution.py`](./solution.py) for the implementation.
