from math import factorial

def get_kth_permutation(n, k):
    numbers = list(range(1, n + 1))
    k -= 1  # Adjust k to 0-based index

    result = []
    for i in range(n, 0, -1):
        index, k = divmod(k, factorial(i - 1))
        result.append(numbers.pop(index))

    return result

# Example usage:
n = int(input("enter n"))
k = int(input("enter k"))

kth_permutation = get_kth_permutation(n, k)
print(f"The {k}th permutation of {list(range(1, n + 1))} is: {kth_permutation}")
