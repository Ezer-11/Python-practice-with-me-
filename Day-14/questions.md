# Day 14 — Python Logic Practice

### 1\. Classify a triangle using a function


Write a function called `classify_triangle(a, b, c)` that determines the type of triangle based on its three side lengths.

Rules\:

- Equilateral: all three sides are equal.
- Isosceles: exactly two sides are equal.
- Scalene: all three sides are different.
- Invalid: the sides cannot form a triangle.

**Input\:**

```text
5 5 8
```

**Output\:**

```text
Isosceles
```

Another example\:

```text
2 3 8
```

Output\:

```text
Invalid Triangle
```

**Requirements\:**

- Use a function.
- Use conditional statements.
- Check the triangle inequality before classification.
- All side lengths must be positive.
#
### 2\. Move all zeros to the end

(Beginner–Intermediate)

Given a list of integers, move all zeros to the end while preserving the relative order of non-zero elements.

**Input\:**

```text
7
0 4 0 2 5 0 8
```

**Output\:**

```text
4 2 5 8 0 0 0
```

**Requirements\:**

- Use loops.
- Do not use `sort()` or `sorted()`\.
- Preserve the order of non-zero elements.
- Try creating a new list.

#
### 3\. Check whether two strings are anagrams


Two strings are anagrams if they contain exactly the same characters with the same frequencies, regardless of their order.

For this problem, ignore spaces and uppercase/lowercase differences.

**Input\:**

```text
Dormitory
Dirty room
```

**Output\:**

```text
Anagrams
```

Another example\:

```text
hello
world
```

Output\:

```text
Not Anagrams
```

**Requirements\:**

- Use a dictionary to count character frequencies.
- Do not use `sorted()`\.
- Do not use `Counter`\.
- Write your own comparison logic.
#
### 4\. Find the pair with the minimum difference

(Intermediate)

Given a list of integers, find two elements whose absolute difference is the smallest.

Print their original indexes and their difference.

**Input\:**

```text
5
8 3 12 5 9
```

**Output\:**

```text
Indexes: 0 4
Minimum difference: 1
```

Explanation: The elements at indexes 0 and 4 are `8` and `9`\.

**Requirements\:**

- Use nested loops.
- Do not sort the list.
- Do not use `min()`\.
- If multiple pairs have the same minimum difference, choose the pair with the smallest first index, then the smallest second index.

#
### 5\. Convert a Roman numeral into an integer


Roman numerals use the following symbols\:

| Symbol | Value |
|--------|--------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Some symbols are subtracted when they appear before a larger symbol.

For example\:

- IV = 4
- IX = 9
- XL = 40
- CM = 900

Write a function\:

```python
def roman_to_int(s):
```

It should return the integer represented by the Roman numeral.

**Input\:**

```text
MCMXCIV
```

**Output\:**

```text
1994
```

Another example\:

```text
LVIII
```

Output\:

```text
58
```

**Requirements\:**

- Use a dictionary.
- Use loops and conditional statements.
- Do not use external libraries.
- Assume the input is a valid standard Roman numeral.


