# Prefix Sum Technique

The **prefix sum** (also known as cumulative sum) is a powerful algorithmic technique used to efficiently compute the sum of elements in a subarray or range of an array. It is widely used in problems involving range queries, array manipulation, and optimization.

## Definition

Given an array `A` of length `n`, the prefix sum array `P` is defined as:

- `P[0] = 0`
- `P[i] = A[0] + A[1] + ... + A[i-1]` for `1 <= i <= n`

Alternatively, for 0-based indexing:

- `P[i] = A[0] + A[1] + ... + A[i]` for `0 <= i < n`

## Construction

To construct the prefix sum array in O(n) time:

```python
A = [a0, a1, a2, ..., an-1]
P = [0] * (n + 1)
for i in range(1, n + 1):
    P[i] = P[i-1] + A[i-1]
```
