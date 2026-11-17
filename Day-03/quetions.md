# Day 03 — Indexing, Iteration & Problem Solving

Main focus: List indexing, adjacent elements, nested logic, and building problem-solving skills.


Q1. Find the first occurrence index

Given a list and a target number, find the index of its first occurrence.
numbers = [10, 20, 30, 20, 40]target = 20



Expected output:
1


Rules:
- Don't use .index().
- Don't use in to search.
- Use a loop.
- If the target doesn't exist, print -1.

Q2. Count descending adjacent pairs

Count how many times an element is greater than the element immediately after it.
numbers = [9, 5, 7, 3, 2, 8]



Expected output:
3

Q3. Move all zeros to the end

Move every zero to the end of the list while preserving the original order of non-zero elements.
numbers = [0, 5, 0, 3, 8, 0, 2]



Expected output:
[5, 3, 8, 2, 0, 0, 0]


Rules:
- Don't use sort() or sorted().
- Preserve the order of non-zero elements.

Q4. Check whether two strings are anagrams

Two strings are anagrams if they contain exactly the same characters with the same frequencies, but in a different order.
word1 = "listen"word2 = "silent"

Expected output:
True

Rules:
- Ignore uppercase/lowercase differences.
- Ignore spaces.
- Don't use sorting.

Q5. Find the longest strictly increasing contiguous sequence

Find the length of the longest continuous section in which every next element is greater than the previous one.
numbers = [1, 2, 3, 2, 4, 5, 6, 1]



Expected output:
4

Explanation: The longest strictly increasing contiguous sequence is [2, 4, 5, 6].