# n-th Prime via Willans-Style and Sieve (GitHub Codespaces Ready)

This repository implements two ways to compute the n-th prime:

1. **Willans-style / Wilson-based method**  
   - Uses Wilson's theorem as a primality detector.  
   - Extremely slow, only for very small `n` (like `n <= 6`).  
   - Included to show the idea behind constructions like Willans' formula.

2. **Fast Sieve method**  
   - Uses a Sieve of Eratosthenes with a good upper bound on \( p_n \).  
   - Practical and fast for reasonable `n`.

Everything is contained in a **single file**: `nth_prime.py`.

---

## 1. Run in GitHub Codespaces

1. Push this repo to GitHub.
2. On GitHub, click the green **Code** button → **Codespaces** tab → **Create codespace on main**.
3. Wait for the Codespace to open in the browser (VS Code UI).
4. In the integrated terminal at the bottom, run:

```bash
python nth_prime.py 10
