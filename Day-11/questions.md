# Day 11 — Python Logic Practice

### 1\. Check whether a number is an Armstrong number


An Armstrong number is a number equal to the sum of its digits, each raised to the power of the total number of digits.

For example\:

\[
153 = 1^3 + 5^3 + 3^3
\]

Write a program to check whether a number is an Armstrong number.

**Input\:**

```text
153
```

**Output\:**

```text
Armstrong Number
```

Another example\:

```text
154
```

Output\:

```text
Not Armstrong
```

**Requirements\:**

- Use loops and arithmetic.
- Handle single-digit numbers.
- Do not use external libraries.
#
### 2\. Group words by their length

(Beginner–Intermediate)

Take `n` words and group them according to their length using a dictionary.

Display the groups in ascending order of word length. Preserve the original order of words within each group.

**Input\:**

```text
6
cat apple dog banana ant elephant
```

**Output\:**

```text
3: cat dog ant
5: apple
6: banana
8: elephant
```

**Requirements\:**

- Use a dictionary.
- Dictionary values should contain lists of words.
- Do not use `groupby()`\.
#
### 3\. Rearrange a list: even numbers before odd numbers


Given a list of integers, rearrange it so that all even numbers appear before all odd numbers.

Preserve the relative order of elements within both groups.

**Input\:**

```text
8
3 8 5 2 7 4 9 6
```

**Output\:**

```text
8 2 4 6 3 5 7 9
```

**Requirements\:**

- Use loops.
- Do not use `sort()` or `sorted()`\.
- Do not use `filter()`\.
- Try using a new list.
#
### 4\. Find the equilibrium index

(Intermediate)

An equilibrium index is an index where the sum of all elements to its left equals the sum of all elements to its right.

The element at the equilibrium index is excluded from both sums.

**Input\:**

```text
5
1 3 5 2 2
```

**Output\:**

```text
2
```

Explanation\:

- Left sum: `1 + 3 = 4`
- Right sum: `2 + 2 = 4`

If multiple equilibrium indexes exist, print the first one. If none exists, print `-1`\.

**Requirements\:**

- Use list indexing and loops.
- Try to solve this in \(O(n)\) time rather than \(O(n^2)\)\.
- Constraint: `1 ≤ n ≤ 100000`
#
### 5\. Implement Binary Search


Write a function\:

```python
def binary_search(numbers, target):
```

The function should return the index of the target element if it exists, otherwise return `-1`\.

Binary search works by repeatedly dividing a sorted search range into halves.

**Input\:**

```text
7
2 5 8 12 16 23 38
16
```

**Output\:**

```text
4
```

Another example\:

```text
7
2 5 8 12 16 23 38
10
```

Output\:

```text
-1
```

**Requirements\:**

- The list is sorted in ascending order.
- Use `low`, `high` and `mid` variables.
- Do not use `in`, `index()` or any built-in searching method.
- Use a function.
- Target any matching index if duplicates exist.


