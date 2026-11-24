# 🐍 Day 12 — Python Problem-Solving Practice

> **Goal:** Strengthen Python fundamentals through practical logic-building problems.

##  Today's Focus

- Conditional statements
- String manipulation
- List traversal and indexing
- Dictionary operations
- Functions and recursion

**Total Questions:** 5  
**Difficulty:** Beginner → Intermediate

---

## 1. Calculate an Electricity Bill

**Difficulty:** Beginner

Calculate an electricity bill using the following rates:

| Electricity Units | Rate |
|:---|---:|
| First 100 units | ₹2/unit |
| Next 100 units | ₹3/unit |
| Above 200 units | ₹5/unit |

Add a fixed charge of ₹20 to every bill.

**Example Input**
```text
250
```

**Expected Output**
```text
Total bill: 770
```

**Requirements**
- Use `if-elif-else`.
- Handle zero units.
- Calculate each electricity slab correctly.

---

## 2.  Reverse the Order of Words

**Difficulty:** Beginner–Intermediate

Take a sentence and reverse the order of its words without reversing the individual words.

**Example Input**
```text
Python makes logic stronger
```

**Expected Output**
```text
stronger logic makes Python
```

**Requirements**
- You may use `split()`.
- Do not use `reverse()` or `reversed()`.
- Use loops and list indexing.

---

## 3. Find the Longest Consecutive Repetition

**Difficulty:** Intermediate

Given a list of integers, find the maximum number of times the same element appears consecutively.

**Example Input**
```text
9
1 1 2 2 2 3 3 3 3
```

**Expected Output**
```text
4
```

**Explanation:** The number `3` appears four consecutive times.

**Requirements**
- Use a loop.
- Compare adjacent elements.
- Do not use `count()`.
- Handle a list containing only one element.

---

## 4. Update Product Inventory Using a Dictionary

**Difficulty:** Intermediate

A shop stores product quantities in a dictionary. Process transactions that add or remove stock.

**Example Input**
```text
3
Apple 10
Banana 20
Mango 15
4
Apple 5
Banana -3
Mango 10
Apple -2
```

**Expected Output**
```text
Apple: 13
Banana: 17
Mango: 25
```

**Requirements**
- Store products and quantities in a dictionary.
- Update dictionary values using a loop.
- Do not allow stock to become negative.
- Assume every transaction refers to an existing product.

---

## 5.  Calculate List Sum Using Recursion

**Difficulty:** Intermediate Challenge

Write a recursive function:

```python
def recursive_sum(numbers):
```

It must return the sum of all elements in a list.

**Example Input**
```text
5
10 20 30 40 50
```

**Expected Output**
```text
150
```

**Requirements**
- Use recursion.
- Do not use `sum()`.
- Do not use loops inside the function.
- Define a proper base case.
- An empty list must return `0`.

---

##  Learning Objectives

By completing these problems, you should be able to:

- Apply conditional logic to real-world calculations.
- Manipulate strings and lists using indexes.
- Compare consecutive list elements.
- Store and update data using dictionaries.
- Understand recursive functions and base cases.

---

##  Submission Checklist

- [ ] Question 1 — Electricity Bill
- [ ] Question 2 — Reverse Words
- [ ] Question 3 — Consecutive Repetition
- [ ] Question 4 — Product Inventory
- [ ] Question 5 — Recursive Sum

## Progress Tracker

| Metric | Status |
|:---|:---|
| Questions attempted | 0 / 5 |
| Questions completed | 0 / 5 |
| Solutions reviewed | Pending |
| Difficulty | Beginner–Intermediate |

---

**Remember:** Focus on understanding the logic rather than copying solutions. Test your programs with different inputs and edge cases.
