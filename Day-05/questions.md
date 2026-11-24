# Day 5 — Python Logic Practice

### 1\. Count different character types


Take a string and count\:

- Uppercase letters
- Lowercase letters
- Digits
- Special characters

Spaces should not count in any category.

**Input\:**

```text
Hello123! Python
```

**Output\:**

```text
Uppercase: 2
Lowercase: 9
Digits: 3
Special characters: 1
```

#
### 2\. Print a number triangle


Take an integer `n` and print the following pattern.

**Input\:**

```text
5
```

**Output\:**

```text
1
12
123
1234
12345
```

**Requirement\:** Use nested loops. Do not print each row manually.
#
### 3\. Find common elements in two lists

(Medium)

Take two integer lists and print their common distinct elements in the order they first appear in the first list.

**Input\:**

```text
6
1 2 3 2 4 5
5
2 4 6 2 1
```

**Output\:**

```text
2 4 1
```

**Requirements\:**

- Do not use set intersection.
- Do not print duplicate common elements.
- Preserve the order from the first list.
#
### 4\. Check whether a list is a palindrome


A list is a palindrome if it reads the same forward and backward.

Determine whether the given list is a palindrome.

**Input\:**

```text
5
1 2 3 2 1
```

**Output\:**

```text
Palindrome
```

Another example\:

```text
4
1 2 3 4
```

Output\:

```text
Not Palindrome
```

**Requirements\:**

- Do not use `reverse()`\.
- Do not use slicing (`[::-1]`\).
- Try comparing elements using indexes from both ends.
#
### 5\. Find the GCD using a function


Write a function called `gcd(a, b)` that returns the greatest common divisor of two non-negative integers.

The GCD is the largest positive integer that divides both numbers exactly.

**Input\:**

```text
48 18
```

**Output\:**

```text
6
```

Another example\:

```text
20 15
```

Output\:

```text
5
```S

**Requirements\:**

- You must write your own function.
- Do not use `math.gcd()`\.
- Try solving it using the Euclidean algorithm.
- Handle the case where one number is zero, provided the other is positive.

**Constraint\:** `0 ≤ a, b ≤ 10^9`, with at least one number positive.

