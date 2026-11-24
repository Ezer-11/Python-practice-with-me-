# Day 9 — Python Logic Practice

### 1\. Check whether a number is automorphic


An automorphic number is a number whose square ends with the number itself.

For example\:

- \(25^2 = 625\)
- \(76^2 = 5776\)

Take an integer and determine whether it is automorphic.

**Input\:**

```text
25
```

**Output\:**

```text
Automorphic
```

Another example\:

```text
12
```

Output\:

```text
Not Automorphic
```

**Requirements\:**

- Use arithmetic operations.
- Do not convert the number into a string.
#
### 2\. Print a hollow rectangle pattern


Take the number of rows and columns and print a rectangle whose boundary consists of stars and whose interior is empty.

**Input\:**

```text
4 5
```

**Output\:**

```text
*****
*   *
*   *
*****
```

**Requirements\:**

- Use nested loops.
- Do not manually print individual rows.
- Handle rectangles with only one row or one column.
#
### 3\. Find all peak elements in a list

(Intermediate)

An element is a peak if it is strictly greater than its immediate neighbors.

For the first and last elements, compare against their only existing neighbor.

**Input\:**

```text
7
1 3 2 5 4 6 1
```

**Output\:**

```text
3 5 6
```

**Requirements\:**

- Use list indexing.
- Preserve the original order.
- Do not use `max()`\.

#
### 4\. Find the most frequent word in a sentence

(Intermediate)

Take a sentence and find the word that occurs most frequently.

**Input\:**

```text
red blue red green blue red
```

**Output\:**

```text
red 3
```

**Requirements\:**

- Use a dictionary to count frequencies.
- Ignore uppercase/lowercase differences.
- If two words have the same highest frequency, choose the one that appeared first.
- Words are separated by spaces.
#
### 5\. Calculate the boundary sum of a matrix


Given a rectangular matrix, calculate the sum of all elements on its outer boundary.

The boundary consists of\:

- First and last rows.
- First and last columns.
- Each boundary element must be counted only once.

**Input\:**

```text
3 4
1 2 3 4
5 6 7 8
9 10 11 12
```

**Output\:**

```text
65
```

**Requirements\:**

- Use nested lists and indexes.
- Write a function called `boundary_sum(matrix)`\.
- Handle single-row and single-column matrices correctly.


