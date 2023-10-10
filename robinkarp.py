def rabin_karp_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    
    pattern_hash = sum(ord(pattern[i]) for i in range(m))
    
    for i in range(n - m + 1):
        text_hash = sum(ord(text[i + j]) for j in range(m))
        
        if text_hash == pattern_hash:
            if text[i:i+m] == pattern:
                matches.append(i)
    
    return matches

text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

matches = rabin_karp_string_match(text, pattern)

if matches:
    print(f"Pattern found at positions: {matches}")
else:
    print("Pattern not found in the text.")
