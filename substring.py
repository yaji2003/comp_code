from collections import Counter

def min_window_substring(s, t):
    if not s or not t:
        return ""

    t_counter = Counter(t)
    
    required_chars = len(t)
    left, right = 0, 0
    min_len = float('inf')
    min_window = ""

    while right < len(s):
        
        if t_counter[s[right]] > 0:
            required_chars -= 1
        t_counter[s[right]] -= 1
        right += 1

     
        while required_chars == 0:
            
            if right - left < min_len:
                min_len = right - left
                min_window = s[left:right]

            t_counter[s[left]] += 1
            if t_counter[s[left]] > 0:
                required_chars += 1
            left += 1

    return min_window


s = "ADOBECODEBANC"
t = "ABC"

result = min_window_substring(s, t)
print(f"The minimum window substring is: {result}")
