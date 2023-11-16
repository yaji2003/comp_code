def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    # Initialize dictionaries to store character frequencies
    freq_s1 = {}
    freq_s2 = {}

    # Update frequency for string s1
    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1


    for char in s2:
        freq_s2[char] = freq_s2.get(char, 0) + 1

    return freq_s1 == freq_s2

# Example usage:
s1 = input("enter fst string")
s2 = input("enter 2nd string")
result = are_anagrams(s1, s2)

print(f"Are '{s1}' and '{s2}' anagrams? {result}")
