# Problem Description

```text
LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length
Category: Sliding Window
Difficulty: MEDIUM
URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

=== Description ===
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.



Vowel letters in English are `&#39;a&#39;`, `&#39;e&#39;`, `&#39;i&#39;`, `&#39;o&#39;`, and `&#39;u&#39;`.



 


Example 1:



```

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

```



Example 2:



```

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

```



Example 3:



```

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

```



 


Constraints:




	- `1 <= s.length <= 105`

	- `s` consists of lowercase English letters.

	- `1 <= k <= s.length`
```

## Solution

See [`solution.py`](./solution.py) for the implementation.
