def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    if m == 0 or m > n:
        return positions

    b = 256          
    
    pattern_hash = 0
    window_hash = 0

    highest_power = b ** (m - 1)

    for j in range(m):
        pattern_hash += ord(pattern[j]) * (b ** (m - 1 - j))
        window_hash  += ord(text[j])    * (b ** (m - 1 - j))

    for i in range(n - m + 1):

        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                positions.append(i)

        if i < n - m:
           
            window_hash -= ord(text[i]) * highest_power
            window_hash *= b
            window_hash += ord(text[i + m])

    return positions

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

print("Naive:", [i for i in range(len(text)) if text.startswith(pattern, i)])
print("Rabin–Karp:", rabin_karp(text, pattern))
