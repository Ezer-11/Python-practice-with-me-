# Day 6 — Python Logic Practice

### 1\. Count even digits in a number


Take a non-negative integer and count how many of its digits are even.

Remember that `0` is also an even digit.

**Input\:**

```text
2847310
```

**Output\:**

```text
4
```

**Requirements\:**

- Do not convert the number into a string.
- Use a loop and arithmetic operators.

#
### 2\. Find the longest word in a sentence


Take a sentence and print its longest word. If multiple words have the same maximum length, print the first one.

**Input\:**

```text
Python makes programming enjoyable
```

**Output\:**

```text
programming
```

**Requirements\:**

- Use a loop.
- You may use `split()`\.
- Do not use `max()`\.

#
### 3\. Find a pair whose sum equals the target


Given a list of integers and a target, find the indexes of the first pair whose sum equals the target.

Consider pairs in increasing order of the first index, then the second index.

**Input\:**

```text
5
2 7 11 15 3
9
```

**Output\:**

```text
0 1
```

Explanation: `2 + 7 = 9`\.

If no pair exists, print `-1`\.

**Requirements\:**

- Use nested loops.
- Do not sort the list.
- Do not use a built-in pair-searching function.
#
### 4\. Find the missing number


You are given `n-1` distinct integers from the range `1` to `n`\. Exactly one number is missing.

Find the missing number.

**Input\:**

```text
5
1 2 4 5
```

**Output\:**

```text
3
```

**Constraints\:**

- `2 ≤ n ≤ 100000`
- All supplied numbers are distinct.
- Every number belongs to the range `1` to `n`\.

Try to solve it without sorting.
#
### 5\. Merge two sorted lists


You are given two lists already sorted in non-decreasing order. Merge them into one sorted list.

**Input\:**

```text
4
1 4 7 9
3
2 5 8
```

**Output\:**

```text
1 2 4 5 7 8 9
```

**Requirements\:**

- Do not use `sort()` or `sorted()`\.
- Try using indexes to traverse both lists.
- Write a function named `merge(a, b)` that returns the merged list.
- Handle lists of different lengths and duplicate values.

