# Day 8 — Python Logic Practice

### 1\. Calculate the average and count above-average elements


Take `n` integers, calculate their average, and count how many elements are strictly greater than the average.

**Input\:**

```text
5
10 20 30 40 50
```

**Output\:**

```text
Average: 30
Above average: 2
```

**Requirements\:**

- Use a loop to calculate the sum.
- Do not use `statistics.mean()`\.
- Compare each element with the calculated average.
#
### 2\. Replace negative numbers with zero


Take a list of integers. Replace every negative number with `0`, leaving all other elements unchanged.

**Input\:**

```text
6
-3 5 -1 8 0 -7
```

**Output\:**

```text
0 5 0 8 0 0
```

**Requirement\:** Process the list using indexes.
#
### 3\. Remove duplicate elements while preserving order


Given a list of integers, create a new list containing only the first occurrence of each element.

**Input\:**

```text
8
4 2 4 3 2 5 3 6
```

**Output\:**

```text
4 2 3 5 6
```

**Requirements\:**

- Do not use `set()`\.
- Preserve the original order.
- Try using a second list to store unique elements.
#
### 4\. Find the longest common prefix


Given `n` words, find the longest prefix shared by all of them.

**Input\:**

```text
3
flower flow flight
```

**Output\:**

```text
fl
```

Another example\:

```text
3
dog racecar car
```

Output\:

```text
No common prefix
```

**Requirements\:**

- Use loops and string indexing.
- Do not use sorting.
- Handle words of different lengths.
#
### 5\. Transpose a matrix

(Intermediate challenge)

Given a matrix with `r` rows and `c` columns, create its transpose.

The transpose converts rows into columns and columns into rows.

**Input\:**

```text
2 3
1 2 3
4 5 6
```

**Output\:**

```text
1 4
2 5
3 6
```

**Requirements\:**

- Use nested lists and loops.
- Do not use NumPy.
- Write a function named `transpose(matrix)` that returns the transposed matrix.


