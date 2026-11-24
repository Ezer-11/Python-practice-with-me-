# Day 10 — Python Logic Practice

### 1\. Check whether a number is perfect


A perfect number is a positive integer equal to the sum of all its positive divisors excluding itself.

For example\:

\(6 = 1 + 2 + 3\)

Determine whether the given number is perfect.

**Input\:**

```text
28
```

**Output\:**

```text
Perfect Number
```

Another example\:

```text
12
```

Output\:

```text
Not a Perfect Number
```

**Requirements\:**

- Use a loop.
- Do not use external libraries.
- Handle `1` correctly.
#
### 2\. Check whether two strings are rotations

(Beginner–Intermediate)

Two strings are rotations if one can be obtained by moving some characters from the beginning to the end of the other, without changing their relative order.

**Input\:**

```text
waterbottle
erbottlewat
```

**Output\:**

```text
Rotation
```

Another example\:

```text
hello
world
```

Output\:

```text
Not Rotation
```

**Requirements\:**

- Compare the strings logically.
- Do not use sorting.
- Handle strings of different lengths.
#
### 3\. Find the second-largest distinct element

(Intermediate)

Given a list of integers, find the second-largest distinct number.

**Input\:**

```text
7
12 35 1 10 34 35 20
```

**Output\:**

```text
34
```

If no second-largest distinct element exists, print\:

```text
No second largest element
```

**Requirements\:**

- Do not use `sort()`, `sorted()` or `max()`\.
- Use loops and conditions.
- Try solving in a single traversal of the list.

**Constraint\:** `1 ≤ n ≤ 100000`
#
### 4\. Find the first and last occurrence of a target

(Intermediate)

Given a list of integers and a target number, find the index of its first occurrence and its last occurrence.

**Input\:**

```text
8
4 2 7 2 9 2 5 2
2
```

**Output\:**

```text
First occurrence: 1
Last occurrence: 7
```

If the target doesn't exist, print\:

```text
-1 -1
```

**Requirements\:**

- Use loops and indexing.
- Do not use `index()` or `count()`\.
- Try to solve it with a single traversal.
#
### 5\. Implement Bubble Sort

(Intermediate challenge)

Write a function called `bubble_sort(numbers)` that sorts a list in ascending order using the Bubble Sort algorithm.

Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

**Input\:**

```text
6
64 34 25 12 22 11
```

**Output\:**

```text
11 12 22 25 34 64
```

**Requirements\:**

- Write your own function.
- Do not use `sort()` or `sorted()`\.
- Use nested loops.
- Try to avoid unnecessary passes when the list is already sorted.

**Constraint\:** `1 ≤ n ≤ 1000`

