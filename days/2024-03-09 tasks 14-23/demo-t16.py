def f(n):
    if n > 2024:
        return n
    else:
        return n * f(n + 1)


print(f(2022))
print(2022 * 2023 * 2024 * 2025)

print(f(2024))
print(2024 * 2025)

print(2022 * 2023)
print(f(2022) / f(2024))

"""
- 1 - prime
- 2 - setrecursionlimit(12_000)
- 3 - @lru_cache
- 3 - self cache
"""