# Willans-Style n-th Prime Calculator

This repository contains a small Python project for computing the n-th prime in two different ways:

1. A **Willans-style method** using a primality detector based on **Wilson's theorem**, together with a very loose theoretical upper bound \(p_n < 2^n\).
2. A **fast method using the Sieve of Eratosthenes** with a sharper upper bound on \(p_n\).

The goal is to illustrate:

- How a **prime detector** can be turned into a **prime computer** (given an index \(n\), compute \(p_n\)).
- Why Willans-style formulas are **theoretically interesting but computationally useless** compared to algorithmic methods like sieves.
- How to compare **time complexities** between different constructions for \(p_n\).

---

## 1. Mathematical Background (Short)

### 1.1 Wilson's theorem as a prime detector

Wilson's theorem states that an integer \(n > 1\) is prime if and only if

\[
(n-1)! \equiv -1 \pmod{n}.
\]

This gives a **primality detector**: for each \(n\), compute \((n-1)! \bmod n\) and check if it equals \(n-1\).  
If yes, \(n\) is prime; otherwise, composite.

In code, we implement:

- `is_prime_wilson(n)` – returns `True` if and only if \(n\) is prime (for \(n \ge 2\)).

This detector is exact but **very slow**: computing \((n-1)!\bmod n\) naively costs \(O(n)\) multiplications.

### 1.2 Turning a detector into a prime computer

We can convert any prime detector into a function that outputs the n-th prime:

1. Fix an upper bound \(U(n)\) such that \(p_n < U(n)\).  
   - Here, for the Willans-style method, we use a very loose bound \(U(n) = 2^n\) (simple but huge).
2. Iterate through integers starting from 2, use the detector to check primality, and **count** primes.
3. Stop when we have found the n-th prime.

This is an algorithmic counterpart of Willans-like formulas that sum over indicators of primality up to a large bound.

### 1.3 Fast method: Sieve-based n-th prime

For a practical method, we use a **sieve of Eratosthenes**:

1. Use a sharper upper bound for \(p_n\). For large enough \(n\), it is known that:
   \[
   p_n < n (\log n + \log \log n).
   \]
2. Run a sieve up to this bound.
3. Collect all primes and return the n-th.

This method is **dramatically faster** than anything based on Wilson’s theorem.

---

## 2. Project Structure

```text
.
├── README.md
├── requirements.txt
└── nth_prime
    ├── __init__.py
    ├── detectors.py
    ├── willans.py
    ├── sieve.py
    └── cli.py
