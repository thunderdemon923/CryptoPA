#!/usr/bin/env python3
import argparse
import math
from typing import Optional


# ---------------------------
# 1. Primality detector (Wilson)
# ---------------------------

def is_prime_wilson(n: int) -> bool:
   
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    prod = 1
    for k in range(1, n):
        prod = (prod * k) % n

    return (prod + 1) % n == 0


# ---------------------------
# 2. Willans-style n-th prime
# ---------------------------

def nth_prime_wilson(n: int) -> int:
   
    if n < 1:
        raise ValueError("n must be >= 1")

    upper = 2 ** n  # theoretical upper bound p_n < 2^n

    count = 0
    for k in range(2, upper + 1):
        if is_prime_wilson(k):
            count += 1
            if count == n:
                return k

    raise RuntimeError(f"Failed to find the {n}-th prime below 2**n = {upper}.")


# ---------------------------
# 3. Fast sieve-based n-th prime
# ---------------------------

def _upper_bound_pn(n: int) -> int:
   
    if n < 6:
        # The 5th prime is 11, so 15 is safe.
        return 15

    ln = math.log
    return int(n * (ln(n) + ln(ln(n)))) + 10  # small margin


def nth_prime_sieve(n: int) -> int:
  
    if n < 1:
        raise ValueError("n must be >= 1")

    bound = _upper_bound_pn(n)

    sieve = [True] * (bound + 1)
    sieve[0] = False
    sieve[1] = False

    p = 2
    while p * p <= bound:
        if sieve[p]:
            step = p
            start = p * p
            for multiple in range(start, bound + 1, step):
                sieve[multiple] = False
        p += 1

    count = 0
    for k in range(2, bound + 1):
        if sieve[k]:
            count += 1
            if count == n:
                return k

    raise RuntimeError(
        f"Upper bound {bound} was too small to find the {n}-th prime. "
        f"Increase margin in _upper_bound_pn."
    )


# ---------------------------
# 4. Command-line interface
# ---------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute the n-th prime using 'sieve' (fast) or 'wilson' (slow, Willans-style)."
    )
    parser.add_argument(
        "n",
        type=int,
        help="Index n of the prime to compute (n >= 1).",
    )
    parser.add_argument(
        "--method",
        choices=["sieve", "wilson"],
        default="sieve",
        help="Method: 'sieve' (fast, default) or 'wilson' (Willans-style, extremely slow).",
    )
    args = parser.parse_args()

    if args.method == "sieve":
        result = nth_prime_sieve(args.n)
    else:
        result = nth_prime_wilson(args.n)

    print(result)


if __name__ == "__main__":
    main()
