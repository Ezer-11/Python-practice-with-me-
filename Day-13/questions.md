# Day 13 — Python Logic Practice

### 1\. Convert decimal to binary


Take a positive decimal integer and convert it into its binary representation without using `bin()`\.

**Input\:**

```text
13
```

**Output\:**

```text
1101
```

Another example\:

```text
20
```

Output\:

```text
10100
```

**Requirements\:**

- Use arithmetic operators and loops.
- Do not use `bin()`\.
- Handle `0` correctly.

#
### 2\. Validate a password


Write a program to check whether a password satisfies all these conditions\:

1. At least 8 characters long.
2. Contains at least one uppercase letter.
3. Contains at least one lowercase letter.
4. Contains at least one digit.
5. Contains at least one special character (`!@#$%^&*`\).

**Input\:**

```text
Python123!
```

**Output\:**

```text
Strong Password
```

Another example\:

```text
python123
```

Output\:

```text
Weak Password
```

**Requirements\:**

- Use loops and conditional statements.
- You may use `isupper()`, `islower()` and `isdigit()`\.
- Check all five conditions.
#
### 3\. Find the first non-repeating character


Given a string, find the first character that appears exactly once.

**Input\:**

```text
aabbcdeeff
```

**Output\:**

```text
c
```

Another example\:

```text
aabbcc
```

Output\:

```text
No non-repeating character
```

**Requirements\:**

- Use a dictionary to count character frequencies.
- Preserve the original character order when finding the answer.
- Do not use `count()`\.

#
### 4\. Find all leaders in a list

(Intermediate)

An element is called a leader if it is strictly greater than every element to its right.

The last element is always a leader.

**Input\:**

```text
6
16 17 4 3 5 2
```

**Output\:**

```text
17 5 2
```

Explanation\:

- `17` is greater than everything to its right.
- `5` is greater than `2`\.
- `2` is the last element.

**Requirements\:**

- Use list indexing and loops.
- Preserve the original relative order of leaders.
- Do not use `max()`\.
#

### 5\. Find the row with the maximum sum in a matrix

(Intermediate challenge)

Given a matrix, find the row whose elements have the greatest sum.

Print both the row number (1-based indexing) and its sum.

**Input\:**

```text
3 4
1 2 3 4
10 5 2 1
3 4 5 6
```

**Output\:**

```text
Row: 2
Maximum sum: 18
```

**Requirements\:**

- Use nested lists and loops.
- Write a function named `max_row_sum(matrix)`\.
- Handle negative numbers.
- If multiple rows have the same maximum sum, return the first row.

**Constraints\:**

- `1 ≤ rows, columns ≤ 100`
- Matrix elements can be negative, zero or positive.

