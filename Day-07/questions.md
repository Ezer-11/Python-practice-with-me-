# Day 7 — Python Logic Practice

### Q1. Calculate the sum of digits using a function

(Beginner)

Write a function `digit_sum(n)` that returns the sum of all digits of a non-negative integer.

**Input\:**

```text
5832
```

**Output\:**

```text
18
```

Requirements\:

- Use a function.
- Do not convert the number into a string.
- Use arithmetic and a loop.

#
### Q2. Find the product of non-zero elements

(Beginner)

Take a list of integers and calculate the product of all non-zero elements.

**Input\:**

```text
6
2 0 3 4 0 5
```

**Output\:**

```text
120
```

If every element is zero, print `1`\.

Requirement: Use a loop, not `math.prod()`\.
#
### Q3. Compress consecutive repeated characters

(Intermediate)

Given a string, compress consecutive occurrences of the same character by writing the character followed by its count.

**Input\:**

```text
aaabbccccdaa
```

**Output\:**

```text
a3b2c4d1a2
```

Another example\:

```text
abcd
```

Output\:

```text
a1b1c1d1
```

Requirements\:

- Use a loop.
- Do not use regular expressions.
- Preserve the original character order.
#
### Q4. Find the student with the highest marks using a dictionary

(Intermediate)

Take the names and marks of `n` students. Store them in a dictionary and find the student with the highest marks.

**Input\:**

```text
4
Rahul 78
Aman 92
Priya 85
Ravi 88
```

**Output\:**

```text
Aman 92
```

If two students have equal highest marks, print the one who appeared first.

Requirements\:

- Use a dictionary.
- Use a loop to find the highest marks.
- Do not use `max()`\.
#
### Q5. Calculate the main diagonal sum of a matrix

(Intermediate challenge)

Take an `n × n` matrix and calculate the sum of its main diagonal elements.

**Input\:**

```text
3
1 2 3
4 5 6
7 8 9
```

**Output\:**

```text
15
```

Explanation: The main diagonal contains `1, 5, 9`\.

Requirements\:

- Use nested lists.
- Use indexes to access diagonal elements.
- Write a function called `diagonal_sum(matrix)` that returns the result.

---
